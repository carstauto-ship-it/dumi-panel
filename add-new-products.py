#!/usr/bin/env python3
"""Add new acoustic panel products"""

new_products = [
    {
        "id": "fabric-acoustic-panels",
        "title": "Fabric Wrapped Acoustic Panels",
        "description": "Premium fabric-wrapped panels with high-density acoustic core. Professional-grade sound absorption for offices, studios, and public spaces.",
        "price": "From $40/m²",
        "material": "Glass Wool Core + Acoustic Fabric",
        "thickness": "25mm, 50mm, 75mm",
        "sizes": "600x600mm, 1200x600mm, 2400x1200mm",
        "finish": "Guilford of Maine, Camira fabrics, custom colors",
        "fire_rating": "A2 (non-combustible)",
        "nrc": "0.80-0.95",
        "features": [
            "Premium acoustic fabric finishes",
            "High-density glass wool core",
            "Professional studio quality",
            "Custom sizes and shapes",
            "Easy installation with concealed clips"
        ],
        "applications": ["Recording studios", "Home theaters", "Conference rooms", "Offices", "Auditoriums", "Restaurants"]
    },
    {
        "id": "perforated-metal-panels",
        "title": "Perforated Metal Acoustic Panels",
        "description": "Metal panels with precision perforations and acoustic backing. Industrial aesthetic with superior sound control for high-traffic areas.",
        "price": "From $55/m²",
        "material": "Galvanized Steel + Acoustic Fleece",
        "thickness": "15mm, 25mm, 50mm",
        "sizes": "600x600mm, 1200x600mm, custom",
        "finish": "Powder coated RAL colors, natural metal",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.70-0.90",
        "features": [
            "Durable metal construction",
            "Precision laser perforations",
            "Wide range of perforation patterns",
            "Corrosion resistant",
            "Modern industrial look"
        ],
        "applications": ["Shopping malls", "Sports facilities", "Transit stations", "Industrial buildings", "Public buildings"]
    },
    {
        "id": "micropore-acoustic-panels",
        "title": "Micropore Acoustic Panels",
        "description": "Ultra-thin microperforated panels with innovative pore technology. Perfect for space-constrained applications without compromising acoustic performance.",
        "price": "From $65/m²",
        "material": "Microperforated Polymer Composite",
        "thickness": "8mm, 12mm, 18mm",
        "sizes": "600x600mm, 1200x600mm",
        "finish": "White, black, custom colors",
        "fire_rating": "B1",
        "nrc": "0.60-0.85",
        "features": [
            "Ultra-thin profile",
            "Microperforation technology",
            "Sleek modern appearance",
            "Lightweight construction",
            "Ideal for limited space"
        ],
        "applications": ["Elevators", "Clean rooms", "Compact offices", "Medical facilities", "Libraries"]
    },
    {
        "id": "echo-absorbers",
        "title": "Echo Absorbers & Baffles",
        "description": "Suspended ceiling baffles and floating absorbers for comprehensive echo control in large spaces with high ceilings.",
        "price": "From $45/unit",
        "material": "High-density Mineral Wool",
        "thickness": "100mm, 150mm, 200mm",
        "sizes": "600x1200mm, 1200x2400mm",
        "finish": "Fabric wrapped, painted",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.85-1.00",
        "features": [
            "Suspended installation",
            "Maximum sound absorption",
            "Minimal ceiling obstruction",
            "Various hanging configurations",
            "Ideal for echo reduction"
        ],
        "applications": ["Gyms", "Swimming pools", "Atriums", "Warehouses", "Churches", "Event halls"]
    },
    {
        "id": "sound-diffusers",
        "title": "Acoustic Sound Diffusers",
        "description": "MLS and quadratic residue diffusers for balanced acoustic treatment. Scatters sound energy evenly for natural, live-sounding rooms.",
        "price": "From $75/unit",
        "material": "MDF, Solid Wood, Polymer",
        "thickness": "50mm, 100mm, 150mm",
        "sizes": "600x600mm, 1200x600mm",
        "finish": "Natural wood, painted, laminated",
        "fire_rating": "B1",
        "nrc": "0.50-0.70 (scattering)",
        "features": [
            "Proprietary diffuser designs",
            "Balanced frequency diffusion",
            "Premium wood finishes",
            "Wall and ceiling mountable",
            "Professional studio grade"
        ],
        "applications": ["Recording studios", "Broadcast rooms", "Concert halls", "Home theaters", "Practice rooms"]
    },
    {
        "id": "concertina-foam-panels",
        "title": "Concertina Foam Panels",
        "description": "Classic accordion-style acoustic foam panels. Cost-effective solution for music rooms, podcast studios, and vocal booths.",
        "price": "From $18/m²",
        "material": "High-density Polyurethane Foam",
        "thickness": "30mm, 50mm, 75mm",
        "sizes": "300x300mm, 600x600mm",
        "finish": "Graphite, charcoal, beige",
        "fire_rating": "B1",
        "nrc": "0.65-0.85",
        "features": [
            "Classic wedge profile",
            "Budget-friendly option",
            "Easy self-adhesive installation",
            "Lightweight and flexible",
            "Ideal for vocal treatment"
        ],
        "applications": ["Home studios", "Podcast booths", "Vocal booths", "Gaming setups", "Music practice rooms"]
    },
    {
        "id": "stretch-fabric-ceiling",
        "title": "Stretch Fabric Ceiling Systems",
        "description": "Tensioned fabric ceiling with acoustic insulation backing. Seamless appearance with excellent sound absorption and design flexibility.",
        "price": "From $50/m²",
        "material": "PVC-Free Stretch Fabric + Acoustic Pad",
        "thickness": "20mm, 30mm, 50mm",
        "sizes": "Custom dimensions",
        "finish": "Matte, satin, perforated fabrics",
        "fire_rating": "B1",
        "nrc": "0.75-0.90",
        "features": [
            "Seamless ceiling appearance",
            "Infinite design possibilities",
            "Integrated acoustic padding",
            "Quick installation",
            "Easy maintenance and cleaning"
        ],
        "applications": ["Hotels", "Restaurants", "Spas", "Offices", "Retail showrooms", "Residential"]
    }
]

