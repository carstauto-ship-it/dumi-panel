#!/usr/bin/env python3
"""
Batch Generate 15 Acoustic Panel Products for dumi-panel.com
Date: 2026-05-09
"""

import os
import re

PRODUCTS_DIR = "/Users/carstauto/.openclaw/workspace/dumi-panel/products"
BASE_URL = "https://dumi-panel.com"

# 15 New Acoustic Panel Products
products = [
    {
        "id": "studio-acoustic-starter-kit",
        "name": "Studio Acoustic Treatment Starter Kit",
        "title": "Studio Acoustic Treatment Starter Kit | Complete Soundproofing Set | DUMI",
        "description": "Complete acoustic treatment starter kit for home studios and podcast setups. Includes 12 bass traps, 24 wall panels, and installation hardware. Everything you need for professional studio acoustics.",
        "keywords": "acoustic treatment kit, studio starter kit, soundproofing kit, bass trap set, wall panel kit, studio acoustic package",
        "h2_features": "12 Bass Traps | 24 Wall Panels | Mounting Hardware Included | NRC 0.90+",
        "price": "From $399/kit",
        "specs": "Full Kit: 12 Corner Bass Traps + 24 Wall Panels + Hardware",
        "applications": "Home Studios | Podcast Rooms | Music Practice | Gaming setups"
    },
    {
        "id": "pro-audio-waveform-panels",
        "name": "Audio Waveform Pattern Acoustic Panels",
        "title": "Audio Waveform Pattern Acoustic Panels | Music Visual Design | DUMI",
        "description": "Unique audio waveform pattern design acoustic panels. Visual appeal meets acoustic performance. Perfect for modern recording studios and music production spaces.",
        "keywords": "waveform panels, audio pattern acoustic, music studio panels, visual acoustic design, soundwave art panels",
        "h2_features": "Audio Waveform Pattern | Modern Design | NRC 0.85+ | Custom Colors",
        "price": "From $75/piece",
        "specs": "24\"x48\"x2\" | 48\"x48\"x2\" | Multiple waveform patterns",
        "applications": "Music Studios | Recording Rooms | Audio Labs | Home theaters"
    },
    {
        "id": "broadband-acoustic-absorbers",
        "name": "Broadband Acoustic Absorbers",
        "title": "Broadband Acoustic Absorbers | Full-Range Sound Control | DUMI",
        "description": "Broadband acoustic absorbers designed for full-range frequency control. Effective from 50Hz to 20kHz. Professional-grade panels for critical listening environments.",
        "keywords": "broadband absorber, full-range acoustic, low frequency absorber, professional acoustic panels, studio broadband",
        "h2_features": "Full-Range Absorption | 50Hz-20kHz | Thick Profile | Professional Grade",
        "price": "From $85/piece",
        "specs": "24\"x24\"x6\" | 24\"x48\"x6\" | 48\"x48\"x6\"",
        "applications": "Recording Studios | Mastering Rooms | Broadcast Studios | Audiophile Rooms"
    },
    {
        "id": "ceiling-suspended-acoustic-panels",
        "name": "Suspended Ceiling Acoustic Panels",
        "title": "Suspended Ceiling Acoustic Panels | Drop Ceiling Sound Absorption | DUMI",
        "description": "Suspended ceiling acoustic panels designed for commercial drop ceiling systems. Easy integration with standard ceiling grids. Superior noise reduction for office environments.",
        "keywords": "suspended ceiling panels, drop ceiling acoustic, ceiling grid panels, office acoustic ceiling, commercial sound panels",
        "h2_features": "Drop Ceiling Compatible | Grid Mount System | NRC 0.80+ | Lightweight Design",
        "price": "From $55/piece",
        "specs": "24\"x24\"x1\" | 24\"x48\"x1\" | Standard grid sizes",
        "applications": "Office Buildings | Conference Rooms | Call Centers | Schools"
    },
    {
        "id": "marine-floating-floor-acoustic",
        "name": "Marine Floating Floor Acoustic System",
        "title": "Marine Floating Floor Acoustic | Boat Soundproofing | DUMI",
        "description": "Marine-grade floating floor acoustic system for boats and yachts. Vibration dampening and sound isolation in one complete package. Saltwater resistant materials.",
        "keywords": "marine acoustic, boat soundproofing, yacht flooring, marine floating floor, boat insulation, vessel acoustic",
        "h2_features": "Marine Grade | Saltwater Resistant | Floating Floor Design | Vibration Dampening",
        "price": "From $180/sqft",
        "specs": "Per square foot | Custom boat layouts | Complete system",
        "applications": "Yachts | Sailboats | Commercial Vessels | Houseboats"
    },
    {
        "id": "transparent-acoustic-screen",
        "name": "Transparent Acoustic Privacy Screen",
        "title": "Transparent Acoustic Privacy Screen | See-Through Sound Barrier | DUMI",
        "description": "Transparent acoustic screens for visual visibility while blocking sound. Perfect for retail spaces, reception areas, and dividers where sight lines matter.",
        "keywords": "transparent acoustic screen, privacy barrier, see-through sound panel, transparent sound barrier, acoustic partition",
        "h2_features": "Transparent Design | Sound Blocking | Portable | Modular Setup",
        "price": "From $250/screen",
        "specs": "48\"x72\" | 48\"x96\" | Clear acrylic with acoustic layer",
        "applications": "Retail Stores | Reception Desks | Meeting Rooms | Open Plan Offices"
    },
    {
        "id": "hvac-duct-acoustic-liner",
        "name": "HVAC Duct Acoustic Liner",
        "title": "HVAC Duct Acoustic Liner | Duct Sound Attenuation | DUMI",
        "description": "Acoustic liner for HVAC ducts to reduce mechanical noise transmission. Flexible glass wool lining with protective facing. Essential for quiet building climate control.",
        "keywords": "HVAC acoustic liner, duct sound attenuation, HVAC noise reduction, duct insulation, mechanical noise control",
        "h2_features": "Flexible Liner | Glass Wool Core | Foil Faced | Fire Rated",
        "price": "From $25/linear ft",
        "specs": "Standard duct sizes | Custom lengths | Foil facing",
        "applications": "Commercial Buildings | Hotels | Hospitals | Office HVAC Systems"
    },
    {
        "id": "studio-door-acoustic-seal",
        "name": "Acoustic Door Seal Kit",
        "title": "Acoustic Door Seal Kit | Soundproof Door Weatherstripping | DUMI",
        "description": "Complete acoustic door seal kit for studio doors and soundproof rooms. Includes threshold seal, perimeter seals, and door sweep. Achieve STC 50+ rating on standard doors.",
        "keywords": "acoustic door seal, soundproof door kit, door weatherstripping, sound blocking door, STC rating door",
        "h2_features": "Complete Kit | Threshold Included | STC 50+ Rating | DIY Installation",
        "price": "From $89/kit",
        "specs": "Standard 36\" door kit | Adjustable threshold | All hardware included",
        "applications": "Recording Studios | Home Studios | Podcast Booths | Rehearsal Rooms"
    },
    {
        "id": "acoustical-rack-mount-panel",
        "name": "Rack Mount Acoustic Panels",
        "title": "Rack Mount Acoustic Panels | Studio Equipment Rack Soundproofing | DUMI",
        "description": "Rack mount acoustic panels designed to line studio equipment racks and cabinets. Reduce resonance and vibration from power amplifiers and equipment cooling fans.",
        "keywords": "rack mount acoustic, studio rack panels, equipment soundproofing, rack isolation, amplifier resonance control",
        "h2_features": "Rack Mount Design | 2U Size | Sound Absorption | Vibration Damping",
        "price": "From $45/panel",
        "specs": "Standard 2U rack size | 19\" width | 2\" depth",
        "applications": "Recording Studios | Broadcast Equipment | DJ Gear | Home Studios"
    },
    {
        "id": "outdoor-speaker-enclosure-acoustic",
        "name": "Outdoor Speaker Acoustic Enclosure",
        "title": "Outdoor Speaker Acoustic Enclosure | Weatherproof Speaker Box | DUMI",
        "description": "Weatherproof acoustic enclosure for outdoor speakers. Protects speakers while maintaining sound quality. UV-resistant and waterproof design for year-round outdoor use.",
        "keywords": "outdoor speaker enclosure, weatherproof speaker box, outdoor acoustic box, patio speaker housing, landscape speaker enclosure",
        "h2_features": "Weatherproof Design | UV Resistant | Acoustically Transparent Grille | Outdoor Rated",
        "price": "From $165/enclosure",
        "specs": "Single speaker enclosure | Dual speaker option | Custom sizes",
        "applications": "Patios | Gardens | Pool Areas | Outdoor Venues | Resorts"
    },
    {
        "id": "acoustic-panel-adhesive-spray",
        "name": "Acoustic Panel Adhesive Spray",
        "title": "Acoustic Panel Adhesive Spray | Permanent Mounting Solution | DUMI",
        "description": "Professional-grade adhesive spray specifically formulated for acoustic panel installation. Strong initial tack and permanent bond. Low VOC and quick drying formula.",
        "keywords": "acoustic adhesive spray, panel mounting adhesive, permanent spray adhesive, acoustic panel glue, sound panel adhesive",
        "h2_features": "Strong Initial Tack | Permanent Bond | Low VOC | Quick Drying",
        "price": "From $28/can",
        "specs": "17oz can | Coverage: 40-60 sq ft per can | Permanent bond",
        "applications": "Wall Panel Installation | Ceiling Panels | DIY Acoustic Projects"
    },
    {
        "id": "portable-acoustic-divider-wall",
        "name": "Portable Acoustic Divider Wall",
        "title": "Portable Acoustic Divider Wall | Mobile Sound Barrier | DUMI",
        "description": "Portable acoustic divider walls on casters for flexible space division. Create temporary recording spaces or noise isolation zones. Easy to move and store when not in use.",
        "keywords": "portable acoustic divider, mobile sound wall, movable acoustic partition, temporary sound barrier, rolling acoustic panel",
        "h2_features": "Portable Design | Caster Wheels | 6ft Height | Sound Blocking Core",
        "price": "From $320/wall",
        "specs": "6ft H x 4ft W | Rolling casters | Stackable design",
        "applications": "Event Spaces | Temporary Studios | Trade Shows | Office Reconfiguration"
    },
    {
        "id": "acoustical-vent-covers",
        "name": "Acoustic Vent Covers",
        "title": "Acoustic Vent Covers | Vent Sound Blockers | DUMI",
        "description": "Acoustic vent covers that block sound transmission through HVAC vents and grilles. Magnetic attachment for easy installation and removal. Maintains airflow while blocking noise.",
        "keywords": "acoustic vent cover, vent sound blocker, HVAC acoustic cover, vent noise reduction, grille acoustic cover",
        "h2_features": "Magnetic Attachment | Airflow Maintained | Sound Blocking | Removable Design",
        "price": "From $35/cover",
        "specs": "6\"x10\" | 8\"x12\" | 12\"x12\" | Custom sizes",
        "applications": "Recording Studios | Home Theaters | Bedroom Soundproofing | Office Privacy"
    },
    {
        "id": "stairwell-acoustic-treatment",
        "name": "Stairwell Acoustic Panels",
        "title": "Stairwell Acoustic Panels | Echo Reduction for Stairs | DUMI",
        "description": "Acoustic panels designed for stairwell installations. Reduces echo and reverberation in multi-level spaces. Architectural brackets for angled mounting on stair walls.",
        "keywords": "stairwell acoustic panels, stair echo reduction, stairwell soundproofing, multi-level acoustic, staircase acoustic treatment",
        "h2_features": "Angled Mounting System | Echo Reduction | Architectural Design | NRC 0.85+",
        "price": "From $65/piece",
        "specs": "24\"x24\"x2\" | Angled brackets included | Multiple finishes",
        "applications": "Commercial Stairwells | Hotel Lobbies | Office Atriums | Public Buildings"
    },
    {
        "id": "measurement-microphone-booth",
        "name": "Measurement Microphone Booth",
        "title": "Acoustic Measurement Microphone Booth | Studio Calibration Setup | DUMI",
        "description": "Portable acoustic booth for measurement microphones used in room calibration and acoustic testing. Ensures accurate readings by isolating microphone from room reflections.",
        "keywords": "measurement microphone booth, acoustic calibration booth, mic isolation box, room calibration setup, acoustic testing booth",
        "h2_features": "Microphone Isolation | Reflection-Free Design | Portable | Acoustic Foam Lined",
        "price": "From $189/booth",
        "specs": "Fits standard measurement mics | Portable design | Acoustic foam lined",
        "applications": "Studio Calibration | Acoustic Testing | Room Analysis | Audio Engineers"
    }
]

