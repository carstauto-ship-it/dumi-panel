#!/usr/bin/env python3
"""Generate 12 additional acoustic panel product pages to reach 60+ products"""

import os

PRODUCTS_DIR = '/Users/carstauto/.openclaw/workspace/dumi-panel/products'

products = [
    {
        "slug": "studio-diffuser-panels",
        "filename": "studio-diffuser-panels.html",
        "name": "Studio Diffuser Panels",
        "tagline": "Premium quadratic residue diffusers for professional recording studios",
        "description": "Studio Diffuser Panels are precision-engineered acoustic diffusers designed to scatter sound waves evenly across a room, eliminating flutter echoes and standing waves while maintaining a live, natural-sounding environment. Our quadratic residue diffusers (QRDs) are crafted from high-density materials and are essential for professional recording studios, mastering rooms, and broadcast control rooms where accurate acoustic balance is critical.",
        "price": "From $85/m²",
        "image": "../images/akupanelcn/diffuser-1.jpg",
        "features": [
            "Precision QRD (Quadratic Residue) diffuser geometry",
            "Even sound scattering across mid and high frequencies",
            "Eliminates flutter echo and standing waves",
            "Maintains natural room liveliness",
            "Solid hardwood or MDF construction options",
            "Wall-mounted or free-standing configurations"
        ],
        "specs": {
            "Material": "High-Density MDF / Solid Wood",
            "Thickness": "50mm, 75mm, 100mm",
            "Standard Sizes": "600x600mm, 1200x600mm",
            "Diffusion Range": "500Hz - 8kHz",
            "Fire Rating": "B1",
            "Finish": "Natural Wood, Lacquered, Raw MDF",
            "Mounting": "Wall Mount / Free Standing",
            "Application": "Recording Studios, Mastering Rooms"
        },
        "applications": "Recording studios, mastering suites, mixing rooms, broadcast control rooms, home studios, podcast rooms, film post-production",
        "keywords": "studio diffuser panels, QRD diffuser, acoustic diffuser, sound diffuser, studio acoustic treatment, recording room diffusers"
    },
    {
        "slug": "cinema-acoustic-panels",
        "filename": "cinema-acoustic-panels.html",
        "name": "Cinema Acoustic Panels",
        "tagline": "High-performance acoustic panels engineered for private cinema rooms",
        "description": "Cinema Acoustic Panels are purpose-built for private home theaters and commercial cinema rooms, delivering controlled sound absorption and diffusion for optimal audio playback. These panels address the specific acoustic challenges of rectangular cinema rooms including bass buildup in corners, early reflections from side walls, and rear wall reflections that can smear dialogue clarity.",
        "price": "From $75/m²",
        "image": "../images/akupanelcn/echo-absorber-1.jpg",
        "features": [
            "Optimized for cinema room acoustics",
            "Broadband absorption for all speaker frequencies",
            "Bass management in corner locations",
            "Reflection control from side and rear walls",
            "Acoustically transparent fabric finishes",
            "Black core options to minimize visual presence"
        ],
        "specs": {
            "Material": "Mineral Wool / Glass Fiber + Fabric",
            "Thickness": "50mm, 75mm, 100mm, 150mm",
            "Standard Sizes": "1200x600mm, 2400x600mm",
            "NRC Rating": "0.85-1.00",
            "Bass NRC": "0.60-0.80 at 100Hz",
            "Fire Rating": "B1 / A2",
            "Finish": "Acoustic Fabric, Perforated Panel",
            "Application": "Cinema Rooms, Screening Rooms"
        },
        "applications": "Private home cinemas, commercial cinema lobbies, screening rooms, media rooms, film studios, VFX review rooms",
        "keywords": "cinema acoustic panels, home theater acoustic panels, theater soundproofing, cinema room treatment, movie room acoustics"
    },
    {
        "slug": "office-acoustic-ceiling-tiles",
        "filename": "office-acoustic-ceiling-tiles.html",
        "name": "Office Acoustic Ceiling Tiles",
        "tagline": "Drop-in ceiling tiles with superior speech absorption for open plan offices",
        "description": "Office Acoustic Ceiling Tiles are designed for commercial suspended ceiling systems, providing effective sound absorption to reduce ambient noise levels in open-plan offices, call centers, and collaborative workspaces. These tiles help control reverberation and improve speech clarity, creating more comfortable and productive work environments while meeting commercial building acoustic standards.",
        "price": "From $28/tile",
        "image": "../images/akupanelcn/ceiling-1.jpg",
        "features": [
            "Drop-in installation for standard grid ceilings",
            "High NRC ratings for speech absorption",
            "Reduces ambient office noise levels",
            "Moisture-resistant options for humid environments",
            "Class A fire rated for commercial buildings",
            "Sustainable recycled content options"
        ],
        "specs": {
            "Material": "Mineral Fiber / Fiberglass",
            "Thickness": "15mm, 19mm, 25mm",
            "Standard Size": "600x600mm, 600x1200mm",
            "NRC Rating": "0.70-0.90",
            "CAC Rating": "35-40",
            "Fire Rating": "A / Class A",
            "Light Reflectance": "Up to 85%",
            "Application": "Suspended Ceiling Grid"
        },
        "applications": "Open-plan offices, call centers, conference facilities, reception areas, libraries, healthcare waiting rooms, educational facilities",
        "keywords": "acoustic ceiling tiles, office ceiling panels, suspended ceiling tiles, drop-in ceiling panels, commercial ceiling absorption"
    },
    {
        "slug": "acoustic-wall-coverings",
        "filename": "acoustic-wall-coverings.html",
        "name": "Acoustic Wall Coverings",
        "tagline": "Fabric-wrapped acoustic panels for wall installation in premium interiors",
        "description": "Acoustic Wall Coverings are premium fabric-wrapped acoustic panels designed for direct wall installation in corporate, hospitality, and residential interiors where aesthetics and acoustic performance are equally important. Available in a wide range of fabric colors and textures, these panels provide effective sound absorption while serving as decorative wall elements.",
        "price": "From $65/m²",
        "image": "../images/akupanelcn/fabric-1.jpg",
        "features": [
            "Premium fabric finishes in unlimited colors",
            "Effective mid to high-frequency absorption",
            "Direct wall mount installation",
            "Custom sizes and shapes available",
            "Frames with acoustic mineral wool core",
            " LEED credit contributing materials"
        ],
        "specs": {
            "Material": "Mineral Wool Core + Acoustic Fabric",
            "Thickness": "25mm, 50mm",
            "Standard Sizes": "1200x600mm, 2400x1200mm, Custom",
            "NRC Rating": "0.80-0.95",
            "Fire Rating": "B1 / Class A",
            "Fabric Options": "Guilford of Maine, Camira, Gabriel",
            "Frame": "Aluminum or MDF",
            "Application": "Wall Installation"
        },
        "applications": "Corporate headquarters, hotel lobbies, conference rooms, boardrooms, restaurants, residential living rooms, home offices",
        "keywords": "acoustic wall coverings, fabric acoustic panels, wall mounted acoustic panels, acoustic wall tiles, interior acoustic treatment"
    },
    {
        "slug": "acoustic-bass-traps",
        "filename": "acoustic-bass-traps.html",
        "name": "Corner Bass Traps",
        "tagline": "High-performance bass absorption panels for corner placement",
        "description": "Corner Bass Traps are specifically engineered low-frequency absorption panels designed to be placed in room corners where bass energy naturally builds up. These traps use a combination of rigid mineral wool and air cavity backing to achieve effective bass absorption down to the lowest frequencies. Essential for any critical listening environment including recording studios, mixing rooms, and high-end home theaters.",
        "price": "From $95/piece",
        "image": "../images/akupanelcn/bass-trap-1.jpg",
        "features": [
            "Triangular corner-mounted design",
            "Deep bass absorption below 200Hz",
            "Broadband absorption when properly installed",
            "Can be floor-to-ceiling mounted",
            "Fabric-covered or raw finish options",
            "Stand-off and flush mount options"
        ],
        "specs": {
            "Material": "Mineral Wool / Fiberglass",
            "Thickness": "100mm, 150mm",
            "Base Size": "600x600mm triangle",
            "Length": "1200mm, 2400mm, Custom",
            "Bass Absorption": "NRC 0.80 at 100Hz",
            "Broadband NRC": "0.90+",
            "Fire Rating": "B1 / A2",
            "Mounting": "Corner Bracket / Adhesive",
            "Application": "Room Corners"
        },
        "applications": "Recording studios, mixing rooms, mastering suites, home theaters, listening rooms, broadcast studios, post-production facilities",
        "keywords": "bass traps, corner bass traps, low frequency absorption, studio bass traps, acoustic bass treatment, corner absorbers"
    },
    {
        "slug": "pipe-noise-covers",
        "filename": "pipe-noise-covers.html",
        "name": "Pipe Noise Cover Panels",
        "tagline": "Acoustic insulation jackets for noisy pipes and ductwork",
        "description": "Pipe Noise Cover Panels provide acoustic insulation for noisy water pipes, drain pipes, HVAC ducts, and mechanical pipes in residential and commercial buildings. These wrap-around covers reduce structure-borne and airborne noise transmission from pipes, solving common issues like running water noise, pipe hammering, and HVAC rumble without requiring pipe replacement.",
        "price": "From $45/m",
        "image": "../images/akupanelcn/micropore-1.jpg",
        "features": [
            "Wrap-around acoustic insulation design",
            "Reduces both airborne and structure-borne noise",
            "Flexible jacketing for easy installation",
            "Water-resistant outer skin",
            "Can be installed on existing pipes",
            "High-temperature rated options available"
        ],
        "specs": {
            "Material": "Fiberglass / Mineral Wool + PVC Jacket",
            "Thickness": "25mm, 50mm",
            "Pipe Diameter": "25mm - 300mm",
            "Length": "1m sections or custom",
            "Noise Reduction": "15-25 dB",
            "Temperature Range": "-30°C to +120°C",
            "Fire Rating": "B1 / A2",
            "Application": "Pipes and Ductwork"
        },
        "applications": "Apartment buildings, hotels, offices, hospitals, schools, residential bathrooms, mechanical rooms, HVAC systems",
        "keywords": "pipe noise covers, pipe insulation, duct noise reduction, acoustic pipe wrap, plumbing soundproofing, HVAC noise control"
    },
    {
        "slug": "outdoor-noise-barriers",
        "filename": "outdoor-noise-barriers.html",
        "name": "Outdoor Noise Barrier Panels",
        "tagline": "Weather-resistant acoustic barriers for outdoor noise reduction",
        "description": "Outdoor Noise Barrier Panels are heavy-duty, weather-resistant acoustic barriers designed for exterior applications including highway noise reduction, construction site boundaries, outdoor equipment enclosures, and outdoor event venues. These panels are engineered to withstand UV exposure, rain, wind, and temperature extremes while providing effective long-term outdoor sound reduction.",
        "price": "From $150/m²",
        "image": "../images/akupanelcn/perforated-metal-1.jpg",
        "features": [
            "UV-stable and weather-resistant construction",
            "Heavy-duty steel or aluminum frame",
            "Designed for decades of outdoor use",
            "High STC ratings for traffic noise",
            "Anti-graffiti coating options",
            "Vegetation integration for green barriers"
        ],
        "specs": {
            "Material": "Steel/Aluminum + Dense Core + Weather Skin",
            "Thickness": "50mm, 75mm, 100mm",
            "Panel Size": "1000x2000mm, 1250x2500mm",
            "STC Rating": "35-48 dB",
            "Weather Resistance": "UV Stable, -30°C to +70°C",
            "Fire Rating": "A1 / A2",
            "Wind Load": "Up to 150 km/h",
            "Application": "Outdoor Enclosures"
        },
        "applications": "Highway noise barriers, construction site screens, outdoor equipment enclosures, rooftop mechanical screening, outdoor event venues, sports facility boundaries",
        "keywords": "outdoor noise barriers, acoustic fence panels, highway noise reduction, outdoor soundproofing, exterior acoustic panels, weather resistant acoustic barriers"
    },
    {
        "slug": "artistic-acoustic-panels",
        "filename": "artistic-acoustic-panels.html",
        "name": "Artistic Acoustic Panel Art",
        "tagline": "Custom-printed acoustic panels featuring artwork and photography",
        "description": "Artistic Acoustic Panel Art combines custom-printed artwork, photography, or graphic designs with high-performance acoustic cores to create functional wall art that improves room acoustics. These panels serve a dual purpose: enhancing room sound quality while adding visual impact as statement wall pieces. Perfect for home theaters, hospitality spaces, and corporate environments seeking unique acoustic solutions.",
        "price": "From $120/m²",
        "image": "../images/akupanelcn/acoustic-screen-1.jpg",
        "features": [
            "Custom high-resolution printing on acoustic panel",
            "Full-color photographic or artwork printing",
            "Acoustic performance not compromised by print",
            "Various frame and edge options",
            "Large format up to 3m wide",
            "Both absorptive and diffusive versions"
        ],
        "specs": {
            "Material": "Acoustic Core + Printed Canvas/Vinyl",
            "Thickness": "25mm, 50mm",
            "Max Size": "3000mm x 1200mm",
            "Print Resolution": "1200 DPI",
            "NRC Rating": "0.75-0.90",
            "Fire Rating": "B1",
            "Print Surface": "Fabric, Canvas, Vinyl",
            "Application": "Wall Mounted Art"
        },
        "applications": "Home theater feature walls, hotel lobbies, corporate art installations, restaurant decor, residential living spaces, media rooms",
        "keywords": "artistic acoustic panels, printed acoustic panels, acoustic wall art, custom acoustic art, decorative acoustic panels, acoustic panel art"
    },
    {
        "slug": "acoustic-door-seals",
        "filename": "acoustic-door-seals.html",
        "name": "Acoustic Door Seal Kits",
        "tagline": "Complete sealing systems for soundproof doors",
        "description": "Acoustic Door Seal Kits provide comprehensive weatherstripping and sealing solutions for soundproof doors, reducing sound leakage through door perimeters. These complete kits include door sweeps, jamb seals, and threshold seals that work together to achieve the door's rated STC performance. Essential for recording studios, home theaters, and any room requiring sound isolation.",
        "price": "From $85/kit",
        "image": "../images/akupanelcn/acoustic-door-1.jpg",
        "features": [
            "Complete door sealing system",
            "Drop-down door sweep for bottom seal",
            "Adhesive jamb seals for sides and top",
            "Adjustable threshold seal",
            "Maintains door acoustic rating",
            "Suitable for wood and metal doors"
        ],
        "specs": {
            "Material": "Silicone / EPDM Rubber + Aluminum",
            "Door Gap Coverage": "Up to 15mm",
            "STC Improvement": "+8 to +12 dB",
            "Fire Rated Options": "Available",
            "Finish": "Silver, Brown, White, Black",
            "Length": "Door perimeter + threshold",
            "Installation": "Adhesive / Screw Fix",
            "Application": "Soundproof Door Perimeters"
        },
        "applications": "Recording studio doors, home theater doors, apartment entry doors, office conference rooms, broadcast booths, music practice rooms",
        "keywords": "acoustic door seals, door weatherstripping, soundproof door seals, door seal kits, acoustic door weatherstripping, sound isolation door seals"
    },
    {
        "slug": "acoustical-vanity-mirrors",
        "filename": "acoustical-vanity-mirrors.html",
        "name": "Acoustical Vanity Mirrors",
        "tagline": "Sound-absorbing mirror panels for bathrooms with acoustic needs",
        "description": "Acoustical Vanity Mirrors combine the functionality of bathroom mirrors with sound-absorbing acoustic panels, providing dual benefits of room acoustics improvement and mirror functionality. These are ideal for hotel bathrooms, spa changing rooms, and upscale residential bathrooms where both acoustics and aesthetics matter.",
        "price": "From $180/piece",
        "image": "../images/akupanelcn/acoustic-tile-1.jpg",
        "features": [
            "Mirror surface with acoustic backing",
            "Combines reflection and absorption",
            "Moisture-resistant for wet environments",
            "Standard and custom sizes available",
            "Frameless and framed options",
            "LED mirror integration available"
        ],
        "specs": {
            "Material": "Acoustic Panel + Mirror Glass",
            "Thickness":": "40mm total (6mm mirror + 34mm panel)",
            "Standard Sizes": "600x600mm, 600x900mm, 1200x600mm",
            "NRC Rating": "0.70-0.85",
            "Moisture Resistance": "IP44 rated",
            "Fire Rating": "B1",
            "Mirror Thickness": "4mm, 6mm",
            "Application": "Bathroom Walls"
        },
        "applications": "Hotel bathrooms, spa changing rooms, luxury residential bathrooms, gym changing rooms, hair salon walls, dance studio viewing areas",
        "keywords": "acoustical vanity mirrors, acoustic mirror panels, sound absorbing mirrors, bathroom acoustic panels, spa acoustic mirrors, hotel bathroom acoustics"
    },
    {
        "slug": "studio-acoustic-foam-profiles",
        "filename": "studio-acoustic-foam-profiles.html",
        "name": "Studio Acoustic Foam Profiles",
        "tagline": "Professional acoustic foam in wedge, pyramid, egg-crate, and flat profiles",
        "description": "Studio Acoustic Foam Profiles offer professional-grade acoustic treatment in a variety of surface profiles to match different room requirements and aesthetic preferences. From classic wedge panels for broadband absorption to pyramid panels for enhanced high-frequency diffusion, these foams provide effective room treatment for recording studios, podcast spaces, and home theaters at accessible price points.",
        "price": "From $35/m²",
        "image": "../images/akupanelcn/concertina-foam-1.jpg",
        "features": [
            "Multiple profile options: wedge, pyramid, egg-crate, flat",
            "High-density foam for consistent performance",
            "Broadband absorption from 200Hz upward",
            "Self-adhesive backing for easy mounting",
            "Class B fire-rated versions available",
            "Cost-effective professional results"
        ],
        "specs": {
            "Material": "Open-Cell Polyurethane Foam",
            "Thickness": "30mm, 50mm, 75mm",
            "Standard Sizes": "500x500mm, 600x600mm",
            "Density": "25-35 kg/m³",
            "NRC Rating": "0.70-0.90",
            "Fire Rating": "B1 / CA117",
            "Profile Options": "Wedge, Pyramid, Egg-crate, Flat",
            "Application": "Wall and Ceiling Treatment"
        },
        "applications": "Recording studios, podcast rooms, voice-over booths, home theaters, mixing rooms, rehearsal spaces, drum rooms, instrument isolation",
        "keywords": "acoustic foam studio, wedge foam panels, pyramid acoustic foam, egg crate foam, studio foam panels, sound foam panels"
    },
    {
        "slug": "concert-hall-acoustic-panels",
        "filename": "concert-hall-acoustic-panels.html",
        "name": "Concert Hall Acoustic Panels",
        "tagline": "Architectural acoustic panels for concert halls and performing arts centers",
        "description": "Concert Hall Acoustic Panels are architectural-grade acoustic treatment products designed for world-class performing arts venues, concert halls, and theaters. These panels feature precision-engineered acoustics with custom finishes that integrate seamlessly into prestigious architectural designs while delivering the controlled reverberation and intelligibility that live music and speech performances demand.",
        "price": "From $180/m²",
        "image": "../images/akupanelcn/stretch-ceiling-1.jpg",
        "features": [
            "Architectural-grade acoustic engineering",
            "Custom finishes: wood veneer, metal, stone",
            "Precision-tuned for specific venue acoustics",
            "Integrated lighting and speaker mounting",
            "Concealed fixing systems",
            "Tested to international acoustic standards"
        ],
        "specs": {
            "Material": "Engineered Acoustic Core + Architectural Finish",
            "Thickness": "50mm - 200mm",
            "Standard Sizes": "1200x600mm, 2400x1200mm, Custom",
            "NRC Rating": "0.85-1.00",
            "Fire Rating": "A2-s1, d0",
            "Finish Options": "Wood Veneer, Perforated Metal, Stone, Custom",
            "RT60 Adjustment": "Precision tuned per venue",
            "Application": "Concert Halls, Theaters, Auditoriums"
        },
        "applications": "Concert halls, opera houses, symphony halls, performing arts centers, lecture theaters, church sanctuaries, chamber music venues",
        "keywords": "concert hall acoustic panels, performing arts acoustic panels, auditorium acoustic treatment, concert venue acoustics, theater acoustic panels"
    }
]

