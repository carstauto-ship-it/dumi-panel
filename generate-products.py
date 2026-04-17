#!/usr/bin/env python3
"""
Product page generator for acoustic website
"""

import os
from pathlib import Path

# Product data
products = [
    {
        "id": "wood-slat-panels",
        "title": "Wood Slat Panels (Akupanel)",
        "description": "Combination of PET felt backing with MDF wood slats. Aesthetic design with functional acoustic performance.",
        "price": "From $35/m²",
        "material": "PET Felt + MDF Wood Slats",
        "thickness": "25mm, 38mm, 50mm",
        "sizes": "Various sizes up to 3000x1200mm",
        "finish": "Natural wood, painted finishes",
        "fire_rating": "B1",
        "nrc": "0.70-0.85",
        "features": [
            "Aesthetic wood slat design",
            "Combines acoustic and visual appeal",
            "Easy installation options",
            "Customizable slat widths (19mm, 28mm, 45mm)",
            "Sustainable materials"
        ],
        "applications": ["Office spaces", "Hotel lobbies", "Restaurants", "Retail stores", "Residential interiors"]
    },
    {
        "id": "3d-acoustic-panels",
        "title": "3D Acoustic Wall Panels",
        "description": "3D geometric design with built-in air cavities for enhanced sound absorption and visual appeal.",
        "price": "From $45/m²",
        "material": "High-density Polyurethane Foam",
        "thickness": "25mm, 50mm, 75mm",
        "sizes": "600x600mm, 1200x600mm",
        "finish": "Various colors and patterns",
        "fire_rating": "B1",
        "nrc": "0.75-0.90",
        "features": [
            "3D geometric patterns",
            "Enhanced sound diffusion",
            "Lightweight and easy to install",
            "Custom designs available",
            "Paintable surface"
        ],
        "applications": ["Recording studios", "Home theaters", "Conference rooms", "Restaurants", "Creative spaces"]
    },
    {
        "id": "acoustic-ceiling",
        "title": "Acoustic Ceiling Panels",
        "description": "Suspended ceiling systems for comprehensive room acoustic treatment and noise control.",
        "price": "From $30/m²",
        "material": "Mineral Fiber, Metal",
        "thickness": "15mm, 20mm, 25mm",
        "sizes": "600x600mm, 600x1200mm",
        "finish": "White, custom colors",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.60-0.90",
        "features": [
            "Suspended grid system",
            "Easy access to ceiling space",
            "Integrated lighting options",
            "High sound absorption",
            "Moisture resistant options"
        ],
        "applications": ["Offices", "Schools", "Hospitals", "Shopping malls", "Airports"]
    },
    {
        "id": "acoustic-screens",
        "title": "Acoustic Screens & Partitions",
        "description": "Freestanding screens and partitions for flexible space division and noise reduction in open offices.",
        "price": "From $150/unit",
        "material": "Wood Frame with Acoustic Fabric",
        "thickness": "50mm, 75mm, 100mm",
        "sizes": "Various heights (1200-1800mm)",
        "finish": "Fabric wrapped, wood veneer",
        "fire_rating": "B1",
        "nrc": "0.70-0.85",
        "features": [
            "Freestanding and mobile",
            "Easy to reposition",
            "Cable management options",
            "Whiteboard surfaces available",
            "Custom sizes and fabrics"
        ],
        "applications": ["Open-plan offices", "Call centers", "Co-working spaces", "Healthcare facilities", "Educational settings"]
    },
    {
        "id": "acoustic-tiles",
        "title": "Acoustic Wall Tiles",
        "description": "Modular wall tiles for easy installation and customizable acoustic treatment patterns.",
        "price": "From $20/m²",
        "material": "PET, Fabric, Wood",
        "thickness": "20mm, 30mm",
        "sizes": "300x300mm, 600x600mm",
        "finish": "Various fabrics and finishes",
        "fire_rating": "B1",
        "nrc": "0.65-0.80",
        "features": [
            "Modular design",
            "Easy to install and replace",
            "Create custom patterns",
            "Wide range of colors",
            "Affordable solution"
        ],
        "applications": ["Home offices", "Studios", "Restaurants", "Hotels", "Retail spaces"]
    },
    {
        "id": "acoustic-lighting",
        "title": "Acoustic Lighting Panels",
        "description": "Combined lighting and acoustic panels for multifunctional ceiling solutions.",
        "price": "From $60/panel",
        "material": "PET with Integrated LED",
        "thickness": "30mm",
        "sizes": "600x600mm, 300x1200mm",
        "finish": "White diffuser",
        "fire_rating": "B1",
        "nrc": "0.70-0.85",
        "features": [
            "Integrated LED lighting",
            "Energy efficient",
            "Dimmable options",
            "Easy maintenance",
            "Combined function"
        ],
        "applications": ["Offices", "Conference rooms", "Educational facilities", "Healthcare", "Retail"]
    },
    {
        "id": "bass-traps",
        "title": "Bass Traps & Corner Absorbers",
        "description": "Specialized acoustic treatment for low-frequency absorption in corners and room boundaries.",
        "price": "From $80/unit",
        "material": "High-density Mineral Wool",
        "thickness": "200mm, 300mm, 400mm",
        "sizes": "Various corner sizes",
        "finish": "Fabric wrapped",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.80-0.95 (low frequencies)",
        "features": [
            "Targets low frequencies",
            "Corner and wall mounting",
            "Effective room mode control",
            "Professional studio quality",
            "Custom sizes available"
        ],
        "applications": ["Recording studios", "Home theaters", "Control rooms", "Practice rooms", "Broadcast studios"]
    },
    {
        "id": "acoustic-doors",
        "title": "Acoustic Doors",
        "description": "Soundproof doors with high STC ratings for studios, offices, and noise-sensitive areas.",
        "price": "From $500/door",
        "material": "Solid Core with Seals",
        "thickness": "45mm, 55mm, 65mm",
        "sizes": "Standard door sizes",
        "finish": "Various wood veneers and paints",
        "stc_rating": "35-45 dB",
        "features": [
            "Magnetic perimeter seals",
            "Automatic door bottoms",
            "Heavy-duty hardware",
            "Fire rated options",
            "Custom sizes and finishes"
        ],
        "applications": ["Recording studios", "Server rooms", "Medical facilities", "Office meeting rooms", "Home theaters"]
    },
    {
        "id": "acoustic-windows",
        "title": "Acoustic Windows",
        "description": "Double/triple glazed windows with acoustic laminated glass for noise reduction.",
        "price": "From $300/m²",
        "material": "Laminated Glass with Air Gap",
        "thickness": "24mm, 32mm, 40mm",
        "sizes": "Custom sizes",
        "finish": "Aluminum or uPVC frames",
        "stc_rating": "35-45 dB",
        "features": [
            "Acoustic laminated glass",
            "Thermal break frames",
            "Weather sealing",
            "UV protection",
            "Custom configurations"
        ],
        "applications": ["Urban residences", "Office buildings", "Hotels", "Hospitals", "Schools near roads"]
    }
]

