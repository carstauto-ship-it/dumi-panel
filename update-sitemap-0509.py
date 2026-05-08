#!/usr/bin/env python3
"""Update sitemap.xml with 15 new products"""

import os
from datetime import datetime

PRODUCTS_DIR = "/Users/carstauto/.openclaw/workspace/dumi-panel/products"
SITEMAP_PATH = "/Users/carstauto/.openclaw/workspace/dumi-panel/sitemap.xml"
BASE_URL = "https://dumi-panel.com"
TODAY = "2026-05-09"

new_products = [
    "studio-acoustic-starter-kit",
    "pro-audio-waveform-panels",
    "broadband-acoustic-absorbers",
    "ceiling-suspended-acoustic-panels",
    "marine-floating-floor-acoustic",
    "transparent-acoustic-screen",
    "hvac-duct-acoustic-liner",
    "studio-door-acoustic-seal",
    "acoustical-rack-mount-panel",
    "outdoor-speaker-enclosure-acoustic",
    "acoustic-panel-adhesive-spray",
    "portable-acoustic-divider-wall",
    "acoustical-vent-covers",
    "stairwell-acoustic-treatment",
    "measurement-microphone-booth"
]

# Read existing sitemap
with open(SITEMAP_PATH, 'r') as f:
    content = f.read()

# Add new URLs before closing </urlset>
new_urls = ""
for slug in new_products:
    new_urls += f"  <url><loc>{BASE_URL}/products/{slug}.html</loc><lastmod>{TODAY}</lastmod></url>\n"

# Insert before </urlset>
updated_sitemap = content.replace("</urlset>", new_urls + "</urlset>")

# Update all lastmod dates to today
updated_sitemap = updated_sitemap.replace("lastmod>2026-05-07", f"lastmod>{TODAY}")

# Write updated sitemap
with open(SITEMAP_PATH, 'w') as f:
    f.write(updated_sitemap)

# Count URLs
url_count = updated_sitemap.count("<url>")

print(f"Sitemap updated: {url_count} URLs")
print(f"Added {len(new_products)} new products with lastmod {TODAY}")