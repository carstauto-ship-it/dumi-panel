#!/usr/bin/env python3
"""Generate 15 new acoustic panel product pages for dumi-panel.com"""

import os

PRODUCTS_DIR = '/Users/carstauto/.openclaw/workspace/dumi-panel/products'
DATE = '2026-04-26'

products = [
    {
        "slug": "mineral-wool-acoustic-boards",
        "filename": "mineral-wool-acoustic-boards.html",
        "name": "Mineral Wool Acoustic Boards",
        "tagline": "High-density mineral wool boards for superior broadband sound absorption",
        "description": "Mineral Wool Acoustic Boards are engineered from volcanic rock fibers to deliver exceptional broadband sound absorption across all frequencies. These boards are the industry standard for recording studios, commercial buildings, and industrial applications where acoustic performance is paramount. Their high density composition provides outstanding noise reduction coefficients while remaining fire-resistant and thermally insulating.",
        "price": "From $35/m²",
        "image": "../images/akupanelcn/mineral-wool-1.jpg",
        "features": [
            "High-density volcanic rock fiber composition",
            "Broadband absorption from 125Hz to 4kHz",
            "Non-combustible, fire-rated to A1",
            "Thermal insulation properties (lambda 0.035 W/mK)",
            "Moisture resistant and water repellent",
            "Available in various densities: 40-120 kg/m³"
        ],
        "specs": {
            "Material": "Mineral Wool (Volcanic Rock Fiber)",
            "Density": "40, 60, 80, 100, 120 kg/m³",
            "Thickness": "25mm, 50mm, 75mm, 100mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "NRC Rating": "0.75-1.00",
            "Fire Rating": "A1 (Non-combustible)",
            "Thermal Conductivity": "0.035 W/mK",
            "Application": "Studios, Cinemas, Industrial"
        },
        "applications": "Recording studios, home theaters, office partitions, industrial machinery enclosures, HVAC duct linings, ceiling void insulation",
        "keywords": "mineral wool acoustic board, rock wool panel, acoustic mineral board, soundproofing mineral wool, insulation board"
    },
    {
        "slug": "bamboo-fiber-acoustic-panels",
        "filename": "bamboo-fiber-acoustic-panels.html",
        "name": "Bamboo Fiber Acoustic Panels",
        "tagline": "Eco-friendly sustainable acoustic panels from renewable bamboo resources",
        "description": "Bamboo Fiber Acoustic Panels combine outstanding acoustic performance with environmental sustainability. Made from compressed bamboo fibers, these panels offer natural sound absorption properties while adding a warm, organic aesthetic to any space. Bamboo grows rapidly and regenerates without replanting, making these panels one of the most eco-conscious acoustic solutions available for green building projects.",
        "price": "From $48/m²",
        "image": "../images/akupanelcn/bamboo-1.jpg",
        "features": [
            "100% renewable and biodegradable material",
            "Natural warm aesthetic with unique grain patterns",
            "Excellent mid-frequency absorption performance",
            "Low embodied energy in manufacturing",
            "Hypoallergenic and formaldehyde-free options",
            "Ideal for LEED and green building projects"
        ],
        "specs": {
            "Material": "Compressed Bamboo Fiber",
            "Thickness": "12mm, 15mm, 25mm",
            "Standard Size": "600x600mm, 1200x600mm, 2400x1200mm",
            "NRC Rating": "0.65-0.85",
            "Fire Rating": "B1",
            "Density": "350-500 kg/m³",
            "Finish": "Natural, Carbonized, Lacquered",
            "Application": "Yoga Studios, Spas, Green Buildings"
        },
        "applications": "Yoga studios, meditation rooms, restaurants, hospitality venues, residential living rooms, eco-friendly office fit-outs, children's play areas",
        "keywords": "bamboo fiber acoustic panel, eco acoustic panel, sustainable sound absorption, green building acoustic, bamboo acoustic board"
    },
    {
        "slug": "gypsum-acoustic-boards",
        "filename": "gypsum-acoustic-boards.html",
        "name": "Gypsum Acoustic Boards",
        "tagline": "Perforated gypsum boards with integrated acoustic performance for ceilings and walls",
        "description": "Gypsum Acoustic Boards are perforated drywall panels designed for ceiling and wall installation in commercial and residential buildings. The precision-drilled perforations allow sound waves to enter the cavity behind the board where they are absorbed by insulation material. These boards integrate seamlessly with standard drywall installation methods while providing significant acoustic improvement over standard gypsum plasterboard.",
        "price": "From $22/board",
        "image": "../images/akupanelcn/gypsum-1.jpg",
        "features": [
            "Standard drywall installation methods",
            "Perforated pattern for acoustic resonance",
            "Compatible with standard grid ceiling systems",
            "Paintable surface in any color",
            "Fire-rated gypsum core available",
            "Cost-effective acoustic solution"
        ],
        "specs": {
            "Material": "Gypsum Plasterboard with Perforations",
            "Thickness": "9.5mm, 12.5mm, 15mm",
            "Standard Size": "600x600mm, 600x1200mm, 1200x2400mm",
            "Perforation Pattern": "Round, Square, Slotted",
            "NRC Rating": "0.55-0.80",
            "Fire Rating": "A2-s1,d0",
            "Cavity Depth": "50mm-200mm recommended",
            "Application": "Ceilings, Walls"
        },
        "applications": "Office corridors, meeting rooms, healthcare facilities, educational buildings, retail spaces, corridors, hallways, conference rooms",
        "keywords": "gypsum acoustic board, perforated gypsum board, acoustic plasterboard, soundproof drywall, ceiling acoustic board"
    },
    {
        "slug": "carbonized-acoustic-panels",
        "filename": "carbonized-acoustic-panels.html",
        "name": "Carbonized Acoustic Panels",
        "tagline": "Pyrolyzed wood panels with enhanced acoustic diffusion and striking dark aesthetics",
        "description": "Carbonized Acoustic Panels are produced through pyrolysis of natural wood, creating panels with a distinctive deep black carbonized surface. This thermal treatment process not only produces a striking visual appearance but also enhances the wood's acoustic properties by increasing its density and internal damping. These panels serve as both highly effective acoustic diffusers and bold design statements for premium interiors.",
        "price": "From $95/m²",
        "image": "../images/akupanelcn/carbonized-1.jpg",
        "features": [
            "Authentic carbonized wood surface (not painted)",
            "Enhanced internal damping for better absorption",
            "Class 1 fire performance after treatment",
            "Exceptional durability and dimensional stability",
            "Unique natural black color variations",
            "Suitable for both wall and ceiling installation"
        ],
        "specs": {
            "Material": "Pyrolyzed Natural Wood",
            "Thickness": "18mm, 22mm, 28mm",
            "Standard Size": "600x600mm, 1200x240mm",
            "NRC Rating": "0.60-0.75",
            "Fire Rating": "Class 1 (BS476 Part 7)",
            "Density": "600-800 kg/m³",
            "Finish": "Natural Carbonized Surface",
            "Application": "Luxury Hotels, Recording Studios, Theaters"
        },
        "applications": "Luxury hotel lobbies, high-end recording studios, boutique restaurants, museum galleries, executive boardrooms, premium retail environments",
        "keywords": "carbonized acoustic panel, charred wood panel, burnt wood acoustic, shou sugi ban acoustic, black wood panel"
    },
    {
        "slug": "polymer-composite-acoustic-panels",
        "filename": "polymer-composite-acoustic-panels.html",
        "name": "Polymer Composite Acoustic Panels",
        "tagline": "Durable polymer-fiberglass composite panels for demanding acoustic environments",
        "description": "Polymer Composite Acoustic Panels combine high-performance fiberglass acoustic cores with durable polymer surface finishes to create panels that withstand harsh environments while delivering superior sound control. These panels resist moisture, impact, and chemical exposure, making them ideal for swimming pools, industrial facilities, food processing plants, and other challenging applications where standard acoustic panels would fail.",
        "price": "From $68/m²",
        "image": "../images/akupanelcn/polymer-composite-1.jpg",
        "features": [
            "Fiberglass acoustic core with polymer skin",
            "Moisture and humidity resistant",
            "Impact and scratch resistant surface",
            "Chemical and grease resistant finish",
            "Easy to clean and sanitize",
            "UV stable for outdoor applications"
        ],
        "specs": {
            "Material": "Fiberglass Core + Polymer Surface",
            "Thickness": "25mm, 50mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "NRC Rating": "0.85-0.95",
            "Fire Rating": "B-s1,d0",
            "Impact Resistance": "IK08",
            "Water Absorption": "< 0.5%",
            "Application": "Indoor Pools, Spas, Industrial"
        },
        "applications": "Indoor swimming pools, spa facilities, water treatment plants, food processing facilities, marine environments, railway stations, tunnel linings",
        "keywords": "polymer composite acoustic panel, fiberglass composite panel, moisture resistant acoustic, wet room acoustic panel, industrial acoustic"
    },
    {
        "slug": "cassette-acoustic-panels",
        "filename": "cassette-acoustic-panels.html",
        "name": "Cassette Acoustic Panels",
        "tagline": "Modular cassette-style metal acoustic panels for architectural ceiling applications",
        "description": "Cassette Acoustic Panels are modular metal ceiling panels with micro-perforations that provide acoustic absorption while maintaining clean architectural lines. The cassette design creates a frameless appearance where the panel edges fold downward, creating a sleek continuous ceiling plane. Available in aluminum or steel with powder coat finishes, these panels are widely used in airports, transit stations, and modern office buildings.",
        "price": "From $55/m²",
        "image": "../images/akupanelcn/cassette-1.jpg",
        "features": [
            "Micro-perforated metal surface (0.5-1.5mm holes)",
            "Frameless modular cassette design",
            "Aluminum or galvanized steel construction",
            "Powder coat finish in RAL colors",
            "Compatible with standard ceiling grid systems",
            "Linear and square perforation patterns"
        ],
        "specs": {
            "Material": "Aluminum / Galvanized Steel",
            "Thickness": "0.6mm, 0.8mm, 1.0mm skin",
            "Module Size": "300x300mm, 600x600mm",
            "Perforation": "0.5mm to 1.5mm diameter",
            "NRC Rating": "0.70-0.90",
            "Fire Rating": "A2-s1,d0",
            "Finish": "Powder Coat (RAL colors)",
            "Application": "Ceiling Systems"
        },
        "applications": "Airport terminals, metro stations, shopping malls, corporate offices, hospital corridors, university buildings, government facilities",
        "keywords": "cassette acoustic panel, metal ceiling panel, micro-perforated metal, architectural ceiling panel, linear ceiling acoustic"
    },
    {
        "slug": "composite-sound-absorbers",
        "filename": "composite-sound-absorbers.html",
        "name": "Composite Sound Absorbers",
        "tagline": "Multi-layer composite panels combining mass and absorption for total acoustic control",
        "description": "Composite Sound Absorbers are engineered multi-layer acoustic panels that combine dense mass-loaded barrier layers with high-performance acoustic fiber cores to provide both sound absorption and sound blocking in a single panel. This dual-action approach makes them ideal for treating walls and ceilings where both reverberation control and sound isolation are required, such as in podcast recording spaces, home theaters, and music practice rooms.",
        "price": "From $72/m²",
        "image": "../images/akupanelcn/composite-absorber-1.jpg",
        "features": [
            "Integrated mass barrier + absorber construction",
            "Dual performance: absorption AND blocking",
            "Slim profile for space-constrained applications",
            "No resonance or drum effect",
            "Wall or ceiling mountable",
            "Class A fire rated materials"
        ],
        "specs": {
            "Material": "MLV Barrier + Acoustic Fiber + Fabric",
            "Total Thickness": "50mm, 75mm, 100mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "NRC Rating": "0.90-1.00",
            "STC Improvement": "+8 to +12 dB",
            "Fire Rating": "Class A",
            "Surface": "Acoustic Fabric (multi colors)",
            "Application": "Studios, Home Theaters, Practice Rooms"
        },
        "applications": "Podcast recording rooms, voice-over booths, drum rooms, music practice spaces, home theater walls, podcast studios, radio stations",
        "keywords": "composite sound absorber, multi-layer acoustic panel, mass loaded vinyl panel, sound block panel, dual performance acoustic"
    },
    {
        "slug": "calcium-silicate-acoustic-panels",
        "filename": "calcium-silicate-acoustic-panels.html",
        "name": "Calcium Silicate Acoustic Panels",
        "tagline": "Fire-proof calcium silicate boards with built-in acoustic performance",
        "description": "Calcium Silicate Acoustic Panels are incombustible building boards manufactured from calcium silicates that offer excellent fire resistance combined with good acoustic absorption properties. These panels withstand temperatures exceeding 1000°C without releasing toxic gases, making them essential for fire-rated wall and ceiling applications in high-rise buildings, tunnels, and industrial facilities where acoustic treatment must not compromise fire safety.",
        "price": "From $45/m²",
        "image": "../images/akupanelcn/calcium-silicate-1.jpg",
        "features": [
            "Incombustible calcium silicate composition",
            "Fire resistance exceeding 1000°C",
            "Zero smoke or toxic gas release",
            "Good acoustic absorption performance",
            "Dimensionally stable under heat",
            "Suitable for fire-rated construction systems"
        ],
        "specs": {
            "Material": "Calcium Silicate",
            "Thickness": "6mm, 9mm, 12mm, 20mm",
            "Standard Size": "1220x2440mm, 1200x600mm",
            "NRC Rating": "0.40-0.65",
            "Fire Rating": "A1 (Non-combustible)",
            "Maximum Temperature": "1000°C",
            "Density": "300-450 kg/m³",
            "Application": "Fire-rated Walls, Ceilings, Tunnels"
        },
        "applications": "High-rise building corridors, tunnel linings, industrial furnace rooms, boiler houses, elevator shafts, fire escape stairwells, power plant facilities",
        "keywords": "calcium silicate acoustic panel, fireproof acoustic board, incombustible panel, tunnel acoustic panel, high temperature acoustic"
    },
    {
        "slug": "perlite-acoustic-panels",
        "filename": "perlite-acoustic-panels.html",
        "name": "Perlite Acoustic Panels",
        "tagline": "Lightweight expanded perlite panels for thermal and acoustic insulation",
        "description": "Perlite Acoustic Panels are lightweight panels manufactured from expanded perlite ore, a volcanic glass that expands when heated to create a highly porous, low-density material with excellent acoustic absorption and thermal insulation properties. These panels are particularly effective in ceiling void applications where their lightweight nature reduces structural load while their open pore structure provides superior broadband absorption.",
        "price": "From $32/m²",
        "image": "../images/akupanelcn/perlite-1.jpg",
        "features": [
            "Expanded perlite volcanic glass material",
            "Exceptionally lightweight construction",
            "Open pore structure for broadband absorption",
            "Inorganic and rot-resistant composition",
            "Excellent thermal insulation properties",
            "Can be直接粘贴 or mechanically fixed"
        ],
        "specs": {
            "Material": "Expanded Perlite",
            "Density": "40-100 kg/m³",
            "Thickness": "25mm, 50mm, 75mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "NRC Rating": "0.60-0.85",
            "Fire Rating": "A1 (Non-combustible)",
            "Thermal Conductivity": "0.045 W/mK",
            "Application": "Ceiling Voids, Roof Spaces"
        },
        "applications": "Ceiling voids, roof insulation spaces, utility rooms, plant rooms, cold storage facilities, agricultural buildings, warehouse offices",
        "keywords": "perlite acoustic panel, expanded perlite board, lightweight acoustic panel, volcanic acoustic panel, ceiling void insulation"
    },
    {
        "slug": "acoustic-battens",
        "filename": "acoustic-battens.html",
        "name": "Acoustic Battens",
        "tagline": "Linear wooden acoustic battens for ceiling and wall installations with slatted aesthetics",
        "description": "Acoustic Battens are linear wooden slats designed for ceiling and wall installations where architectural aesthetics are as important as acoustic performance. The spacing between battens creates narrow slots that allow sound to reach the acoustic material behind, while the visible wood surface provides warm natural aesthetics. Available in various wood species, widths, and spacing configurations to suit any interior design scheme.",
        "price": "From $58/m²",
        "image": "../images/akupanelcn/battens-1.jpg",
        "features": [
            "Natural wood slat surface finish",
            "Configurable batten width and spacing",
            "Visible wood grain adds warmth to interiors",
            "Absorptive material behind the battens",
            "Wall and ceiling mounting options",
            " FSC certified wood options available"
        ],
        "specs": {
            "Material": "Solid Wood / Engineered Wood",
            "Batten Width": "27mm, 40mm, 60mm, 80mm",
            "Batten Depth": "15mm, 20mm, 30mm",
            "Spacing": "10mm, 15mm, 20mm, 30mm",
            "Standard Length": "2400mm, 3000mm",
            "NRC Rating": "0.65-0.80",
            "Fire Rating": "B1 (with treatment)",
            "Application": "Ceilings, Walls"
        },
        "applications": "Hotel reception areas, restaurant ceilings, retail showrooms, corporate atriums, library reading rooms, concert hall foyers, sports facility viewing areas",
        "keywords": "acoustic battens, wooden slat ceiling, timber acoustic battens, linear wood panel, slatted acoustic ceiling"
    },
    {
        "slug": "microporous-absorbers",
        "filename": "microporous-absorbers.html",
        "name": "Microporous Acoustic Absorbers",
        "tagline": "Ultra-fine pore acoustic panels engineered for low-frequency bass absorption",
        "description": "Microporous Acoustic Absorbers utilize extremely fine pore structures to achieve effective absorption at low frequencies that conventional acoustic panels cannot reach. These panels are specifically engineered for bass control in listening rooms, home theaters, and recording studios where low-frequency standing waves and bass buildup are the primary acoustic problems. The microporous technology allows panels to be thinner than traditional bass traps while achieving equivalent performance.",
        "price": "From $95/m²",
        "image": "../images/akupanelcn/microporous-1.jpg",
        "features": [
            "Ultra-fine pore structure for low-frequency absorption",
            "Thin profile compared to traditional bass traps",
            "Effective below 200Hz frequencies",
            "Consistent performance across humidity range",
            "No fiber release or particulate shedding",
            "Available as panels or free-standing units"
        ],
        "specs": {
            "Material": "Microporous Acoustic Foam / Mineral",
            "Thickness": "25mm, 40mm, 50mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "Absorption Range": "63Hz - 500Hz",
            "NRC Rating": "0.80-0.95 at low frequencies",
            "Fire Rating": "B1",
            "Density": "80-200 kg/m³",
            "Application": "Low-frequency Control, Bass Treatment"
        },
        "applications": "Recording studio control rooms, home theater bass zones, listening rooms, audiophile listening spaces, broadcast studios, dubbing stages, live mixing rooms",
        "keywords": "microporous absorber, bass absorber panel, low frequency acoustic panel, bass trap panel, subwoofer acoustic treatment"
    },
    {
        "slug": "cement-wood-wool-panels",
        "filename": "cement-wood-wool-panels.html",
        "name": "Cement Wood Wool Acoustic Panels",
        "tagline": "Reinforced cement-bonded wood fiber panels for acoustic and structural applications",
        "description": "Cement Wood Wool Acoustic Panels are manufactured by bonding shredded wood wool fibers with Portland cement to create panels that combine acoustic absorption with structural strength. The resulting panels can be used as both acoustic treatment and construction material, making them ideal for sports halls, swimming pool halls, and industrial buildings where durable acoustic panels must also withstand mechanical impact and moisture exposure.",
        "price": "From $40/m²",
        "image": "../images/akupanelcn/cement-wood-1.jpg",
        "features": [
            "Cement-bonded wood wool construction",
            "High impact and abrasion resistance",
            "Moisture and rot resistant",
            "Can be directly mechanically fixed without clips",
            "Load-bearing construction capability",
            "Natural concrete-wood aesthetic"
        ],
        "specs": {
            "Material": "Portland Cement + Wood Wool",
            "Thickness": "25mm, 35mm, 50mm",
            "Standard Size": "600x600mm, 1200x600mm, 2400x600mm",
            "NRC Rating": "0.70-0.90",
            "Fire Rating": "A2-s1,d0",
            "Compressive Strength": "5-15 MPa",
            "Density": "350-500 kg/m³",
            "Application": "Sports Halls, Industrial, Pools"
        },
        "applications": "Indoor sports halls, school gymnasiums, swimming pool halls, equestrian arenas, manufacturing plants, loading bay offices, agricultural storage buildings",
        "keywords": "cement wood wool panel, wood cement acoustic, cement bonded particle board, acoustic construction panel, impact resistant acoustic"
    },
    {
        "slug": "echo-cancellation-panels",
        "filename": "echo-cancellation-panels.html",
        "name": "Echo Cancellation Panels",
        "tagline": "Active electronic echo cancellation panels for real-time acoustic feedback elimination",
        "description": "Echo Cancellation Panels integrate passive acoustic absorption with active electronic echo cancellation technology to provide real-time elimination of acoustic feedback and echo in large reverberant spaces. These hybrid panels continuously monitor the acoustic environment and generate anti-phase signals to cancel reflections, making them ideal for conference rooms, lecture halls, and live performance venues where speech intelligibility is critical.",
        "price": "From $150/m²",
        "image": "../images/akupanelcn/echo-cancel-1.jpg",
        "features": [
            "Active electronic echo cancellation technology",
            "Real-time adaptive acoustic feedback elimination",
            "Passive absorption backing for broadband control",
            "Digital signal processing with auto-calibration",
            "Remote monitoring and adjustment capability",
            "Suitable for live voice and music applications"
        ],
        "specs": {
            "Material": "Active Electronics + Acoustic Backing",
            "Panel Thickness": "50mm passive + 20mm electronics",
            "Standard Size": "600x600mm, 1200x600mm",
            "Cancellation Range": "125Hz - 4kHz",
            "Attenuation": "Up to 15dB echo reduction",
            "Power": "24V DC / POE",
            "Connectivity": "Ethernet, RS485",
            "Application": "Conference, Live Venues"
        },
        "applications": "Conference rooms with video conferencing, lecture halls, courtrooms, live performance venues, Houses of worship, auditorium acoustic correction, telemedicine rooms",
        "keywords": "echo cancellation panel, active acoustic panel, electronic acoustic treatment, anti-echo panel, real-time acoustic correction"
    },
    {
        "slug": "spring-isolator-panels",
        "filename": "spring-isolator-panels.html",
        "name": "Spring Isolator Acoustic Panels",
        "tagline": "Decoupled spring-mount acoustic panels for maximum sound isolation performance",
        "description": "Spring Isolator Acoustic Panels are wall and ceiling panels mounted on resilient springs that physically decouple them from the building structure. This isolation prevents sound vibrations from traveling through the building structure, providing superior sound isolation performance compared to directly fixed panels. These are essential for achieving high STC ratings in recording studio walls, home cinema constructions, and any application where preventing sound transmission between spaces is the primary goal.",
        "price": "From $85/m²",
        "image": "../images/akupanelcn/spring-isolator-1.jpg",
        "features": [
            "Spring-loaded resilient mount isolation",
            "Decouples panel from building structure",
            "Prevents structural sound transmission",
            "Achieves STC ratings of 60+",
            "Minimal force on building walls",
            "Adjustable isolation performance"
        ],
        "specs": {
            "Material": "Steel Frame + Springs + Acoustic Fill",
            "Panel Thickness": "75mm, 100mm, 150mm",
            "Standard Size": "600x600mm, 1200x600mm",
            "NRC Rating": "0.95-1.00",
            "STC Improvement": "+15 to +25 dB",
            "Spring Rate": "20-60 Hz natural frequency",
            "Fire Rating": "A1 inner, B1 cladding",
            "Application": "Studio Walls, Isolation Rooms"
        },
        "applications": "Recording studio wall construction, home cinema room-within-room, broadcast control rooms, audio mastering suites, acoustic test chambers, industrial noise control enclosures",
        "keywords": "spring isolator panel, decoupled acoustic panel, sound isolation panel, resilient mount acoustic, studio wall isolation"
    },
    {
        "slug": "nitrile-rubber-acoustic-pads",
        "filename": "nitrile-rubber-acoustic-pads.html",
        "name": "Nitrile Rubber Acoustic Pads",
        "tagline": "High-density nitrile rubber pads for impact sound isolation and vibration damping",
        "description": "Nitrile Rubber Acoustic Pads are dense rubber sheets designed to isolate impact sound and reduce vibration transmission through floors and structural elements. Made from high-density nitrile rubber with excellent damping properties, these pads are the preferred solution for reducing footfall noise in apartments, controlling machinery vibration in industrial settings, and improving the acoustic separation of floating floor constructions.",
        "price": "From $18/m²",
        "image": "../images/akupanelcn/nitrile-pad-1.jpg",
        "features": [
            "High-density nitrile rubber composition",
            "Excellent impact sound isolation performance",
            "Superior vibration damping characteristics",
            "Oil and fuel resistant properties",
            "Long-term durability without compression set",
            "Wide temperature range stability"
        ],
        "specs": {
            "Material": "High-Density Nitrile Rubber (NBR)",
            "Thickness": "3mm, 5mm, 8mm, 12mm",
            "Standard Size": "1000x1000mm rolls",
            "Density": "800-1200 kg/m³",
            "Hardness": "60-80 Shore A",
            "Thermal Range": "-30°C to +80°C",
            "Fire Rating": "B1",
            "Application": "Floor Isolation, Vibration Damping"
        },
        "applications": "Apartment floor isolation under screed or wood flooring, machinery vibration isolation mounts, HVAC equipment vibration pads, elevator shaft isolation, pipe support isolation, professional recording studio floor isolation",
        "keywords": "nitrile rubber acoustic pad, impact sound pad, floor isolation pad, vibration damping pad, acoustic underlayment, soundproofing underlay"
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

    # Title (≤60 chars)
    title = f"{name} | Acoustic Panel Solutions | DUMI"

    # Meta description (150-160 chars)
    meta_desc = tagline + " Professional acoustic treatment from DUMI. Factory direct pricing, global shipping."
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + "..."

    # JSON-LD
    json_ld = f"""<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{name}",
  "description": "{tagline} Professional acoustic treatment from DUMI. Factory direct pricing worldwide.",
  "brand": {
    "@type": "Brand",
    "name": "DUMI"
  },
  "category": "Acoustic Panels / Soundproofing",
  "keywords": "{keywords}",
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "0",
    "availability": "https://schema.org/InStock"
  }}
}}
</script>"""

    # ALT text
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
    <!-- Header -->
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

    <!-- Product Detail -->
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

            <!-- Description -->
            <div style="margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Product Description</h2>
                <p style="line-height: 1.8; color: #555; max-width: 900px;">{desc}</p>
            </div>

            <!-- Specifications -->
            <div style="background: #ecf0f1; padding: 40px; border-radius: 10px; margin-bottom: 60px;">
                <h2 style="margin-bottom: 30px; color: #2c3e50;">Technical Specifications</h2>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
{specs_html}                </div>
            </div>

            <!-- Applications -->
            <div style="margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Applications</h2>
                <p style="line-height: 1.8; color: #555;">{applications}</p>
            </div>

            <!-- CTA -->
            <div style="text-align: center; margin: 60px 0;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Ready to Order?</h2>
                <p style="margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto;">Contact us for custom sizes, colors, and bulk pricing. We offer worldwide shipping and technical support.</p>
                <a href="../index.html#contact" class="cta-button" style="display: inline-block;">Contact Us Now</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
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
