#!/usr/bin/env python3
"""Generate 15 new acoustic panel product pages for dumi-panel.com - 2026-04-27"""

import os

PRODUCTS_DIR = '/Users/carstauto/.openclaw/workspace/dumi-panel/products'
DATE = '2026-04-27'

products = [
    {
        "slug": "acoustic-bass-traps",
        "filename": "acoustic-bass-traps.html",
        "name": "Acoustic Bass Traps",
        "tagline": "High-performance bass traps for low-frequency control in studios and home theaters",
        "description": "Acoustic Bass Traps are specialized acoustic treatment panels designed to absorb low-frequency sound waves that cause bass buildup and standing waves in rooms. These traps are essential for achieving accurate acoustic balance in recording studios, mastering rooms, and home theaters where low-frequency accuracy is critical for professional audio work.",
        "price": "From $65/piece",
        "image": "../images/akupanelcn/bass-trap-1.jpg",
        "features": [
            "Optimized for low-frequency absorption below 250Hz",
            "Corner-mounted design for maximum efficiency",
            "Broadband bass absorption capability",
            "Professional studio-grade performance",
            "Multiple installation options available",
            "Class A fire rated materials"
        ],
        "specs": {
            "Material": "Mineral Wool + Membrane",
            "Thickness": "100mm, 150mm, 200mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "Absorption Range": "40Hz - 250Hz",
            "NRC Rating": "0.95-1.00 at low frequencies",
            "Fire Rating": "Class A",
            "Mounting": "Corner, Wall, Ceiling",
            "Application": "Studios, Mastering Rooms, Home Theaters"
        },
        "applications": "Recording studio control rooms, audio mastering suites, home theater bass zones, broadcast studios, dubbing stages, music practice rooms, audiophile listening rooms",
        "keywords": "acoustic bass trap, bass trap panel, low frequency absorber, studio bass trap, corner bass trap, bass treatment"
    },
    {
        "slug": "fabric-wrapped-acoustic-panels",
        "filename": "fabric-wrapped-acoustic-panels.html",
        "name": "Fabric Wrapped Acoustic Panels",
        "tagline": "Customizable fabric-wrapped panels combining acoustic performance with interior design aesthetics",
        "description": "Fabric Wrapped Acoustic Panels are premium acoustic treatment panels encased in acoustically transparent fabric that allows sound waves to pass through to the absorbing core while providing a clean, designer finish. Available in hundreds of fabric colors and textures, these panels blend seamlessly into any interior design scheme from corporate offices to luxury residences.",
        "price": "From $55/m²",
        "image": "../images/akupanelcn/fabric-wrapped-1.jpg",
        "features": [
            "Hundreds of fabric color and texture options",
            "Acoustically transparent fabric material",
            "Seamless edge-to-edge fabric finish",
            "Custom sizes and shapes available",
            "Mounting hardware included",
            "CRC-free and eco-friendly fabrics available"
        ],
        "specs": {
            "Material": "Acoustic Fiber Core + Fabric Wrap",
            "Thickness": "25mm, 50mm, 75mm, 100mm",
            "Standard Size": "600x600mm, 1200x600mm, custom",
            "NRC Rating": "0.80-1.00",
            "Fire Rating": "Class A (with FR fabric)",
            "Fabric Options": "GUARD, Guilford of Maine, Camira",
            "Application": "Offices, Hotels, Restaurants, Homes"
        },
        "applications": "Corporate office meeting rooms, hotel lobbies and ballrooms, restaurant dining areas, residential home theaters, retail showrooms, healthcare facilities, educational classrooms",
        "keywords": "fabric wrapped acoustic panel, upholstered acoustic panel, acoustic wall panel, fabric acoustic panel, decorative acoustic panel, interior acoustic treatment"
    },
    {
        "slug": "perforated-wood-acoustic-panels",
        "filename": "perforated-wood-acoustic-panels.html",
        "name": "Perforated Wood Acoustic Panels",
        "tagline": "Perforated wood veneer panels with integrated acoustic absorption for architectural applications",
        "description": "Perforated Wood Acoustic Panels combine the warmth and beauty of natural wood veneer with precision-drilled perforations that allow sound to reach the acoustic backing material behind. These panels provide excellent mid to high-frequency absorption while maintaining a refined architectural appearance suitable for premium commercial and residential interiors.",
        "price": "From $85/m²",
        "image": "../images/akupanelcn/perforated-wood-1.jpg",
        "features": [
            "Real natural wood veneer surface",
            "Precision CNC-perforated patterns",
            "Multiple wood species available",
            "Excellent mid-frequency absorption",
            "Wall and ceiling mounting options",
            "FSC certified wood sources"
        ],
        "specs": {
            "Material": "Wood Veneer + Acoustic Backing",
            "Thickness": "15mm, 22mm, 28mm",
            "Standard Size": "600x600mm, 1200x600mm, 2400x1200mm",
            "Perforation Pattern": "Round, Square, Slot, Custom",
            "NRC Rating": "0.65-0.85",
            "Fire Rating": "B1",
            "Wood Species": "Oak, Walnut, Maple, Ash",
            "Application": "Auditoriums, Conference Rooms, Atriums"
        },
        "applications": "Concert hall interiors, corporate conference rooms, university lecture halls, museum galleries, luxury retail environments, executive boardrooms, library reading rooms",
        "keywords": "perforated wood acoustic panel, wooden perforated panel, acoustic wood panel, perforated timber panel, architectural wood panel, wood slat acoustic"
    },
    {
        "slug": "melamine-foam-acoustic",
        "filename": "melamine-foam-acoustic.html",
        "name": "Melamine Foam Acoustic Panels",
        "tagline": "Cost-effective melamine foam panels for professional sound absorption at an affordable price",
        "description": "Melamine Foam Acoustic Panels are lightweight, cost-effective acoustic treatment panels made from open-cell melamine resin foam. Despite their affordable price point, these panels offer excellent broadband sound absorption performance and are widely used in recording studios, practice rooms, and commercial spaces where budget-conscious acoustic treatment is required.",
        "price": "From $18/m²",
        "image": "../images/akupanelcn/melamine-foam-1.jpg",
        "features": [
            "Ultra-lightweight foam construction",
            "Excellent cost-to-performance ratio",
            "Broadband sound absorption",
            "Easy cutting and installation",
            "Multiple surface profiles available",
            "Self-supporting without frameworks"
        ],
        "specs": {
            "Material": "Melamine Resin Foam",
            "Thickness": "20mm, 30mm, 50mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "Surface Profile": "Plain, Pyramid, Wedge, Random",
            "NRC Rating": "0.70-0.95",
            "Fire Rating": "B1",
            "Density": "9-12 kg/m³",
            "Application": "Studios, Practice Rooms, Commercial"
        },
        "applications": "Home recording studios, music practice rooms, podcast recording spaces, home theater rooms, commercial office pods, call center acoustic treatment, HVAC noise reduction",
        "keywords": "melamine foam acoustic panel, acoustic foam panel, sound absorption foam, studio foam panels, melamine acoustic panel, budget acoustic panel"
    },
    {
        "slug": "glass-wool-acoustic-panels",
        "filename": "glass-wool-acoustic-panels.html",
        "name": "Glass Wool Acoustic Panels",
        "tagline": "High-performance glass wool acoustic panels for superior broadband sound absorption",
        "description": "Glass Wool Acoustic Panels are manufactured from fine glass fibers bonded with thermosetting resins to create highly effective sound absorption panels. Glass wool offers excellent acoustic performance across a wide frequency range, making it a preferred choice for commercial buildings, industrial facilities, and professional audio environments where consistent acoustic treatment is essential.",
        "price": "From $28/m²",
        "image": "../images/akupanelcn/glass-wool-1.jpg",
        "features": [
            "Fine glass fiber construction",
            "Excellent broadband absorption",
            "Thermal insulation properties included",
            "Moisture resistant binder",
            "Non-combustible mineral wool base",
            "Cost-effective acoustic solution"
        ],
        "specs": {
            "Material": "Glass Wool (Glass Fiber)",
            "Density": "24, 32, 48, 64 kg/m³",
            "Thickness": "25mm, 50mm, 75mm, 100mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "NRC Rating": "0.75-1.00",
            "Fire Rating": "A1 (Non-combustible)",
            "Thermal Resistance": "R-2.5 to R-11",
            "Application": "Studios, Industrial, Commercial"
        },
        "applications": "Recording studios and control rooms, industrial machinery enclosures, commercial building ceilings, HVAC equipment rooms, conference rooms, school classrooms, hospital waiting areas",
        "keywords": "glass wool acoustic panel, glass fiber acoustic panel, acoustic glass wool, sound absorption glass wool, studio glass wool, commercial acoustic panel"
    },
    {
        "slug": "ceiling-hanging-baffles",
        "filename": "ceiling-hanging-baffles.html",
        "name": "Ceiling Hanging Acoustic Baffles",
        "tagline": "Vertical hanging baffle systems for effective acoustic treatment in high-ceiling spaces",
        "description": "Ceiling Hanging Acoustic Baffles are vertically suspended acoustic panels designed to absorb sound in spaces with high ceilings where wall and ceiling surface area is insufficient for effective acoustic treatment. These baffles are commonly used in gymsnasiums, swimming pools, warehouses, and transit stations where reverberation control is challenging due to large volumes of air.",
        "price": "From $45/m²",
        "image": "../images/akupanelcn/hanging-baffle-1.jpg",
        "features": [
            "Vertically suspended installation",
            "Effective in high-ceiling applications",
            "Multiple suspension lengths available",
            "Weather-resistant options for pools",
            "Easy inspection and maintenance access",
            "Custom colors and graphics available"
        ],
        "specs": {
            "Material": "Mineral Wool / Glass Wool Core",
            "Baffle Size": "1200x300mm, 2400x400mm",
            "Thickness": "50mm, 75mm, 100mm",
            "Suspension Height": "300mm - 3000mm",
            "NRC Rating": "0.90-1.00",
            "Fire Rating": "A1 (Non-combustible)",
            "Water Resistance": "FR treated for pool use",
            "Application": "High Ceiling Spaces"
        },
        "applications": "Indoor swimming pool halls, school gymnasiums, warehouse distribution centers, airport terminal buildings, train station platforms, convention center halls, sports arena viewing areas",
        "keywords": "ceiling hanging baffle, acoustic baffle, hanging acoustic panel, suspended baffle, reverberation control baffle, high ceiling acoustic treatment"
    },
    {
        "slug": "perforated-metal-ceiling",
        "filename": "perforated-metal-ceiling.html",
        "name": "Perforated Metal Ceiling Panels",
        "tagline": "Architectural micro-perforated metal ceiling panels with integrated acoustic performance",
        "description": "Perforated Metal Ceiling Panels are architectural metal ceiling tiles with micro-precision perforations that provide acoustic absorption while maintaining clean modern aesthetic lines. The micro-perforations are invisible from normal viewing distances, creating the appearance of solid metal while delivering effective sound control. These panels are specified in airports, hospitals, and premium office developments worldwide.",
        "price": "From $65/m²",
        "image": "../images/akupanelcn/perforated-metal-1.jpg",
        "features": [
            "Micro-perforated invisible pattern",
            "Clean architectural appearance",
            "Aluminum or steel construction",
            "Powder coat finish in RAL colors",
            "Compatible with standard grid systems",
            "High durability and recyclability"
        ],
        "specs": {
            "Material": "Aluminum 0.7mm / Steel 0.5mm",
            "Perforation": "0.5mm, 0.7mm, 1.0mm diameter",
            "Module Size": "300x300mm, 600x600mm, 600x1200mm",
            "Finish": "Powder Coat (RAL), Anodized",
            "NRC Rating": "0.70-0.90",
            "Fire Rating": "A2-s1,d0",
            "Acoustic Backing": "50mm rock wool recommended",
            "Application": "Ceiling Systems"
        },
        "applications": "Airport terminal ceilings, hospital corridors and atriums, corporate office buildings, transit station platforms, shopping mall atriums, government building lobbies, university campus buildings",
        "keywords": "perforated metal ceiling, micro-perforated metal ceiling, architectural ceiling panel, metal ceiling tile, acoustic metal ceiling, commercial ceiling panel"
    },
    {
        "slug": "resilient-bar-channel",
        "filename": "resilient-bar-channel.html",
        "name": "Resilient Bar Channel Systems",
        "tagline": "Spring-decoupled channel systems for maximum wall and ceiling sound isolation",
        "description": "Resilient Bar Channel Systems are specialized furring channels that mechanically decouple drywall from building structure using a spring-like metal clip mechanism. This isolation prevents sound vibrations from transmitting through the wall or ceiling structure, dramatically improving the STC rating of the partition. Essential for achieving high-performance wall and ceiling constructions in recording studios and media rooms.",
        "price": "From $12/m²",
        "image": "../images/akupanelcn/resilient-bar-1.jpg",
        "features": [
            "Spring-loaded resilient clip mechanism",
            "Significant STC rating improvement",
            "Standard drywall installation compatible",
            "Minimal thickness addition",
            "Cost-effective sound isolation",
            " DIY-friendly installation"
        ],
        "specs": {
            "Material": "Galvanized Steel Channel + Spring Clip",
            "Channel Depth": "13mm, 20mm, 28mm",
            "Spacing": "400mm, 600mm centers",
            "STC Improvement": "+5 to +15 dB",
            "Fire Rating": "A1",
            "Max Span": "600mm without support",
            "Application": "Wall and Ceiling Isolation"
        },
        "applications": "Recording studio wall construction, home cinema room-within-room, apartment wall upgrades, professional broadcast studios, audio mastering facilities, acoustic test chambers, professional video production rooms",
        "keywords": "resilient bar channel, resilient channel, sound isolation channel, acoustic furring channel, decoupling channel, wall soundproofing channel"
    },
    {
        "slug": "acoustic-door-panels",
        "filename": "acoustic-door-panels.html",
        "name": "Acoustic Door Panels",
        "tagline": "Retrofitted acoustic door panels for upgrading standard doors to soundproof doors",
        "description": "Acoustic Door Panels are high-density acoustic boards designed to be mounted directly onto existing door surfaces to upgrade their sound isolation performance. These panels provide a cost-effective way to improve the STC rating of standard hollow-core or solid-core doors without requiring full door replacement. Essential for recording studio airlocks, home theater entrances, and professional audio facility vestibules.",
        "price": "From $85/piece",
        "image": "../images/akupanelcn/door-panel-1.jpg",
        "features": [
            "High-density mass-loaded construction",
            "Direct surface mounting on existing doors",
            "Significant STC improvement for standard doors",
            "Gasket seal kit included",
            "Multiple thickness options",
            "Professional studio-grade performance"
        ],
        "specs": {
            "Material": "Mass-Loaded Vinyl + Dense Fiber",
            "Thickness": "25mm, 50mm",
            "Standard Size": "900x2100mm, custom to door",
            "STC Improvement": "+10 to +20 dB",
            "Fire Rating": "B1",
            "Surface": "Acoustic fabric wrapped",
            "Seal System": "Automatic door bottom + perimeter gasket",
            "Application": "Door Upgrades"
        },
        "applications": "Recording studio vocal booths, home theater room entries, professional broadcast facilities, audio mastering suites, podcast recording rooms, voice-over booths, professional video production studios",
        "keywords": "acoustic door panel, soundproof door panel, door acoustic treatment, studio door panel, sound blocking door panel, door sound isolation panel"
    },
    {
        "slug": "mass-loaded-vinyl-sheets",
        "filename": "mass-loaded-vinyl-sheets.html",
        "name": "Mass Loaded Vinyl Sheets",
        "tagline": "High-density flexible vinyl sheets for floor, wall, and ceiling soundproofing",
        "description": "Mass Loaded Vinyl Sheets are dense, flexible sound blocking membranes that add mass to walls, floors, and ceilings to prevent sound from transmitting through building structures. Unlike rigid drywall, MLV sheets can be draped or wrapped around irregular shapes, making them ideal for pipes, ductwork, and structural elements where conventional rigid barriers cannot be easily installed.",
        "price": "From $25/m²",
        "image": "../images/akupanelcn/mlv-sheet-1.jpg",
        "features": [
            "Flexible and easy to drape",
            "High mass per square meter",
            "Can be wrapped around pipes and ducts",
            "Non-toxic and odor-free formulations",
            "Works as both blocker and damping layer",
            "Compatible with all construction types"
        ],
        "specs": {
            "Material": "Mass-Loaded Vinyl (MLV)",
            "Thickness": "1.5mm, 2.5mm, 3.5mm",
            "Weight": "2kg/m², 5kg/m², 8kg/m²",
            "Roll Size": "1.2m x 5m, 1.2m x 10m",
            "STC Improvement": "+5 to +15 dB per layer",
            "Fire Rating": "B1",
            "Temperature Range": "-30°C to +80°C",
            "Application": "Floor, Wall, Ceiling, Ducts"
        },
        "applications": "Apartment floor underlayment, studio wall construction, pipe wrapping for noise control, HVAC duct sound lagging, ceiling soundproofing, automotive sound deadening, marine vessel soundproofing",
        "keywords": "mass loaded vinyl, MLV sheet, soundproofing vinyl, floor soundproofing, wall sound blocking, acoustic vinyl sheet, sound deadening vinyl"
    },
    {
        "slug": "window-acoustic-glazing",
        "filename": "window-acoustic-glazing.html",
        "name": "Window Acoustic Glazing Units",
        "tagline": "Double and triple glazed acoustic windows for superior soundproofing of windows",
        "description": "Window Acoustic Glazing Units are specially designed multi-pane glass windows that dramatically reduce sound transmission from traffic, aircraft, and neighborhood noise. Using asymmetric glass thicknesses and specialized acoustic interlayers, these windows achieve STC ratings of 45-55 compared to standard double glazing at STC 30-35. Essential for properties in noisy urban environments.",
        "price": "From $350/window",
        "image": "../images/akupanelcn/acoustic-glazing-1.jpg",
        "features": [
            "Asymmetric glass thickness construction",
            "Acoustic PVB or resin interlayer",
            "STC ratings from 45 to 55",
            "U-value: 1.1-1.8 W/m²K",
            "UV blocking up to 99%",
            "Professional installation recommended"
        ],
        "specs": {
            "Material": "Laminated Acoustic Glass",
            "Configuration": "6+0.76+4+16+6mm, Custom",
            "Glass Thickness": "4mm, 6mm, 8mm, 10mm",
            "Cavity Width": "6mm to 20mm argon-filled",
            "STC Rating": "45-55 dB reduction",
            "Rw Rating": "42-52 dB",
            "Frame Material": "UPVC, Aluminum, Timber",
            "Application": "Windows"
        },
        "applications": "Homes near busy roads, apartments under flight paths, recording studio windows, video production studio glazing, professional audio control rooms, home theaters in noisy areas, healthcare facilities near hospitals",
        "keywords": "acoustic glazing, soundproof window, acoustic glass, double glazing soundproofing, triple glazing acoustic, window soundproofing, noise reduction window"
    },
    {
        "slug": "stadium-acoustic-panels",
        "filename": "stadium-acoustic-panels.html",
        "name": "Stadium Acoustic Panels",
        "tagline": "Impact-resistant acoustic panels designed for sports venue reverberation control",
        "description": "Stadium Acoustic Panels are specially engineered acoustic treatment panels designed to withstand the unique conditions found in sports venues including ball impacts, crowd noise, and large volume reverberation. These panels provide effective acoustic absorption while meeting stringent impact resistance requirements for arena construction. Used in sports halls, swimming pool arenas, and multi-purpose indoor stadiums worldwide.",
        "price": "From $75/m²",
        "image": "../images/akupanelcn/stadium-panel-1.jpg",
        "features": [
            "Ball-impact resistant construction",
            "Designed for large volume spaces",
            "Weather-resistant options for indoor arenas",
            "Fire-rated for public assembly venues",
            "Acoustic performance maintained post-impact",
            "Available with team branding graphics"
        ],
        "specs": {
            "Material": "Reinforced Mineral Wool + Mesh",
            "Thickness": "50mm, 75mm, 100mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "Impact Resistance": "BS 5234 Level 4",
            "NRC Rating": "0.90-1.00",
            "Fire Rating": "Class 0 (BS476 Part 6/7)",
            "Humidity Resistance": "Up to 95% RH",
            "Application": "Sports Venues"
        },
        "applications": "Indoor arena acoustics, swimming pool halls, multi-purpose sports halls, ice rink acoustics, indoor athletics facilities, gymnasium reverberation control, sports clubhouse facilities",
        "keywords": "stadium acoustic panel, sports venue acoustic, arena acoustic panel, gymnasium acoustic panel, sports hall acoustic treatment, indoor arena soundproofing"
    },
    {
        "slug": "transportation-acoustic-panels",
        "filename": "transportation-acoustic-panels.html",
        "name": "Transportation Acoustic Panels",
        "tagline": "Lightweight acoustic panels for automotive, rail, and marine transportation noise control",
        "description": "Transportation Acoustic Panels are lightweight, high-performance acoustic treatment solutions specifically engineered for vehicles, trains, ships, and aircraft where weight is a critical factor. These panels combine effective sound absorption with minimal added weight, improving passenger comfort and reducing fatigue on long journeys while meeting strict transportation fire safety regulations.",
        "price": "From $55/m²",
        "image": "../images/akupanelcn/transport-panel-1.jpg",
        "features": [
            "Ultra-lightweight construction",
            "Multi-layer acoustic absorption design",
            "Transportation fire safety compliant",
            "Moisture and vibration resistant",
            "Easy installation with adhesive backing",
            "Custom die-cutting available"
        ],
        "specs": {
            "Material": "Lightweight Acoustic Foam + MLV",
            "Thickness": "10mm, 20mm, 30mm",
            "Weight": "1.5-4 kg/m²",
            "Standard Size": "1000x1000mm, rolls available",
            "NRC Rating": "0.70-0.90",
            "Fire Rating": "BS 6853 / EN 45545 (transport)",
            "Temperature Range": "-40°C to +120°C",
            "Application": "Vehicles, Trains, Ships"
        },
        "applications": "Automotive engine bay insulation, train cabin acoustic treatment, ferry engine room lining, aircraft interior soundproofing, commercial vehicle cab insulation, recreational vehicle interior, luxury yacht cabin acoustics",
        "keywords": "transportation acoustic panel, automotive acoustic, rail acoustic panel, vehicle soundproofing, marine acoustic panel, ship soundproofing, lightweight acoustic panel"
    },
    {
        "slug": "marine-acoustic-panels",
        "filename": "marine-acoustic-panels.html",
        "name": "Marine Acoustic Panels",
        "tagline": "Saltwater-resistant acoustic panels for ships, yachts, and offshore installations",
        "description": "Marine Acoustic Panels are specially engineered acoustic treatment products designed to withstand the demanding marine environment including saltwater exposure, humidity, vibration, and salt spray. These panels are used in commercial vessels, luxury yachts, offshore platforms, and naval vessels where acoustic comfort and fire safety must be maintained in harsh maritime conditions.",
        "price": "From $95/m²",
        "image": "../images/akupanelcn/marine-panel-1.jpg",
        "features": [
            "Marine-grade salt-resistant materials",
            "Fire-rated for vessel safety regulations",
            "Vibration and shock resistant",
            "Low smoke and toxic gas emission",
            "Modular panel and tile options",
            "IMO/MED SOLAS compliant versions"
        ],
        "specs": {
            "Material": "Marine Mineral Wool + FR Resin",
            "Thickness": "25mm, 50mm, 75mm",
            "Standard Size": "600x600mm, custom",
            "NRC Rating": "0.80-0.95",
            "Fire Rating": "IMO Resolution A.653, MED compliant",
            "Salt Spray Resistance": "500+ hours (ASTM B117)",
            "Water Absorption": "< 2% by volume",
            "Application": "Marine Vessels"
        },
        "applications": "Luxury yacht interiors, commercial ship engine rooms, naval vessel accommodation areas, offshore oil platform living quarters, cruise ship public rooms, ferry passenger lounges, fishing vessel wheelhouses",
        "keywords": "marine acoustic panel, yacht acoustic panel, ship soundproofing, vessel acoustic treatment, offshore acoustic panel, naval acoustic panel, marine soundproofing"
    },
    {
        "slug": "custom-shaped-acoustic-panels",
        "filename": "custom-shaped-acoustic-panels.html",
        "name": "Custom Shaped Acoustic Panels",
        "tagline": "CNC-cut custom shaped acoustic panels for unique architectural installations",
        "description": "Custom Shaped Acoustic Panels are precision CNC-cut acoustic panels manufactured to exact specifications for unique architectural installations where standard rectangular panels cannot fit or achieve the desired aesthetic effect. From circular ceiling clouds to triangular wall features to branded logo panels, these custom solutions enable architects and designers to incorporate acoustic treatment as an integral part of interior design.",
        "price": "From $95/m²",
        "image": "../images/akupanelcn/custom-shape-1.jpg",
        "features": [
            "CNC precision cutting to any shape",
            "Vector file import (AI, DXF, DWG)",
            "3D design consultation available",
            "Logo and text cutting capability",
            "Complex geometric patterns possible",
            "Full acoustic performance maintained"
        ],
        "specs": {
            "Material": "Mineral Wool / PET Felt / Foam",
            "Thickness": "12mm to 100mm",
            "Max Size": "2400x1200mm per piece",
            "Tolerance": "± 0.5mm precision",
            "NRC Rating": "0.70-1.00 (shape dependent)",
            "Fire Rating": "A1 or B1 (material dependent)",
            "File Formats": "AI, EPS, DXF, DWG, PDF",
            "Application": "Architectural Feature Walls"
        },
        "applications": "Feature walls in hotel lobbies, corporate reception areas, retail brand environments, museum exhibition spaces, children's play centers, sports facility branding walls, acoustic art installations",
        "keywords": "custom shaped acoustic panel, custom cut acoustic panel, shaped acoustic panel, CNC acoustic panel, architectural acoustic panel, acoustic logo panel, decorative acoustic panel"
    }
]


