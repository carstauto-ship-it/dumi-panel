#!/usr/bin/env python3
"""Generate 12 new acoustic panel product pages"""

import os

PRODUCTS_DIR = '/Users/carstauto/.openclaw/workspace/dumi-panel/products'

products = [
    {
        "slug": "polyester-fiber-acoustic-panels",
        "filename": "polyester-fiber-acoustic-panels.html",
        "name": "Polyester Fiber Acoustic Panels",
        "tagline": "Eco-friendly 100% polyester fiber panels with superior sound absorption",
        "description": "Our Polyester Fiber Acoustic Panels are manufactured from 100% recycled polyester fibers, making them an environmentally friendly choice for acoustic treatment. These panels offer excellent sound absorption across a wide frequency range while being lightweight, durable, and easy to install. Perfect for offices, schools, recording studios, and residential spaces where both aesthetics and acoustic performance matter.",
        "price": "From $38/m²",
        "image": "../images/akupanelcn/fabric-1.jpg",
        "features": [
            "100% recycled polyester material, eco-friendly",
            "Excellent sound absorption NRC 0.85-0.95",
            "Lightweight and easy to handle",
            "Multiple colors and thicknesses available",
            "Class A fire rating available",
            "Anti-static and dust-resistant finish"
        ],
        "specs": {
            "Material": "100% Recycled Polyester Fiber",
            "Thickness": "9mm, 12mm, 24mm",
            "Standard Sizes": "1220x2440mm, 600x600mm, 1200x600mm",
            "Density": "60-200 kg/m3",
            "Fire Rating": "B1 / Class A",
            "NRC Rating": "0.85-0.95",
            "Color": "36+ standard colors",
            "Application": "Walls and Ceilings"
        },
        "applications": "Office partitions, conference rooms, home theaters, recording studios, restaurants, schools, libraries, healthcare facilities",
        "keywords": "polyester fiber acoustic panels, pet acoustic panels, eco acoustic panels, recycled acoustic panels, sound absorbing panels"
    },
    {
        "slug": "melamine-foam-panels",
        "filename": "melamine-foam-panels.html",
        "name": "Melamine Foam Acoustic Panels",
        "tagline": "Lightweight open-cell melamine foam for superior high-frequency absorption",
        "description": "Melamine Foam Acoustic Panels utilize advanced open-cell melamine resin foam technology to deliver exceptional sound absorption, particularly in the high and mid-frequency ranges. These ultra-lightweight panels are ideal for recording studios, broadcast rooms, and precision acoustic environments. The smooth, clean surface requires no fabric covering, reducing cost while maintaining excellent acoustic performance.",
        "price": "From $32/m²",
        "image": "../images/akupanelcn/micropore-1.jpg",
        "features": [
            "Ultra-lightweight open-cell foam structure",
            "Outstanding high-frequency absorption",
            "Smooth surface, no fabric required",
            "Excellent thermal insulation properties",
            "Self-extinguishing fire performance",
            "Cost-effective acoustic solution"
        ],
        "specs": {
            "Material": "Melamine Resin Foam",
            "Thickness": "20mm, 30mm, 50mm",
            "Standard Sizes": "1200x600mm, 600x600mm",
            "Density": "8-12 kg/m3",
            "Fire Rating": "B1",
            "NRC Rating": "0.70-0.85",
            "Color": "White, Grey",
            "Application": "Walls and Ceilings"
        },
        "applications": "Recording studios, radio stations, home theaters, conference rooms, music rehearsal rooms, speaker enclosures",
        "keywords": "melamine foam panels, acoustic foam, sound absorbing foam, studio foam panels, open-cell foam acoustic"
    },
    {
        "slug": "glass-fiber-acoustic-panels",
        "filename": "glass-fiber-acoustic-panels.html",
        "name": "Glass Fiber Acoustic Panels",
        "tagline": "High-performance glass wool panels for professional acoustic environments",
        "description": "Glass Fiber Acoustic Panels combine high-density glass wool cores with protective facing materials to deliver superior broadband sound absorption. These panels are engineered for professional acoustic applications in theaters, auditoriums, concert halls, and commercial buildings where maximum sound control is required. The panels can be finished with fabric, perforated metal, or wood veneer for architectural integration.",
        "price": "From $55/m²",
        "image": "../images/akupanelcn/ceiling-1.jpg",
        "features": [
            "High-density glass wool core for maximum absorption",
            "Broadband frequency absorption performance",
            "Various finish options: fabric, metal, wood",
            "Excellent thermal and acoustic properties combined",
            "Commercial and professional grade durability",
            "Meets international acoustic standards"
        ],
        "specs": {
            "Material": "High-Density Glass Wool + Finish Layer",
            "Thickness": "25mm, 50mm, 75mm, 100mm",
            "Standard Sizes": "1200x600mm, 2400x600mm",
            "Density": "48-96 kg/m3",
            "Fire Rating": "A2-s1, d0 (non-combustible)",
            "NRC Rating": "0.90-1.00",
            "Finish Options": "Fabric, Perforated Metal, Wood Veneer",
            "Application": "Walls and Ceilings"
        },
        "applications": "Theaters, concert halls, auditoriums, cinemas, convention centers, sports arenas, industrial noise control",
        "keywords": "glass fiber acoustic panels, glass wool panels, commercial acoustic panels, theater acoustic panels, high performance sound absorption"
    },
    {
        "slug": "acoustic-baffles",
        "filename": "acoustic-baffles.html",
        "name": "Acoustic Baffles",
        "tagline": "Hanging sound absorbers for large-volume spaces with hard reflective surfaces",
        "description": "Acoustic Baffles are vertically suspended sound-absorbing panels designed specifically for large spaces with high ceilings and hard reflective surfaces such as warehouses, gymnasiums, swimming pools, and industrial facilities. By hanging from ceiling structures, these baffles create air gaps on all sides, dramatically improving mid to high-frequency absorption. Available in various sizes, thicknesses, and colors to match architectural requirements.",
        "price": "From $65/piece",
        "image": "../images/akupanelcn/stretch-ceiling-1.jpg",
        "features": [
            "Vertically suspended design for maximum exposure",
            "Air gap on all sides enhances absorption",
            "Ideal for high-ceiling spaces",
            "Multiple mounting options available",
            "Weather-resistant options for industrial use",
            "Custom colors and sizes available"
        ],
        "specs": {
            "Material": "Mineral Wool / Glass Fiber / Polyester",
            "Thickness": "50mm, 75mm, 100mm",
            "Standard Sizes": "600x1200mm, 600x1800mm, 600x2400mm",
            "Density": "48-80 kg/m3",
            "Fire Rating": "A1 / B1",
            "NRC Rating": "0.95-1.05",
            "Mounting": "Chain, Cable, or Track System",
            "Application": "Hanging Vertical Installation"
        },
        "applications": "Indoor swimming pools, gymnasiums, warehouses, factories, churches, atriums, transit stations, exhibition halls",
        "keywords": "acoustic baffles, hanging acoustic panels, vertical baffles, ceiling baffles, sound absorbing baffles, industrial acoustic treatment"
    },
    {
        "slug": "mass-loaded-vinyl-panels",
        "filename": "mass-loaded-vinyl-panels.html",
        "name": "Mass Loaded Vinyl Soundproof Panels",
        "tagline": "Thin, dense vinyl barrier for effective sound blocking in limited spaces",
        "description": "Mass Loaded Vinyl (MLV) Soundproof Panels provide high-mass sound blocking in an exceptionally thin profile. These panels use dense vinyl compound loaded with barium salts or similar materials to create effective sound barriers. Ideal for applications where wall thickness is limited but significant sound blocking is required. MLV panels are flexible yet dense, conforming to surfaces while blocking airborne sound transmission.",
        "price": "From $48/m²",
        "image": "../images/akupanelcn/perforated-metal-1.jpg",
        "features": [
            "Thin profile — only 3-6mm thick",
            "High mass for effective sound blocking",
            "Flexible and conforming to irregular surfaces",
            "Excellent for constrained spaces",
            "Can be combined with acoustic panels for combo solutions",
            "No structural reinforcement required"
        ],
        "specs": {
            "Material": "Mass Loaded Vinyl (MLV)",
            "Thickness": "3mm, 4.5mm, 6mm",
            "Standard Sizes": "1200x600mm, 2400x1200mm",
            "Density": "3.5-5 kg/m2",
            "Fire Rating": "B1",
            "STC Rating": "26-32 dB per layer",
            "Color": "Black, Grey, White",
            "Application": "Walls, Floors, Ceilings"
        },
        "applications": "Apartment walls, home offices, music practice rooms, home theaters, automotive soundproofing, machinery enclosures",
        "keywords": "mass loaded vinyl, mlv panels, sound blocking panels, thin soundproofing, vinyl sound barrier, acoustic mass panels"
    },
    {
        "slug": "composite-soundproof-panels",
        "filename": "composite-soundproof-panels.html",
        "name": "Composite Soundproof Panels",
        "tagline": "Multi-layer engineered panels combining mass, damping, and absorption",
        "description": "Composite Soundproof Panels are engineered multi-layer systems that combine mass-loaded barriers, constrained-layer damping compounds, and acoustic absorption materials in a single panel. This layered approach addresses all three soundproofing mechanisms simultaneously: blocking airborne sound, damping structural vibrations, and absorbing residual sound energy. The result is a panel system that significantly outperforms single-layer solutions of equivalent thickness.",
        "price": "From $85/m²",
        "image": "../images/akupanelcn/acoustic-screen-1.jpg",
        "features": [
            "Multi-layer engineered construction",
            "Combined blocking + damping + absorption",
            "Thin profile with high performance",
            "Constrained-layer damping technology",
            "No studs or resilient channels needed",
            "Residential and commercial grade options"
        ],
        "specs": {
            "Material": "MLV + viscoelastic damping + acoustic wool",
            "Thickness": "25mm, 40mm, 60mm",
            "Standard Sizes": "1200x600mm, 2400x1200mm",
            "STC Rating": "52-65 dB",
            "Fire Rating": "B1 / A2",
            "Density": "18-30 kg/m2",
            "Installation": "Direct mount or channel mount",
            "Application": "Walls, Floors, Ceilings"
        },
        "applications": "Recording studio walls, home theaters, podcast studios, commercial partitioning, industrial plant noise control",
        "keywords": "composite soundproof panels, multi-layer acoustic panels, sound blocking composite, acoustic composite board, engineered soundproofing"
    },
    {
        "slug": "acoustic-partition-walls",
        "filename": "acoustic-partition-walls.html",
        "name": "Movable Acoustic Partition Walls",
        "tagline": "Flexible, high-STC partition walls for dynamic space division",
        "description": "Movable Acoustic Partition Walls provide flexible space division with integrated acoustic performance. These floor-to-ceiling panel systems can be retracted, folded, or stacked to reconfigure spaces as needed while maintaining excellent sound isolation between areas. Perfect for hotel ballrooms, conference centers, office spaces, and any venue that requires adaptable acoustic separation.",
        "price": "From $180/m²",
        "image": "../images/akupanelcn/acoustic-window-1.jpg",
        "features": [
            "Floor-to-ceiling acoustic sealing",
            "Smooth retractable/fold operation",
            "High STC ratings for sound isolation",
            "Various surface finish options",
            "Single or double glazed options",
            "Top and bottom acoustic seals"
        ],
        "specs": {
            "Material": "Steel/Aluminum Frame + Acoustic Core",
            "Thickness": "80mm, 100mm, 120mm",
            "Height": "Up to 6000mm",
            "STC Rating": "45-55 dB",
            "Fire Rating": "B1 / A2",
            "Finish": "Fabric, Laminate, Wood, Glass",
            "Operation": "Manual or Motorized",
            "Application": "Interior Space Division"
        },
        "applications": "Hotel ballrooms, conference centers, office spaces, exhibition halls, banquet rooms, training centers",
        "keywords": "acoustic partition walls, movable walls, retractable acoustic walls, folding partition, space dividing panels, acoustic room dividers"
    },
    {
        "slug": "resilient-channel-systems",
        "filename": "resilient-channel-systems.html",
        "name": "Resilient Channel Soundproofing Systems",
        "tagline": "Decoupling technology for maximum sound isolation without mass addition",
        "description": "Resilient Channel Soundproofing Systems use resilient metal channels to mechanically decouple drywall from the structural framing. This decoupling interrupts sound vibration transfer through the wall structure, providing significantly improved sound isolation without adding excessive mass. Resilient channels are a foundational technique in professional soundproofing and work best when combined with acoustic insulation and multiple layers of drywall.",
        "price": "From $25/m²",
        "image": "../images/akupanelcn/wood-slat-1.jpg",
        "features": [
            "Mechanical decoupling of wall structure",
            "Breaks vibration transfer path",
            "Compatible with standard construction",
            "Cost-effective soundproofing solution",
            "Can achieve STC improvements of 10-15 dB",
            "No special tools required for installation"
        ],
        "specs": {
            "Material": "Galvanized Steel Resilient Channel",
            "Channel Width": "63mm",
            "Spacing": "400mm or 600mm center-to-center",
            "Stud Depth": "63mm (to match channel)",
            "STC Improvement": "+10 to +15 dB",
            "Fire Rating": "A1 (non-combustible)",
            "Installation": "Horizontal mount on studs",
            "Application": "Wall and Ceiling Decoupling"
        },
        "applications": "Home theaters, apartment walls, recording studios, commercial office partitions, mixed-use buildings",
        "keywords": "resilient channel, soundproofing channel, acoustic decoupling, resilient channel system, wall soundproofing, decoupling clips"
    },
    {
        "slug": "acoustic-plasterboard",
        "filename": "acoustic-plasterboard.html",
        "name": "Acoustic Plasterboard",
        "tagline": "High-density gypsum board with enhanced sound blocking properties",
        "description": "Acoustic Plasterboard is a specialized high-density gypsum board engineered for superior sound blocking in wall and ceiling construction. With a denser gypsum core than standard drywall, acoustic plasterboard provides improved mass and damping characteristics that reduce airborne sound transmission. It is the ideal choice for specifiers seeking simple, construction-grade acoustic performance without complex multi-layer assemblies.",
        "price": "From $28/sheet",
        "image": "../images/akupanelcn/acoustic-tile-1.jpg",
        "features": [
            "Higher density than standard drywall",
            "Easy to cut and install like regular plasterboard",
            "Improved STC performance per layer",
            "Compatible with standard framing systems",
            "Available in multiple thicknesses",
            "Suitable for new build and retrofit"
        ],
        "specs": {
            "Material": "High-Density Gypsum",
            "Thickness": "12.5mm, 15mm, 18mm",
            "Standard Size": "1200x2400mm",
            "Density": "12-16 kg/m2",
            "Fire Rating": "A2-s1, d0",
            "STC Rating": "35-42 dB per layer",
            "Finish": "Paper-faced, ready for decoration",
            "Application": "Walls and Ceilings"
        },
        "applications": "Internal walls, separating walls, ceiling systems, apartment partitions, school classroom walls, hotel guest room walls",
        "keywords": "acoustic plasterboard, soundproof drywall, high density gypsum board, acoustic gypsum, sound blocking board, acoustic wallboard"
    },
    {
        "slug": "marine-acoustic-panels",
        "filename": "marine-acoustic-panels.html",
        "name": "Marine Acoustic Panels",
        "tagline": "Moisture-resistant acoustic panels designed for marine environments",
        "description": "Marine Acoustic Panels are purpose-designed acoustic treatment products engineered for the unique challenges of marine environments — high humidity, salt spray, temperature extremes, and strict fire safety regulations. These panels utilize moisture-resistant cores, marine-grade finishes, and non-combustible or fire-retardant materials to deliver reliable acoustic performance on yachts, cruise ships, naval vessels, and offshore platforms.",
        "price": "From $95/m²",
        "image": "../images/akupanelcn/bass-trap-1.jpg",
        "features": [
            "Marine-grade moisture resistant construction",
            "Certified fire performance for vessels",
            "Salt spray and humidity resistant",
            "Lightweight to minimize vessel weight load",
            "IMO/SOLAS compliant fire ratings",
            "Marine bolt or adhesive mounting systems"
        ],
        "specs": {
            "Material": "Mineral Wool / Phenolic Foam + Marine GRP",
            "Thickness": "25mm, 50mm, 75mm",
            "Standard Sizes": "600x600mm, 1200x600mm",
            "Density": "40-80 kg/m3",
            "Fire Rating": "IMO A1/A2, SOLAS compliant",
            "NRC Rating": "0.80-0.95",
            "Moisture Resistance": "Up to 98% RH",
            "Application": "Walls and Ceilings on Vessels"
        },
        "applications": "Yachts, cruise ships, naval vessels, offshore oil platforms, maritime vessels, ferry boats, marine entertainment venues",
        "keywords": "marine acoustic panels, ship acoustic panels, nautical soundproofing, marine sound absorption, yacht acoustic treatment, maritime acoustic panels"
    },
    {
        "slug": "high-density-foam-panels",
        "filename": "high-density-foam-panels.html",
        "name": "High Density Acoustic Foam Panels",
        "tagline": "Premium studio-grade acoustic foam with enhanced bass absorption",
        "description": "High Density Acoustic Foam Panels are premium-grade studio treatment products featuring optimized cell structure for superior sound absorption across all frequencies, including low bass. Unlike standard acoustic foam, these high-density panels offer improved longevity, consistent performance, and better bass trapping capabilities. Available in wedge, pyramid, and egg-crate profiles to suit different aesthetic and acoustic requirements.",
        "price": "From $42/m²",
        "image": "../images/akupanelcn/concertina-foam-1.jpg",
        "features": [
            "High-density foam for extended frequency absorption",
            "Enhanced bass and low-frequency performance",
            "Multiple surface profile options",
            "Self-supporting, no framework needed",
            "Lightweight with easy wall mounting",
            "Premium-grade durability and longevity"
        ],
        "specs": {
            "Material": "High-Density Polyurethane Foam",
            "Thickness": "50mm, 75mm, 100mm",
            "Standard Sizes": "600x600mm, 1200x600mm",
            "Density": "30-45 kg/m3",
            "Fire Rating": "B1 / CA117",
            "NRC Rating": "0.80-0.95",
            "Profile Options": "Wedge, Pyramid, Egg-crate, Sonex",
            "Application": "Walls"
        },
        "applications": "Recording studios, mixing rooms, mastering suites, podcast studios, voice-over booths, rehearsal rooms, drum rooms",
        "keywords": "high density acoustic foam, studio foam panels, bass absorbing foam, acoustic foam wedges, pyramid foam panels, sound foam panels"
    },
    {
        "slug": "industrial-soundproof-panels",
        "filename": "industrial-soundproof-panels.html",
        "name": "Industrial Soundproof Enclosure Panels",
        "tagline": "Heavy-duty modular panels for industrial noise containment and machine enclosures",
        "description": "Industrial Soundproof Enclosure Panels are heavy-duty, modular acoustic panels designed for noise containment in industrial settings. These panels feature thick, dense cores with robust outer skins that withstand the demanding conditions of factories, power plants, compressor rooms, and mechanical spaces. The modular design allows for custom enclosure configurations around machinery, equipment rooms, and noisy operational areas.",
        "price": "From $120/m²",
        "image": "../images/akupanelcn/echo-absorber-1.jpg",
        "features": [
            "Heavy-duty industrial-grade construction",
            "Thick cores for maximum noise reduction",
            "Weather and impact resistant outer skins",
            "Modular for custom enclosure designs",
            "Ventilation and access panel options",
            "Quick-install bolt-together frame system"
        ],
        "specs": {
            "Material": "Concrete/Steel Composite + Dense Core",
            "Thickness": "50mm, 75mm, 100mm, 150mm",
            "Panel Size": "600x600mm, 600x1200mm",
            "Noise Reduction": "25-45 dB",
            "Fire Rating": "A1 / Plywood mineral",
            "Density": "80-200 kg/m3",
            "Weather Resistance": "IP55 rated options",
            "Application": "Industrial Enclosures and Machine Housing"
        },
        "applications": "Factory machine enclosures, compressor rooms, power plant noise control, data center noise reduction, generator housings, industrial HVAC noise barriers",
        "keywords": "industrial soundproof panels, machine enclosure panels, noise control panels, industrial acoustic panels, heavy duty acoustic panels, factory soundproofing"
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
                    <span class="logo-icon">&#128263;</span>
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

print(f'\nTotal: {len(products)} product pages created!')
