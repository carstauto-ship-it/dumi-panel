#!/usr/bin/env python3
"""
Simple product page generator for acoustic website
"""

import os

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
    }
]

# Template for product pages
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Professional Acoustic Solutions</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{id}, acoustic panels, soundproofing, noise reduction">
    
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
    <section class="product-detail" style="padding: 60px 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; margin-bottom: 60px;">
                <div>
                    <img src="../images/{id}.jpg" alt="{title}" style="width: 100%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                </div>
                <div>
                    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: #2c3e50;">{title}</h1>
                    <p style="font-size: 1.2rem; color: #7f8c8d; margin-bottom: 30px;">{description}</p>
                    
                    <div style="font-size: 2rem; font-weight: 700; color: #e74c3c; margin-bottom: 30px;">{price}</div>
                    
                    <div style="margin: 30px 0;">
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span>High-quality acoustic performance</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span>Custom sizes and finishes available</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span>Easy installation options</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span>Professional technical support</span>
                        </div>
                    </div>
                    
                    <a href="../index.html#contact" class="cta-button" style="display: inline-block; margin-top: 20px;">Request Quote</a>
                </div>
            </div>

            <!-- Specifications -->
            <div style="background: #ecf0f1; padding: 40px; border-radius: 10px; margin-bottom: 60px;">
                <h2 style="margin-bottom: 30px; color: #2c3e50;">Technical Specifications</h2>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                    <div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">Material</div>
                        <div style="margin-top: 5px;">{material}</div>
                    </div>
                    <div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">Thickness</div>
                        <div style="margin-top: 5px;">{thickness}</div>
                    </div>
                    <div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">Standard Sizes</div>
                        <div style="margin-top: 5px;">{sizes}</div>
                    </div>
                    <div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">Finish</div>
                        <div style="margin-top: 5px;">{finish}</div>
                    </div>
                    {fire_rating_spec}
                    {nrc_spec}
                    {stc_spec}
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
                    <p>WeChat: +86-13001727017</p>
                    <p>WhatsApp: +61493342108</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Professional Acoustic Panels Manufacturer. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

# Generate product pages
for product in products:
    # Prepare spec sections
    fire_rating_spec = ''
    if 'fire_rating' in product:
        fire_rating_spec = f'''<div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">Fire Rating</div>
                        <div style="margin-top: 5px;">{product['fire_rating']}</div>
                    </div>'''
    
    nrc_spec = ''
    if 'nrc' in product:
        nrc_spec = f'''<div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">NRC Rating</div>
                        <div style="margin-top: 5px;">{product['nrc']}</div>
                    </div>'''
    
    stc_spec = ''
    if 'stc_rating' in product:
        stc_spec = f'''<div style="padding: 15px; background: white; border-radius: 5px;">
                        <div style="font-weight: 600; color: #2c3e50;">STC Rating</div>
                        <div style="margin-top: 5px;">{product['stc_rating']}</div>
                    </div>'''
    
    # Format template
    html = template.format(
        title=product['title'],
        description=product['description'],
        id=product['id'],
        price=product['price'],
        material=product['material'],
        thickness=product['thickness'],
        sizes=product['sizes'],
        finish=product['finish'],
        fire_rating_spec=fire_rating_spec,
        nrc_spec=nrc_spec,
        stc_spec=stc_spec
    )
    
    # Write to file
    filename = f"acoustic-website/products/{product['id']}.html"
    with open(filename, 'w') as f:
        f.write(html)
    
    print(f"Generated: {filename}")

print("\nAll product pages generated successfully!")