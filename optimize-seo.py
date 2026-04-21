#!/usr/bin/env python3
"""Optimize SEO for new product pages"""

import os
import re

PRODUCTS_DIR = "/Users/carstauto/.openclaw/workspace/dumi-panel/products"

# Products that need SEO optimization (from add-new-products.py)
new_products = [
    {
        "file": "fabric-acoustic-panels.html",
        "title": "Fabric Wrapped Acoustic Panels | DUMI Soundproofing Solutions",
        "description": "Premium fabric-wrapped acoustic panels with high-density glass wool core. NRC 0.80-0.95, fire-rated A2. Perfect for recording studios, offices, auditoriums. Factory direct pricing.",
        "keywords": "fabric acoustic panels, fabric wrapped panels, acoustic fabric panels, soundproofing panels, office acoustic panels, studio panels, DUMI",
    },
    {
        "file": "perforated-metal-panels.html",
        "title": "Perforated Metal Acoustic Panels | DUMI Industrial Soundproofing",
        "description": "Durable perforated metal acoustic panels with acoustic fleece backing. A1 fire rating, NRC 0.70-0.90. Ideal for shopping malls, transit stations, industrial buildings. Custom RAL colors available.",
        "keywords": "perforated metal panels, metal acoustic panels, industrial acoustic panels, soundproofing panels, metal ceiling panels, DUMI",
    },
    {
        "file": "micropore-acoustic-panels.html",
        "title": "Micropore Acoustic Panels | DUMI Ultra-Thin Soundproofing",
        "description": "Ultra-thin microperforated acoustic panels with innovative pore technology. Space-saving design with superior sound absorption. Perfect for restaurants, libraries, and space-constrained areas.",
        "keywords": "micropore acoustic panels, microperforated panels, thin acoustic panels, space-saving soundproofing, restaurant acoustic panels, DUMI",
    },
    {
        "file": "echo-absorbers.html",
        "title": "Echo Absorbers | DUMI Professional Sound Absorption Solutions",
        "description": "High-performance echo absorbers designed for large spaces. Effective across full frequency range (125Hz-4000Hz). NRC > 0.85. Perfect for gymnasiums, warehouses, and event spaces.",
        "keywords": "echo absorbers, sound absorbers, acoustic absorbers, echo reduction, gymnasium acoustic panels, warehouse soundproofing, DUMI",
    },
    {
        "file": "sound-diffusers.html",
        "title": "Sound Diffusers | DUMI Professional Acoustic Diffusion Panels",
        "description": "Premium sound diffusers for balanced acoustic environments. Evenly distributes sound energy across frequencies. Essential for recording studios, concert halls, and home theaters.",
        "keywords": "sound diffusers, acoustic diffusers, diffusion panels, studio diffusers, acoustic treatment, home theater diffusers, DUMI",
    },
    {
        "file": "concertina-foam-panels.html",
        "title": "Concertina Foam Panels | DUMI High-Density Soundproofing",
        "description": "High-density concertina foam acoustic panels with unique pleated design for maximum sound absorption coverage. NRC > 0.90. Ideal for recording studios, podcast booths, and music rooms.",
        "keywords": "concertina foam panels, acoustic foam panels, studio foam, soundproofing foam, recording studio panels, music room panels, DUMI",
    },
    {
        "file": "stretch-fabric-ceiling.html",
        "title": "Stretch Fabric Ceiling Systems | DUMI Acoustic Ceiling Solutions",
        "description": "Elegant stretch fabric ceiling systems with integrated acoustic padding. Seamless appearance with excellent sound absorption. Perfect for offices, hotels, restaurants, and healthcare facilities.",
        "keywords": "stretch fabric ceiling, acoustic ceiling, fabric ceiling systems, suspended ceiling, office acoustic ceiling, hotel acoustic ceiling, DUMI",
    },
]

def optimize_product(file_path, product):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    base_url = "https://dumi-panel.com"
    canonical = f"{base_url}/products/{product['file']}"
    
    # Check if canonical already exists
    if 'rel="canonical"' in content:
        print(f"  {product['file']}: Already has canonical, skipping")
        return False
    
    # Fix title
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{product["title"]}</title>',
        content
    )
    
    # Fix description
    content = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{product["description"]}">',
        content
    )
    
    # Fix keywords
    content = re.sub(
        r'<meta name="keywords" content="[^"]*">',
        f'<meta name="keywords" content="{product["keywords"]}">',
        content
    )
    
    # Add canonical after description
    content = re.sub(
        r'(<meta name="keywords"[^>]*>)',
        f'<link rel="canonical" href="{canonical}">\n    \\1',
        content
    )
    
    # Add OG tags after canonical
    og_tags = f'''    <meta property="og:title" content="{product["title"]}">
    <meta property="og:description" content="{product["description"]}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{base_url}/images/{product["file"].replace(".html","")}.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{product["title"]}">
    <meta name="twitter:description" content="{product["description"]}">
'''
    content = re.sub(
        r'(<link rel="canonical"[^>]*>)',
        r'\1\n' + og_tags,
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {product['file']}: SEO optimized")
    return True

def main():
    print("Optimizing SEO for new product pages...\n")
    count = 0
    for product in new_products:
        file_path = os.path.join(PRODUCTS_DIR, product["file"])
        if os.path.exists(file_path):
            if optimize_product(file_path, product):
                count += 1
        else:
            print(f"  ✗ {product['file']}: File not found")
    
    print(f"\nTotal optimized: {count}/{len(new_products)}")
    
    # Also optimize existing products that might be missing canonical
    print("\nChecking existing products for missing canonical...")
    missing_canonical = []
    for f in os.listdir(PRODUCTS_DIR):
        if f.endswith('.html'):
            fp = os.path.join(PRODUCTS_DIR, f)
            with open(fp) as fh:
                c = fh.read()
            if 'rel="canonical"' not in c:
                missing_canonical.append(f)
    
    print(f"Products missing canonical: {len(missing_canonical)}")
    if missing_canonical:
        print("Files:", missing_canonical[:10])

if __name__ == "__main__":
    main()
