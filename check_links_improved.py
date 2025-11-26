import re
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def extract_links_from_readme(file_path):
    """Extract all API links from README.md"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all markdown links [text](url)
    pattern = r'\[Link\]\((https?://[^\)]+)\)'
    links = re.findall(pattern, content)
    
    return links

def check_link(url, timeout=15, retries=2):
    """Check if a link is accessible with better handling of bot protection"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    for attempt in range(retries):
        try:
            # Try GET directly (some sites don't support HEAD)
            response = requests.get(url, timeout=timeout, headers=headers, allow_redirects=True)
            
            # Consider these as "working" (even if bot protected)
            if response.status_code in [200, 201, 202, 301, 302, 307, 308, 403, 429]:
                return {
                    'url': url,
                    'status_code': response.status_code,
                    'error': None,
                    'is_broken': False,
                    'note': '403/429 = Bot protection (OK)' if response.status_code in [403, 429] else ''
                }
            
            # Only mark as broken if truly dead (404, 410, 5xx)
            if response.status_code >= 400:
                return {
                    'url': url,
                    'status_code': response.status_code,
                    'error': None,
                    'is_broken': response.status_code in [404, 410, 500, 502, 503],
                    'note': 'Likely dead' if response.status_code in [404, 410] else 'Server error (may be temporary)'
                }
                
        except requests.exceptions.Timeout:
            if attempt < retries - 1:
                time.sleep(2)  # Wait before retry
                continue
            return {
                'url': url,
                'status_code': None,
                'error': 'Timeout',
                'is_broken': False,  # Don't mark as broken - might just be slow
                'note': 'Slow response (not necessarily dead)'
            }
        except requests.exceptions.ConnectionError:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            return {
                'url': url,
                'status_code': None,
                'error': 'Connection Error',
                'is_broken': True,  # This usually means dead
                'note': 'Likely dead service'
            }
        except Exception as e:
            return {
                'url': url,
                'status_code': None,
                'error': str(e),
                'is_broken': False,
                'note': 'Unknown error'
            }
    
    return {
        'url': url,
        'status_code': None,
        'error': 'Max retries exceeded',
        'is_broken': False,
        'note': 'Could not verify'
    }

def main():
    print("🔍 Improved Link Checker (Fewer False Positives)")
    print("=" * 80)
    
    # Extract links
    links = extract_links_from_readme('README.md')
    unique_links = list(set(links))
    
    print(f"📊 Found {len(links)} total links ({len(unique_links)} unique)")
    print(f"⏳ Starting link checks with improved detection...\n")
    
    broken_links = []
    working_links = []
    protected_links = []
    
    # Check links concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:  # Reduced workers to be nice
        future_to_url = {executor.submit(check_link, url): url for url in unique_links}
        
        completed = 0
        for future in as_completed(future_to_url):
            result = future.result()
            completed += 1
            
            if result['is_broken']:
                broken_links.append(result)
                status = f"❌ BROKEN"
            elif result['status_code'] in [403, 429]:
                protected_links.append(result)
                status = f"⚠️  PROTECTED (OK)"
            else:
                working_links.append(result)
                status = f"✅ OK"
            
            if result['status_code']:
                status += f" (HTTP {result['status_code']})"
            elif result['error']:
                status += f" ({result['error']})"
            
            if result['note']:
                status += f" - {result['note']}"
            
            print(f"[{completed}/{len(unique_links)}] {status}")
            print(f"    {result['url']}")
            
            time.sleep(0.2)  # Be nice to servers
    
    # Print summary
    print("\n" + "=" * 80)
    print("📈 SUMMARY")
    print("=" * 80)
    print(f"✅ Working links: {len(working_links)}")
    print(f"⚠️  Protected links (bot protection, still OK): {len(protected_links)}")
    print(f"❌ Truly broken links: {len(broken_links)}")
    total_ok = len(working_links) + len(protected_links)
    print(f"📊 Success rate: {total_ok/len(unique_links)*100:.1f}% ({total_ok}/{len(unique_links)})")
    
    if broken_links:
        print("\n" + "=" * 80)
        print("💔 TRULY BROKEN LINKS (Manual review recommended)")
        print("=" * 80)
        for link in sorted(broken_links, key=lambda x: x['url']):
            error_msg = link['error'] if link['error'] else f"HTTP {link['status_code']}"
            print(f"\n❌ {link['url']}")
            print(f"   Error: {error_msg}")
            print(f"   Note: {link['note']}")
    
    # Save results
    with open('improved_check_report.txt', 'w', encoding='utf-8') as f:
        f.write("IMPROVED LINK CHECK REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total: {len(unique_links)}\n")
        f.write(f"Working: {len(working_links)}\n")
        f.write(f"Protected (403/429): {len(protected_links)}\n")
        f.write(f"Broken: {len(broken_links)}\n\n")
        
        if broken_links:
            f.write("TRULY BROKEN (manual review needed):\n")
            f.write("-" * 80 + "\n")
            for link in sorted(broken_links, key=lambda x: x['url']):
                f.write(f"\n{link['url']}\n")
                error_msg = link['error'] if link['error'] else f"HTTP {link['status_code']}"
                f.write(f"  Error: {error_msg}\n")
                f.write(f"  Note: {link['note']}\n")
    
    print(f"\n📝 Report saved to: improved_check_report.txt")
    print("\n💡 NOTE: 403/429 errors are NORMAL and mean APIs have bot protection.")
    print("   These should NOT be removed from the list!")

if __name__ == "__main__":
    main()
