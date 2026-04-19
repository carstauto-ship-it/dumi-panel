#!/usr/bin/env python3
"""Update product pages to use real product images from akupanelcn"""

import os
import re

# Mapping of SVG filenames to real JPG images from akupanelcn
IMAGE_MAP = {
    'pet-panel-detail.svg': 'akupanelcn/pet-panel-1.jpg',
    'pet-panel.svg': 'akupanelcn/pet-panel-1.jpg',
    'wood-slat-panels.svg': 'akupanelcn/wood-slat-1.jpg',
    'wood-slat-panel.svg': 'akupanelcn/wood-slat-1.jpg',
    '3d-panel.svg': 'akupanelcn/3d-panel-1.jpg',
    'acoustic-ceiling.svg': 'akupanelcn/ceiling-1.jpg',
    'fabric-acoustic-panels.svg': 'akupanelcn/fabric-1.jpg',
    'bass-traps.svg': 'akupanelcn/bass-trap-1.jpg',
    'acoustic-doors.svg': 'akupanelcn/acoustic-door-1.jpg',
    'acoustic-screens.svg': 'akupanelcn/acoustic-screen-1.jpg',
    'acoustic-tiles.svg': 'akupanelcn/acoustic-tile-1.jpg',
    'sound-diffusers.svg': 'akupanelcn/diffuser-1.jpg',
    'stretch-fabric-ceiling.svg': 'akupanelcn/stretch-ceiling-1.jpg',
    'perforated-metal-panels.svg': 'akupanelcn/perforated-metal-1.jpg',
    'concertina-foam-panels.svg': 'akupanelcn/concertina-foam-1.jpg',
    'echo-absorbers.svg': 'akupanelcn/echo-absorber-1.jpg',
    'micropore-acoustic-panels.svg': 'akupanelcn/micropore-1.jpg',
    'acoustic-lighting.svg': 'akupanelcn/acoustic-lighting-1.jpg',
    'acoustic-windows.svg': 'akupanelcn/acoustic-window-1.jpg',
}

PRODUCTS_DIR = '/Users/carstauto/.openclaw/workspace/dumi-panel/products'

for filename in os.listdir(PRODUCTS_DIR):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(PRODUCTS_DIR, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace SVG image references with real JPG images
    for svg_name, jpg_path in IMAGE_MAP.items():
        # Match patterns like src="../images/pet-panel-detail.svg"
        pattern = rf'(src=["\'])\.\./images/{re.escape(svg_name)}(["\'])'
        replacement = rf'\1../images/{jpg_path}\2'
        content = re.sub(pattern, replacement, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filename}')

print('Done!')
