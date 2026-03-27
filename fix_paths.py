#!/usr/bin/env python3
"""
Fix asset paths in all HTML files so they work on GitHub Pages at:
https://harbortech7.github.io/skytab-espanol/

All absolute paths like /_next/... /icons/... /fonts/... /images/...
need to become /skytab-espanol/_next/... etc.
"""

import os
import re

BASE_DIR = "/home/mark/Desktop/skytabmx/www.skytab.com"
REPO_PREFIX = "/skytab-espanol"

# Patterns that need the repo prefix added
LOCAL_PATH_PATTERNS = [
    # src="/_next/..."  href="/_next/..."
    (r'(src|href)="(/_next/[^"]*)"', r'\1="' + REPO_PREFIX + r'\2"'),
    # src="/icons/..."
    (r'(src|href)="(/icons/[^"]*)"', r'\1="' + REPO_PREFIX + r'\2"'),
    # src="/fonts/..."
    (r'(src|href)="(/fonts/[^"]*)"', r'\1="' + REPO_PREFIX + r'\2"'),
    # src="/images/..."
    (r'(src|href)="(/images/[^"]*)"', r'\1="' + REPO_PREFIX + r'\2"'),
]

# Internal page links like href="/contact" href="/features/..." etc
# These need to become /skytab-espanol/contact etc
# But NOT external links (http/https) and NOT already prefixed
LINK_PATTERN = r'href="(/(?!skytab-espanol)(?!http)(?!#)[^"]*)"'
LINK_REPLACEMENT = r'href="' + REPO_PREFIX + r'\1"'

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # Fix asset paths
    for pattern, replacement in LOCAL_PATH_PATTERNS:
        content = re.sub(pattern, replacement, content)

    # Fix internal page links (href="/something")
    content = re.sub(LINK_PATTERN, LINK_REPLACEMENT, content)

    # Fix assetPrefix in Next.js inline scripts
    # Next.js sets __NEXT_DATA__ with assetPrefix
    content = content.replace('"assetPrefix":""', '"assetPrefix":"/skytab-espanol"')
    content = content.replace('"assetPrefix": ""', '"assetPrefix": "/skytab-espanol"')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))

    print(f"Found {len(html_files)} HTML files")
    fixed = 0
    for fp in html_files:
        if fix_file(fp):
            fixed += 1
            print(f"Fixed: {fp.replace(BASE_DIR, '')}")

    print(f"\nDone. Fixed {fixed}/{len(html_files)} files.")

if __name__ == "__main__":
    main()
