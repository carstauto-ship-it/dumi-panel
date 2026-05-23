#!/usr/bin/env python3
"""Update Panel sitemap with new product URLs"""
import os, glob, re
from datetime import datetime

BASE_DIR = "/tmp/dumi-publish-dumi-panel"
PRODUCTS_DIR = os.path.join(BASE_DIR, "products")

def update_sitemap():
    html_files = sorted(glob.glob(os.path.join(PRODUCTS_DIR, "*.html")))
    today = datetime.now().strftime("%Y-%m-%d")
    
    urls = []
    for f in html_files:
        fname = os.path.basename(f)
        url = f"https://dumi-panel.com/products/{fname}"
        urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")
    
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://dumi-panel.com/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://dumi-panel.com/products.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
{"".join(urls)}
</urlset>"""
    
    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    
    # Update products.html counter
    products_html_path = os.path.join(BASE_DIR, "products.html")
    if os.path.exists(products_html_path):
        with open(products_html_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = re.sub(
            r'Updated: \d{4}-\d{2}-\d{2}',
            f'Updated: {today}',
            content
        )
        new_content = re.sub(
            r'(\d+)</strong> Products',
            f'{len(html_files)}</strong> Products',
            new_content
        )
        with open(products_html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    
    print(f"Sitemap updated: {len(html_files)} product URLs")

if __name__ == "__main__":
    update_sitemap()
