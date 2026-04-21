#!/usr/bin/env python3
"""Fix missing canonical tags on existing products"""

import os
import re

PRODUCTS_DIR = "/Users/carstauto/.openclaw/workspace/dumi-panel/products"

missing = [
    "recording-booth-panels.html", "theater-acoustic-panels.html", "perforated-wood-acoustic-panels.html",
    "vehicle-acoustic-treatment.html", "recording-studio-doors.html", "gymnasium-acoustic-baffles.html",
    "acoustic-window-panels.html", "hospital-acoustic-panels.html", "industrial-pipe-insulation.html",
    "church-acoustic-panels.html", "auditorium-acoustic-panels.html", "studio-diffuser-panels.html",
    "resilient-channel-systems.html", "recording-studio-doors.html", "pipe-noise-covers.html",
    "outdoor-noise-barriers.html", "acoustical-vanity-mirrors.html", "artistic-acoustic-panels.html",
    "cinema-acoustic-panels.html", "office-acoustic-ceiling-tiles.html", "acoustic-wall-coverings.html"
]

def fix_canonical(file_path, file_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    base_url = "https://dumi-panel.com"
    canonical = f"{base_url}/products/{file_name}"
    
    # Extract current title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else file_name.replace('.html', '').replace('-', ' ').title()
    
    # Extract current description
    desc_match = re.search(r'<meta name="description" content="([^"]*)"', content)
    description = desc_match.group(1) if desc_match else ""
    
    # Add canonical after keywords meta
    canonical_tag = f'<link rel="canonical" href="{canonical}">'
    
    if 'rel="canonical"' not in content:
        # Try to insert after description
        content = re.sub(
            r'(<meta name="description" content="[^"]*">)',
            r'\1\n    ' + canonical_tag,
            content
        )
    
    # Add OG tags
    og_tags = f'''    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{base_url}/images/{file_name.replace('.html','')}.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
'''
    
    if '<meta property="og:title"' not in content:
        content = re.sub(
            r'(<link rel="canonical"[^>]*>)',
            r'\1\n' + og_tags,
            content
        )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {file_name}: Fixed")

def main():
    print("Adding canonical + OG tags to existing products...\n")
    for f in sorted(set(missing)):
        fp = os.path.join(PRODUCTS_DIR, f)
        if os.path.exists(fp):
            fix_canonical(fp, f)
        else:
            print(f"  ✗ {f}: Not found")
    print(f"\nDone: {len(missing)} products fixed")

if __name__ == "__main__":
    main()