def slugify(name):
    return name.lower().replace(" ", "-").replace("/", "-")

def create_product_html(product):
    slug = product["id"]
    title = product["title"]
    description = product["description"]
    keywords = product["keywords"]
    price = product["price"]
    specs = product["specs"]
    applications = product["applications"]
    features = product["h2_features"]
    
    canonical = f"{BASE_URL}/products/{slug}.html"
    
    # JSON-LD Product structured data
    json_ld = f'''<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{product['name']}",
    "description": "{description}",
    "brand": {{"@type": "Brand", "name": "DUMI"}},
    "sku": "{slug.upper()}",
    "category": "Acoustic Panels",
    "offers": {{
        "@type": "Offer",
        "price": "{price.replace('From $', '').replace('/kit', '').replace('/piece', '').replace('/screen', '').replace('/sqft', '').replace('/ft', '').replace('/panel', '').replace('/enclosure', '').replace('/can', '').replace('/wall', '').replace('/cover', '').replace('/booth', '')}",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": {{"@type": "Organization", "name": "DUMI Panel"}}
    }},
    "image": "{BASE_URL}/images/{slug}-product.jpg"
}}
</script>'''
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description} Sound absorbing panels for studio, office, and commercial use. {price}. Free shipping available.">
    <meta name="keywords" content="{keywords}, acoustic panel, soundproofing, sound absorbing panels">
    <link rel="canonical" href="{canonical}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="{canonical}">
    <meta name="twitter:card" content="product">
    {json_ld}
