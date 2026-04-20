#!/usr/bin/env python3
"""Update sitemap with all current products"""
import os
from datetime import datetime

PRODUCTS_DIR = '/Users/carstauto/.openclaw/workspace/dumi-panel/products'
SITEMAP_PATH = '/Users/carstauto/.openclaw/workspace/dumi-panel/sitemap.xml'

today = datetime.now().strftime('%Y-%m-%d')

# Get all product HTML files
products = sorted([f for f in os.listdir(PRODUCTS_DIR) if f.endswith('.html')])

print(f"Found {len(products)} product pages")

# Build sitemap
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

# Homepage
lines.append('    <url>')
lines.append('        <loc>https://dumi-panel.com/</loc>')
lines.append(f'        <lastmod>{today}</lastmod>')
lines.append('        <changefreq>weekly</changefreq>')
lines.append('        <priority>1.0</priority>')
lines.append('    </url>')

# Products listing
lines.append('    <url>')
lines.append('        <loc>https://dumi-panel.com/products.html</loc>')
lines.append(f'        <lastmod>{today}</lastmod>')
lines.append('        <changefreq>weekly</changefreq>')
lines.append('        <priority>0.9</priority>')
lines.append('    </url>')

# Individual products
for product in products:
    slug = product.replace('.html', '')
    priority = '0.8' if 'acoustic' in slug or 'sound' in slug else '0.7'
    lines.append('    <url>')
    lines.append(f'        <loc>https://dumi-panel.com/products/{product}</loc>')
    lines.append(f'        <lastmod>{today}</lastmod>')
    lines.append('        <changefreq>monthly</changefreq>')
    lines.append(f'        <priority>{priority}</priority>')
    lines.append('    </url>')

lines.append('</urlset>')

content = '\n'.join(lines)
with open(SITEMAP_PATH, 'w') as f:
    f.write(content)

print(f"Updated sitemap with {len(products)} products at {SITEMAP_PATH}")
print(f"Total URL entries: {len(products) + 2}")