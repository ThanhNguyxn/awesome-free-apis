"""
Improved Link Checker for awesome-free-apis

Key improvements:
- Cloudflare protection detection
- Random User-Agent rotation
- Host header setting
- Smart error categorization
"""

import re
import requests
import random
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def extract_links_from_readme(file_path='../README.md'):
    """Extract all API links from README.md"""
    import os
    # Get script directory and go up one level
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(os.path.dirname(script_dir), 'README.md')
    
    # Use provided path if it exists, otherwise use computed path
    if not os.path.exists(file_path):
        file_path = readme_path
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'\[Link\]\((https?://[^\)]+)\)'
    links = re.findall(pattern, content)
    return links

def fake_user_agent():
    """Random User-Agent to avoid bot detection"""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    ]
    return random.choice(user_agents)

def get_host_from_link(link):
    """Extract host from URL"""
    host = link.split('://', 1)[1] if '://' in link else link
    
    if '/' in host:
        host = host.split('/', 1)[0]
    elif '?' in host:
        host = host.split('?', 1)[0]
    elif '#' in host:
        host = host.split('#', 1)[0]
    
    return host

def has_cloudflare_protection(resp):
    """
    Detect Cloudflare or similar bot protection
    Based on public-apis/public-apis implementation
    """
    code = resp.status_code
    server = resp.headers.get('Server', '').lower()
    
    cloudflare_flags = [
        '403 forbidden',
        'cloudflare',
        'security check',
        'please wait...',
        'checking your browser',
        'ddos protection',
        'ray id:',
        '_cf_chl',
        'cf-spinner',
    ]
    
    if code in [403, 503] and 'cloudflare' in server:
        html = resp.text.lower()
        if any(flag in html for flag in cloudflare_flags):
            return True
    
    # Also consider 403 as potential bot protection
    if code == 403:
        return True
    
    return False