</head>
<body>
    <header>
        <nav>
            <a href="{BASE_URL}/">Home</a> > 
            <a href="{BASE_URL}/products.html">Products</a> > 
            <a href="{BASE_URL}/products/{slug}.html">{product['name']}</a>
        </nav>
    </header>
    
    <main>
        <h1>{product['name']}</h1>
        
        <img src="{BASE_URL}/images/{slug}-product.jpg" alt="{product['name']} - Professional acoustic treatment panel for studio and commercial use" width="600" height="400">
        
        <p class="price">{price}</p>
        
        <h2>Product Description</h2>
        <p>{description}</p>
        
        <h2>Specifications</h2>
        <p>{specs}</p>
        
        <h2>Key Features</h2>
        <ul>
            {"".join([f"<li>{feat.strip()}</li>" for feat in features.split("|")])}
        </ul>
        
        <h2>Applications</h2>
        <p>{applications}</p>
        
        <h2>Keywords</h2>
        <p class="keywords">{keywords}</p>
        
        <div class="inquiry-form">
            <h2>Request a Quote</h2>
            <form action="#" method="post">
                <input type="email" placeholder="Your email" required>
                <button type="submit">Send Inquiry</button>
            </form>
        </div>
    </main>
    
    <footer>
        <p>&copy; 2026 DUMI Panel. Professional Acoustic Solutions.</p>
    </footer>
</body>
</html>'''
    
    return html

# Create products directory if needed
os.makedirs(PRODUCTS_DIR, exist_ok=True)

# Generate all product pages
generated = []
for product in products:
    slug = product["id"]
    html_content = create_product_html(product)
    
    filepath = os.path.join(PRODUCTS_DIR, f"{slug}.html")
    with open(filepath, 'w') as f:
        f.write(html_content)
    
    generated.append(slug)
    print(f"Created: {slug}.html")

print(f"\nTotal products created: {len(generated)}")
print("Products:", ", ".join(generated))