def generate_html(product):
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
        .product-detail {{ padding: 60px 0; }}
        .product-header {{ display: grid; grid-template-columns: 1fr 1fr; gap: 50px; margin-bottom: 60px; }}
        .product-gallery img {{ width: 100%; border-radius: 10px; box-shadow: var(--shadow); }}
        .product-specs {{ background: var(--light-color); padding: 40px; border-radius: 10px; }}
        .specs-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 20px; }}
        .spec-item {{ padding: 15px; background: white; border-radius: 5px; }}
        .spec-label {{ font-weight: 600; color: var(--primary-color); }}
        .spec-value {{ margin-top: 5px; }}
        .features-list {{ margin: 30px 0; }}
        .feature-item {{ display: flex; align-items: flex-start; margin-bottom: 15px; }}
        .feature-icon {{ color: var(--secondary-color); margin-right: 10px; margin-top: 3px; }}
        .applications-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 30px; }}
        .application-item {{ text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: var(--shadow); }}
        @media (max-width: 768px) {{ .product-header {{ grid-template-columns: 1fr; }} .specs-grid {{ grid-template-columns: 1fr; }} }}
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
                    <img src="../images/{product['id']}.jpg" alt="{product['title']}" onerror="this.src='../images/placeholder.jpg'">
                </div>
                <div class="product-info">
                    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: var(--primary-color);">{product['title']}</h1>
                    <p style="font-size: 1.2rem; color: var(--text-light); margin-bottom: 30px;">{product['description']}</p>
                    <div class="product-price" style="font-size: 2rem; margin-bottom: 30px; color: var(--primary-color);">{product['price']}</div>
                    <div class="features-list">'''

    for feature in product['features']:
        html += f'''
                        <div class="feature-item">
                            <span class="feature-icon">✓</span>
                            <span>{feature}</span>
                        </div>'''

    html += f'''
                    </div>
                    <a href="../index.html#contact" class="cta-button" style="display: inline-block; margin-top: 20px; padding: 15px 30px; background: var(--primary-color); color: white; text-decoration: none; border-radius: 5px;">Request Quote</a>
                </div>
            </div>

            <!-- Product Specifications -->
            <div class="product-specs">
                <h2 style="margin-bottom: 30px; color: var(--primary-color);">Technical Specifications</h2>
                <div class="specs-grid">
                    <div class="spec-item"><div class="spec-label">Material</div><div class="spec-value">{product['material']}</div></div>
                    <div class="spec-item"><div class="spec-label">Thickness</div><div class="spec-value">{product['thickness']}</div></div>
                    <div class="spec-item"><div class="spec-label">Standard Sizes</div><div class="spec-value">{product['sizes']}</div></div>
                    <div class="spec-item"><div class="spec-label">Finish</div><div class="spec-value">{product['finish']}</div></div>
                    <div class="spec-item"><div class="spec-label">Fire Rating</div><div class="spec-value">{product['fire_rating']}</div></div>
                    <div class="spec-item"><div class="spec-label">NRC Rating</div><div class="spec-value">{product['nrc']}</div></div>
                </div>
            </div>

            <!-- Applications -->
            <div style="margin: 60px 0;">
                <h2 style="margin-bottom: 30px; color: var(--primary-color);">Recommended Applications</h2>
                <div class="applications-grid">'''

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
            <div style="text-align: center; margin: 60px 0; padding: 40px; background: var(--light-color); border-radius: 10px;">
                <h2 style="margin-bottom: 20px; color: var(--primary-color);">Ready to Order?</h2>
                <p style="margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto;">Contact us for custom sizes, colors, and bulk pricing. We offer worldwide shipping and technical support.</p>
                <a href="../index.html#contact" class="cta-button" style="display: inline-block; padding: 15px 30px; background: var(--primary-color); color: white; text-decoration: none; border-radius: 5px;">Contact Us Now</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>AcousticPro</h3>
                    <p>Professional acoustic solutions for noise control and sound absorption.</p>
                </div>
                <div class="footer-section">
                    <h3>Products</h3>
                    <ul class="footer-links">
                        <li><a href="pet-acoustic-panels.html">PET Acoustic Panels</a></li>
                        <li><a href="wood-slat-panels.html">Wood Slat Panels</a></li>
                        <li><a href="3d-acoustic-panels.html">3D Acoustic Panels</a></li>
                        <li><a href="fabric-acoustic-panels.html">Fabric Wrapped Panels</a></li>
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
                    <p>We ship worldwide</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 AcousticPro. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    return html

if __name__ == "__main__":
    import os
    os.makedirs("products", exist_ok=True)
    
    for product in new_products:
        html = generate_html(product)
        filepath = f"products/{product['id']}.html"
        with open(filepath, 'w') as f:
            f.write(html)
        print(f"Created: {filepath}")
    
    print(f"\nTotal new products added: {len(new_products)}")
