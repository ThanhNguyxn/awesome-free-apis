"""
Improved Link Checker for awesome-free-apis
Handles bot protection, retries, and reduces false positives
"""

import re
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session():
    """Create a session with retry strategy"""
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def extract_links_from_readme(file_path='../README.md'):
    """Extract all API links from README.md"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'\[Link\]\((https?://[^\)]+)\)'
    links = re.findall(pattern, content)
    return links

def check_link(url, session, timeout=20):
    """
    Check if a link is accessible
    Returns: dict with status info
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0',
    }
    
    try:
        # Try GET request (more compatible than HEAD)
        response = session.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        status = response.status_code
        
        # Interpret status codes
        if status in [200, 201, 202, 204]:
            return {'url': url, 'status': status, 'state': 'working', 'note': 'OK'}
        elif status in [301, 302, 307, 308]:
            return {'url': url, 'status': status, 'state': 'working', 'note': 'Redirect (OK)'}
        elif status == 403:
            return {'url': url, 'status': status, 'state': 'protected', 'note': 'Bot protection (API likely works)'}
        elif status == 429:
            return {'url': url, 'status': status, 'state': 'protected', 'note': 'Rate limited (API works)'}
        elif status == 404:
            return {'url': url, 'status': status, 'state': 'broken', 'note': 'Not found - likely dead'}
        elif status == 410:
            return {'url': url, 'status': status, 'state': 'broken', 'note': 'Gone - confirmed dead'}
        elif status in [500, 502, 503, 504]:
            return {'url': url, 'status': status, 'state': 'error', 'note': 'Server error (may be temporary)'}
        else:
            return {'url': url, 'status': status, 'state': 'unknown', 'note': f'HTTP {status}'}
            
    except requests.exceptions.SSLError:
        return {'url': url, 'status': None, 'state': 'warning', 'note': 'SSL error (cert issue, not necessarily dead)'}
    except requests.exceptions.Timeout:
        return {'url': url, 'status': None, 'state': 'warning', 'note': 'Timeout (slow server, not necessarily dead)'}
    except requests.exceptions.ConnectionError as e:
        if 'getaddrinfo failed' in str(e) or 'Name or service not known' in str(e):
            return {'url': url, 'status': None, 'state': 'broken', 'note': 'DNS failed - domain dead'}
        return {'url': url, 'status': None, 'state': 'broken', 'note': 'Connection refused - likely dead'}
    except requests.exceptions.TooManyRedirects:
        return {'url': url, 'status': None, 'state': 'error', 'note': 'Too many redirects (misconfigured)'}
    except Exception as e:
        return {'url': url, 'status': None, 'state': 'error', 'note': f'Error: {type(e).__name__}'}

def main():
    print("🔍 Link Checker for awesome-free-apis")
    print("=" * 80)
    
    # Extract and deduplicate links
    links = extract_links_from_readme()
    unique_links = sorted(list(set(links)))
    
    print(f"📊 Found {len(links)} total links ({len(unique_links)} unique)")
    print(f"⏳ Checking links...\n")
    
    # Categories
    results = {
        'working': [],
        'protected': [],
        'warning': [],
        'error': [],
        'broken': [],
        'unknown': []
    }
    
    # Create session with retry logic
    session = create_session()
    
    # Check links with threading
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_link, url, session): url for url in unique_links}
        
        completed = 0
        for future in as_completed(future_to_url):
            result = future.result()
            completed += 1
            
            # Categorize result
            state = result['state']
            results[state].append(result)
            
            # Display
            icons = {
                'working': '✅',
                'protected': '🛡️',
                'warning': '⚠️',
                'error': '🔶',
                'broken': '❌',
                'unknown': '❓'
            }
            
            icon = icons.get(state, '?')
            status_str = f"HTTP {result['status']}" if result['status'] else "N/A"
            print(f"[{completed}/{len(unique_links)}] {icon} {status_str:12} {result['note']}")
            print(f"    {result['url']}")
            
            time.sleep(0.1)  # Be respectful
    
    session.close()
    
    # Summary
    print("\n" + "=" * 80)
    print("📈 SUMMARY")
    print("=" * 80)
    
    total_ok = len(results['working']) + len(results['protected'])
    total_issues = len(results['broken'])
    
    print(f"✅ Working: {len(results['working'])}")
    print(f"🛡️  Protected (403/429): {len(results['protected'])}")
    print(f"⚠️  Warnings: {len(results['warning'])}")
    print(f"🔶 Errors: {len(results['error'])}")
    print(f"❌ Broken: {len(results['broken'])}")
    print(f"❓ Unknown: {len(results['unknown'])}")
    print(f"\n📊 Healthy: {total_ok}/{len(unique_links)} ({total_ok/len(unique_links)*100:.1f}%)")
    
    # Show only truly broken links
    if results['broken']:
        print("\n" + "=" * 80)
        print("💔 TRULY BROKEN LINKS (Manual Review Needed)")
        print("=" * 80)
        for r in sorted(results['broken'], key=lambda x: x['url']):
            print(f"\n❌ {r['url']}")
            print(f"   {r['note']}")
    
    # Save report
    with open('link_check_report.txt', 'w', encoding='utf-8') as f:
        f.write("LINK CHECK REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total: {len(unique_links)}\n")
        f.write(f"Working: {len(results['working'])}\n")
        f.write(f"Protected: {len(results['protected'])}\n")
        f.write(f"Warnings: {len(results['warning'])}\n")
        f.write(f"Errors: {len(results['error'])}\n")
        f.write(f"Broken: {len(results['broken'])}\n\n")
        
        if results['broken']:
            f.write("BROKEN LINKS:\n")
            f.write("-" * 80 + "\n")
            for r in results['broken']:
                f.write(f"\n{r['url']}\n  → {r['note']}\n")
    
    print(f"\n📝 Report saved to: link_check_report.txt")
    print("\n💡 Note: 403/429 (Protected) means bot protection - APIs still work!")

if __name__ == "__main__":
    main()