def feature_list_html(features):
    lines = []
    for feat in features:
        lines.append('                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">')
        lines.append('                            <span style="color: #3498db; margin-right: 10px;">&#10003;</span>')
        lines.append(f'                            <span>{feat}</span>')
        lines.append('                        </div>')
    return '\n'.join(lines)

def specs_grid_html(specs):
    lines = []
    for k, v in specs.items():
        lines.append('                    <div style="padding: 15px; background: white; border-radius: 5px;">')
        lines.append(f'                        <div style="font-weight: 600; color: #2c3e50;">{k}</div>')
        lines.append(f'                        <div style="margin-top: 5px;">{v}</div>')
        lines.append('                    </div>')
    return '\n'.join(lines)

def generate_product_html(product):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product["name"]} | Professional Acoustic Solutions</title>
    <link rel="canonical" href="https://dumi-panel.com/products/{product["slug"]}.html">
    <meta name="description" content="{product["tagline"]}">
    <meta name="keywords" content="{product["keywords"]}">
    
    <link rel="stylesheet" href="../css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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
                    <img src="{product["image"]}" alt="{product["name"]}" style="width: 100%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                </div>
                <div>
                    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: #2c3e50;">{product["name"]}</h1>
                    <p style="font-size: 1.2rem; color: #7f8c8d; margin-bottom: 30px;">{product["description"]}</p>
                    
                    <div style="font-size: 2rem; font-weight: 700; color: #e74c3c; margin-bottom: 30px;">{product["price"]}</div>
                    
                    <div style="margin: 30px 0;">
{feature_list_html(product["features"])}
                    </div>
                    
                    <a href="../index.html#contact" class="cta-button" style="display: inline-block; margin-top: 20px;">Request Quote</a>
                </div>
            </div>

            <!-- Applications -->
            <div style="background: #f8f9fa; padding: 40px; border-radius: 10px; margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; color: #2c3e50;">Applications</h2>
                <p style="font-size: 1.1rem; color: #555;">{product["applications"]}</p>
            </div>

            <!-- Specifications -->
            <div style="background: #ecf0f1; padding: 40px; border-radius: 10px; margin-bottom: 60px;">
                <h2 style="margin-bottom: 30px; color: #2c3e50;">Technical Specifications</h2>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
{specs_grid_html(product["specs"])}
                </div>
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
</html>'''

for product in products:
    filepath = os.path.join(PRODUCTS_DIR, product["filename"])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(generate_product_html(product))
    print(f'Created: {product["filename"]}')

print(f'\nTotal: {len(products)} extra product pages created!')