def generate_product_html(product):
    """Generate HTML for a single product page."""
    slug = product['slug']
    filename = product['filename']
    name = product['name']
    tagline = product['tagline']
    desc = product['description']
    price = product['price']
    image = product['image']
    features = product['features']
    specs = product['specs']
    applications = product['applications']
    keywords = product['keywords']

    title = f"{name} | Acoustic Panel Solutions | DUMI"
    meta_desc = tagline + " Professional acoustic treatment from DUMI. Factory direct pricing, global shipping."
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + "..."

    json_ld = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{name}",
  "description": "{tagline} Professional acoustic treatment from DUMI. Factory direct pricing worldwide.",
  "brand": {{
    "@type": "Brand",
    "name": "DUMI"
  }},
  "category": "Acoustic Panels / Soundproofing",
  "keywords": "{keywords}",
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "0",
    "availability": "https://schema.org/InStock"
  }}
}}
</script>'''

    alt_text = f"{name} - {tagline}"

    specs_html = ""
    for key, value in specs.items():
        specs_html += f"""                    <div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">{key}</div>
                        <div style="margin-top: 5px;">{value}</div>
                    </div>
"""

    features_html = ""
    for feature in features:
        features_html += f"""                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span>{feature}</span>
                        </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="canonical" href="https://dumi-panel.com/products/{filename}">
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="acoustic panel, soundproofing, {keywords}">
    
    <link rel="stylesheet" href="../css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
{json_ld}
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="https://dumi-panel.com/products/{filename}">
</head>
<body>
    <header class="header" id="header">
        <div class="container">
            <div class="header-inner">
                <a href="../index.html" class="logo">
                    <span class="logo-icon">🔇</span>
                    <div class="logo-text">
                        <span class="logo-brand">DUMI</span>
                        <span class="logo-tagline">Professional Sound Solutions</span>
                    </div>
                </a>
                <nav class="nav">
                    <ul class="nav-menu">
                        <li><a href="../index.html" class="nav-link">Home</a></li>
                        <li><a href="../products.html" class="nav-link">Products</a></li>
                        <li><a href="../index.html#applications" class="nav-link">Applications</a></li>
                        <li><a href="../index.html#about" class="nav-link">About</a></li>
                        <li><a href="../index.html#contact" class="nav-link">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <section class="product-detail" style="padding: 60px 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; margin-bottom: 60px;">
                <div>
                    <img src="{image}" alt="{alt_text}" style="width: 100%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                </div>
                <div>
                    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: #2c3e50;">{name}</h1>
                    <p style="font-size: 1.2rem; color: #7f8c8d; margin-bottom: 30px;">{tagline}</p>
                    <div style="font-size: 2rem; font-weight: 700; color: #e74c3c; margin-bottom: 30px;">{price}</div>
                    <div style="margin: 30px 0;">
{features_html}                    </div>
                    <a href="../index.html#contact" class="cta-button" style="display: inline-block; margin-top: 20px;">Request Quote</a>
                </div>
            </div>

            <div style="margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Product Description</h2>
                <p style="line-height: 1.8; color: #555; max-width: 900px;">{desc}</p>
            </div>

            <div style="background: #ecf0f1; padding: 40px; border-radius: 10px; margin-bottom: 60px;">
                <h2 style="margin-bottom: 30px; color: #2c3e50;">Technical Specifications</h2>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
{specs_html}                </div>
            </div>

            <div style="margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Applications</h2>
                <p style="line-height: 1.8; color: #555;">{applications}</p>
            </div>

            <div style="text-align: center; margin: 60px 0;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Ready to Order?</h2>
                <p style="margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto;">Contact us for custom sizes, colors, and bulk pricing. We offer worldwide shipping and technical support.</p>
                <a href="../index.html#contact" class="cta-button" style="display: inline-block;">Contact Us Now</a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>DUMI Acoustic</h3>
                    <p>Professional acoustic solutions for noise control and sound absorption in various environments.</p>
                </div>
                <div class="footer-section">
                    <h3>Products</h3>
                    <ul class="footer-links">
                        <li><a href="pet-acoustic-panels.html">PET Acoustic Panels</a></li>
                        <li><a href="wood-slat-panels.html">Wood Slat Panels</a></li>
                        <li><a href="3d-acoustic-panels.html">3D Acoustic Panels</a></li>
                        <li><a href="acoustic-ceiling.html">Acoustic Ceiling</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../products.html">All Products</a></li>
                        <li><a href="../index.html#applications">Applications</a></li>
                        <li><a href="../index.html#contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Contact Info</h3>
                    <p>Email: carstauto2017@gmail.com</p>
                    <p>WeChat: +86-13001727017</p>
                    <p>WhatsApp: +61493342108</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 DUMI Professional Acoustic Panels Manufacturer. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""
    return html


def main():
    created = []
    for product in products:
        html = generate_product_html(product)
        filepath = os.path.join(PRODUCTS_DIR, product['filename'])
        with open(filepath, 'w') as f:
            f.write(html)
        created.append(product['filename'])
        print(f"Created: {product['filename']}")

    print(f"\nTotal created: {len(created)}")
    return created


if __name__ == '__main__':
    main()