def generate_product_html(product):
    """Generate HTML for a product page"""
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product['title']} | Professional Acoustic Solutions</title>
    <meta name="description" content="{product['description']}">
    <meta name="keywords" content="{product['id'].replace('-', ' ')}, acoustic panels, soundproofing, noise reduction">
    
    <link rel="stylesheet" href="../css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .product-detail {{
            padding: 60px 0;
        }}
        .product-header {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin-bottom: 60px;
        }}
        .product-gallery img {{
            width: 100%;
            border-radius: 10px;
            box-shadow: var(--shadow);
        }}
        .product-specs {{
            background: var(--light-color);
            padding: 40px;
            border-radius: 10px;
        }}
        .specs-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 20px;
        }}
        .spec-item {{
            padding: 15px;
            background: white;
            border-radius: 5px;
        }}
        .spec-label {{
            font-weight: 600;
            color: var(--primary-color);
        }}
        .spec-value {{
            margin-top: 5px;
        }}
        .features-list {{
            margin: 30px 0;
        }}
        .feature-item {{
            display: flex;
            align-items: flex-start;
            margin-bottom: 15px;
        }}
        .feature-icon {{
            color: var(--secondary-color);
            margin-right: 10px;
            margin-top: 3px;
        }}
        .applications-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .application-item {{
            text-align: center;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: var(--shadow);
        }}
        @media (max-width: 768px) {{
            .product-header {{
                grid-template-columns: 1fr;
            }}
            .specs-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header" id="header">
        <div class="container">
            <div class="header-inner">
                <a href="../index.html" class="logo">
                    <span class="logo-icon">🔇</span>
                    <div class="logo-text">
                        <span class="logo-brand">ACOUSTICPRO</span>
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
    <section class="product-detail">
        <div class="container">
            <div class="product-header">
                <div class="product-gallery">
                    <img src="../images/{product['id']}.jpg" alt="{product['title']}">
                </div>
                <div class="product-info">
                    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: var(--primary-color);">{product['title']}</h1>
                    <p style="font-size: 1.2rem; color: var(--text-light); margin-bottom: 30px;">{product['description']}</p>
                    
                    <div class="product-price" style="font-size: 2rem; margin-bottom: 30px;">{product['price']}</div>
                    
                    <div class="features-list">'''

    # Add features
    for feature in product['features']:
        html += f'''
                        <div class="feature-item">
                            <span class="feature-icon">✓</span>
                            <span>{feature}</span>
                        </div>'''

    html += f'''
                    </div>
                    
                    <a href="../index.html#contact" class="cta-button" style="display: inline-block; margin-top: 20px;">Request Quote</a>
                </div>
            </div>

            <!-- Product Specifications -->
            <div class="product-specs">
                <h2 style="margin-bottom: 30px; color: var(--primary-color);">Technical Specifications</h2>
                <div class="specs-grid">'''

    # Add specifications
    specs = [
        ("Material", product.get('material', 'Various acoustic materials')),
        ("Thickness", product.get('thickness', 'Custom thickness available')),
        ("Standard Sizes", product.get('sizes', 'Custom sizes available')),
        ("Finish", product.get('finish', 'Various finishes available')),
    ]
    
    if 'fire_rating' in product:
        specs.append(("Fire Rating", product['fire_rating']))
    
    if 'nrc' in product:
        specs.append(("NRC Rating", product['nrc']))
    
    if 'stc_rating' in product:
        specs.append(("STC Rating", product['stc_rating']))
    
    for label, value in specs:
        html += f'''
                    <div class="spec-item">
                        <div class="spec-label">{label}</div>
                        <div class="spec-value">{value}</div>
                    </div>'''

    html += f'''
                </div>
            </div>

            <!-- Applications -->
            <div style="margin: 60px 0;">
                <h2 style="margin-bottom: 30px; color: var(--primary-color);">Recommended Applications</h2>
                <div class="applications-grid">'''

    # Add applications
    for app in product['applications']:
        html += f'''
                    <div class="application-item">
                        <div style="font-size: 1.5rem; margin-bottom: 15px;">✓</div>
                        <h3>{app}</h3>
                    </div>'''

    html += f'''
                </div>
            </div>

            <!-- CTA -->
            <div style="text-align: center; margin: 60px 0;">
                <h2 style="margin-bottom: 20px; color: var(--primary-color);">Ready to Order?</h2>
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
                    <h3>AcousticPro</h3>
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
                    <p>Email: carter@soundproof-panel.com.cn</p>
                    <p>