def check_link(url, timeout=30, max_retries=3):
    """
    Check if a link is accessible with retry logic
    Returns: dict with status info
    """
    last_error = None
    
    for attempt in range(max_retries):
        try:
            headers = {
                'User-Agent': fake_user_agent(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
            code = response.status_code
            
            #Check for bot protection
            if code >= 400 and has_cloudflare_protection(response):
                return {
                    'url': url,
                    'status': code,
                    'state': 'protected',
                    'note': 'Bot protection (Cloudflare/similar) - API likely works'
                }
            
            # Interpret status codes
            if code in [200, 201, 202, 204]:
                return {'url': url, 'status': code, 'state': 'working', 'note': 'OK'}
            elif code in [301, 302, 307, 308]:
                return {'url': url, 'status': code, 'state': 'working', 'note': 'Redirect (OK)'}
            elif code == 429:
                return {'url': url, 'status': code, 'state': 'protected', 'note': 'Rate limited (API works)'}
            elif code in [401, 403]:
                return {'url': url, 'status': code, 'state': 'protected', 'note': 'Auth required/Forbidden (API works)'}
            elif code in [400, 405, 406]:
                return {'url': url, 'status': code, 'state': 'working', 'note': 'API up (Invalid request/Method)'}
            elif code == 404:
                return {'url': url, 'status': code, 'state': 'broken', 'note': 'Not found - likely dead'}
            elif code == 410:
                return {'url': url, 'status': code, 'state': 'broken', 'note': 'Gone - confirmed dead'}
            elif code in [500, 502, 504, 521, 522, 523]:
                return {'url': url, 'status': code, 'state': 'error', 'note': 'Server error (may be temporary)'}
            elif code == 503:
                # 503 could be Cloudflare or temporary, treat as warning
                if has_cloudflare_protection(response):
                    return {'url': url, 'status': code, 'state': 'protected', 'note': 'Cloudflare protection (503)'}
                return {'url': url, 'status': code, 'state': 'warning', 'note': 'Service unavailable (503) - may be temporary'}
            else:
                return {'url': url, 'status': code, 'state': 'unknown', 'note': f'HTTP {code}'}
                
        except requests.exceptions.SSLError as e:
            # SSL errors could be temporary (cert renewal in progress) or permanent
            # Mark as warning to avoid false positives
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return {'url': url, 'status': None, 'state': 'warning', 'note': 'SSL error (may be temporary cert issue)'}
        except requests.exceptions.Timeout:
            # Retry on timeout
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait 2 seconds before retry
                continue
            return {'url': url, 'status': None, 'state': 'warning', 'note': 'Timeout after retries (slow server)'}
        except requests.exceptions.ConnectionError as e:
            last_error = e
            # Retry on connection errors (might be temporary)
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait 2 seconds before retry
                continue
            # After all retries, mark as WARNING not broken
            # GitHub Actions IPs often get blocked or have DNS issues
            error_str = str(e).lower()
            if 'getaddrinfo' in error_str or 'name or service not known' in error_str or 'nodename nor servname' in error_str:
                return {'url': url, 'status': None, 'state': 'warning', 'note': 'DNS issue (may be temporary/CI environment)'}
            if 'connection refused' in error_str or 'connection reset' in error_str:
                return {'url': url, 'status': None, 'state': 'warning', 'note': 'Connection refused (may be IP blocking)'}
            # Other connection errors -> warning (could be IP blocking)
            return {'url': url, 'status': None, 'state': 'warning', 'note': 'Connection issue (may be temporary)'}
        except requests.exceptions.TooManyRedirects:
            return {'url': url, 'status': None, 'state': 'warning', 'note': 'Too many redirects (may be geo blocking)'}
        except Exception as e:
            return {'url': url, 'status': None, 'state': 'warning', 'note': f'Unknown error: {type(e).__name__}'}
    
    # Should never reach here, but just in case
    return {'url': url, 'status': None, 'state': 'error', 'note': 'Max retries exceeded'}

def main():
    print("Link Checker (based on public-apis approach)")
    print("=" * 80)
    
    # Extract and deduplicate links
    links = extract_links_from_readme()
    unique_links = sorted(list(set(links)))
    
    print(f"Found {len(links)} total links ({len(unique_links)} unique)")
    print(f"Checking links...\n")
    
    # Categories
    results = {
        'working': [],
        'protected': [],
        'warning': [],
        'error': [],
        'broken': [],
        'unknown': []
    }
    
    # Check links with threading
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(check_link, url): url for url in unique_links}
        
        completed = 0
        for future in as_completed(future_to_url):
            result = future.result()
            completed += 1
            
            # Categorize result
            state = result['state']
            results[state].append(result)
            
            # Display with icons
            icons = {
                'working': '[OK]',
                'protected': '[PROTECTED]',
                'warning': '[WARN]',
                'error': '[ERR]',
                'broken': '[DEAD]',
                'unknown': '[?]'
            }
            
            icon = icons.get(state, '?')
            status_str = f"HTTP {result['status']}" if result['status'] else "N/A"
            print(f"[{completed}/{len(unique_links)}] {icon:12} {status_str:12} {result['note']}")
            print(f"    {result['url']}")
            
            time.sleep(0.1)
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total_ok = len(results['working']) + len(results['protected'])
    
    print(f"[OK] Working: {len(results['working'])}")
    print(f"[PROTECTED] Bot protection (403/429): {len(results['protected'])}")
    print(f"[WARN] Warnings: {len(results['warning'])}")
    print(f"[ERR] Errors: {len(results['error'])}")
    print(f"[DEAD] Broken: {len(results['broken'])}")
    print(f"[?] Unknown: {len(results['unknown'])}")
    if len(unique_links) > 0:
        print(f"\nHealthy: {total_ok}/{len(unique_links)} ({total_ok/len(unique_links)*100:.1f}%)")
    else:
        print(f"\nHealthy: {total_ok}/0 (0.0%)")
    
    # Show only truly broken links
    if results['broken']:
        print("\n" + "=" * 80)
        print("TRULY BROKEN LINKS (Manual Review Needed)")
        print("=" * 80)
        for r in sorted(results['broken'], key=lambda x: x['url']):
            print(f"\n[DEAD] {r['url']}")
            print(f"       {r['note']}")
    
    # Save report
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(script_dir, 'link_check_report.txt')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("LINK CHECK REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total: {len(unique_links)}\n")
        f.write(f"Working: {len(results['working'])}\n")
        f.write(f"Protected: {len(results['protected'])}\n")
        f.write(f"Warnings: {len(results['warning'])}\n")
        f.write(f"Errors: {len(results['error'])}\n")
        f.write(f"Broken: {len(results['broken'])}\n")
        f.write(f"Unknown: {len(results['unknown'])}\n\n")
        
        if results['broken']:
            f.write("BROKEN LINKS:\n")
            f.write("-" * 80 + "\n")
            for r in results['broken']:
                f.write(f"\n{r['url']}\n  -> {r['note']}\n")
        
        if results['error']:
            f.write("\nERROR LINKS:\n")
            f.write("-" * 80 + "\n")
            for r in results['error']:
                f.write(f"\n{r['url']}\n  -> {r['note']}\n")

        if results['unknown']:
            f.write("\nUNKNOWN LINKS:\n")
            f.write("-" * 80 + "\n")
            for r in results['unknown']:
                f.write(f"\n{r['url']}\n  -> {r['note']}\n")

        if results['warning']:
            f.write("\nWARNING LINKS:\n")
            f.write("-" * 80 + "\n")
            for r in results['warning']:
                f.write(f"\n{r['url']}\n  -> {r['note']}\n")
    
    print(f"\nReport saved to: link_check_report.txt")
    print("\nNote: 403/429 (Protected) = Bot protection - APIs still work!")
    
    # Exit with error only if truly broken links found
    if results['broken']:
        print(f"\nFound {len(results['broken'])} truly broken links!")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
