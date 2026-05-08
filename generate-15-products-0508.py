#!/usr/bin/env python3
"""
Batch Generate 15 Acoustic Panel Products for dumi-panel.com
Date: 2026-05-08
"""

import os
import re

PRODUCTS_DIR = "/Users/carstauto/.openclaw/workspace/dumi-panel/products"
BASE_URL = "https://dumi-panel.com"

# 15 New Acoustic Panel Products
products = [
    {
        "id": "echo-absorbing-wall-panels",
        "name": "Echo Absorbing Wall Panels",
        "title": "Echo Absorbing Wall Panels | Studio Acoustic Treatment | DUMI",
        "description": "Professional echo absorbing wall panels for studios, home theaters, and commercial spaces. High-density acoustic foam provides superior sound absorption. Easy wall mount installation.",
        "keywords": "echo absorbing panels, acoustic wall panels, sound absorbing panels, studio wall panels, wall acoustic treatment",
        "h2_features": "High-Density Acoustic Foam | NRC 0.85+ | Easy Wall Mount | Fire Retardant",
        "price": "From $45/piece",
        "specs": "24\"x24\"x2\" | 48\"x48\"x2\" | Custom sizes available",
        "applications": "Recording Studios | Home Theaters | Conference Rooms | Restaurants"
    },
    {
        "id": "studio-velcro-acoustic-panels",
        "name": "Studio Velcro Acoustic Panels",
        "title": "Studio Velcro Acoustic Panels | Removable Sound Panels | DUMI",
        "description": "Innovative velcro-attached acoustic panels for easy removal and repositioning. Perfect for rental spaces and temporary installations. Reusable adhesive backing.",
        "keywords": "velcro acoustic panels, removable acoustic panels, studio panels, temporary sound treatment, reusable acoustic panels",
        "h2_features": "Velcro Attachment System | Reusable | Portable | No-Drill Installation",
        "price": "From $55/piece",
        "specs": "24\"x24\"x2\" | 24\"x48\"x2\" | Multiple colors",
        "applications": "Rental Studios | Practice Rooms | Home Studios | Temporary Events"
    },
    {
        "id": "hanging-acoustic-baffles-vertical",
        "name": "Vertical Hanging Acoustic Baffles",
        "title": "Vertical Hanging Acoustic Baffles | Ceiling Sound Absorbers | DUMI",
        "description": "Vertical hanging acoustic baffles for gymnasiums, swimming pools, and large open spaces. Effective ceiling-mounted sound absorption solution.",
        "keywords": "hanging acoustic baffles, vertical baffles, ceiling baffles, gym acoustics, pool acoustics, industrial sound absorption",
        "h2_features": "Vertical Design | Chain Hanging System | Weather Resistant | High NRC 0.90",
        "price": "From $120/piece",
        "specs": "48\"L x 12\"W x 3\"D | 72\"L x 12\"W x 3\"D",
        "applications": "Gymnasiums | Swimming Pools | Warehouses | Atriums"
    },
    {
        "id": "art-acoustic-panels-framed",
        "name": "Framed Art Acoustic Panels",
        "title": "Framed Art Acoustic Panels | Decorative Sound Panels | DUMI",
        "description": "Combine acoustics with art - custom printed framed acoustic panels. Available with your artwork or our design templates. Dual function: decoration + sound absorption.",
        "keywords": "art acoustic panels, decorative acoustic panels, framed sound panels, custom print acoustic, acoustic art panels",
        "h2_features": "Custom Art Printing | Framed Design | NRC 0.75+ | Multiple Frame Styles",
        "price": "From $89/piece",
        "specs": "24\"x24\" | 32\"x32\" | 40\"x40\" | Custom sizes",
        "applications": "Home Studios | Offices | Restaurants | Listening Rooms"
    },
    {
        "id": "outdoor-acoustic-panels-weatherproof",
        "name": "Weatherproof Outdoor Acoustic Panels",
        "title": "Weatherproof Outdoor Acoustic Panels | Exterior Sound Barriers | DUMI",
        "description": "UV-resistant and weatherproof acoustic panels designed for outdoor use. Ideal for patios, outdoor venues, and building facades. All-weather performance.",
        "keywords": "outdoor acoustic panels, weatherproof panels, exterior acoustic, outdoor sound barrier, patio acoustic panels",
        "h2_features": "UV Resistant | Waterproof | Temperature Tolerant | Salt Spray Rated",
        "price": "From $95/piece",
        "specs": "24\"x48\"x2\" | 48\"x48\"x2\" | Custom outdoor sizes",
        "applications": "Outdoor Patios | Pool Areas | Stadium Seating | Building Facades"
    },
    {
        "id": "acoustical-sound-masking-panels",
        "name": "Sound Masking Acoustic Panels",
        "title": "Sound Masking Panels | Privacy Acoustic Solutions | DUMI",
        "description": "Sound masking panels for office privacy and speech intelligibility control. Reduce distracting conversations while maintaining comfortable ambient noise levels.",
        "keywords": "sound masking panels, privacy acoustic, office acoustic panels, speech privacy, ambient sound control",
        "h2_features": "Speech Privacy | Ambient Sound Control | Office Acoustic | Open Plan Solutions",
        "price": "From $65/piece",
        "specs": "24\"x24\"x1\" | 24\"x48\"x1\" | 48\"x48\"x1\"",
        "applications": "Open Offices | Medical Facilities | Legal Offices | Banks"
    },
    {
        "id": "broadcast-studio-acoustic-treatment-kit",
        "name": "Broadcast Studio Acoustic Treatment Kit",
        "title": "Broadcast Studio Acoustic Treatment Kit | Professional Studio Package | DUMI",
        "description": "Complete acoustic treatment kit for broadcast studios and podcast rooms. Includes wall panels, bass traps, and ceiling treatment. Professional grade.",
        "keywords": "broadcast studio kit, podcast room acoustic, radio studio treatment, streaming room panels, professional studio acoustics",
        "h2_features": "Complete Kit | Wall + Ceiling + Corners | Professional Grade | Easy Install",
        "price": "From $599/kit",
        "specs": "Small (8 pieces) | Medium (16 pieces) | Large (24 pieces)",
        "applications": "Broadcast Studios | Podcast Rooms | Radio Stations | Twitch Streaming"
    },
    {
        "id": "motorized-acoustic-panel-system",
        "name": "Motorized Acoustic Panel System",
        "title": "Motorized Acoustic Panel System | Automated Sound Control | DUMI",
        "description": "Revolutionary motorized acoustic panels that adjust automatically based on room usage. Smart home integration. Remote control or app-controlled sound environments.",
        "keywords": "motorized acoustic panels, automated sound control, smart acoustic, motorized panels, adjustable acoustics",
        "h2_features": "Motorized Adjustment | App Control | Smart Home Integration | Variable Absorption",
        "price": "From $299/piece",
        "specs": "24\"x48\" | 48\"x48\" | WiFi + Manual Control",
        "applications": "Home Theaters | Multi-Purpose Rooms | Smart Homes | Luxury Studios"
    },
    {
        "id": "recycled-pet-acoustic-panels",
        "name": "Recycled PET Acoustic Panels",
        "title": "Recycled PET Acoustic Panels | Eco-Friendly Sound Absorption | DUMI",
        "description": "Sustainable acoustic panels made from 100% recycled PET bottles. Eco-friendly alternative with excellent sound absorption. Available in various colors and patterns.",
        "keywords": "recycled PET acoustic panels, eco acoustic panels, sustainable sound absorption, green building materials, recycled acoustic foam",
        "h2_features": "100% Recycled PET | Eco-Friendly | Color Options | NRC 0.80+",
        "price": "From $49/piece",
        "specs": "24\"x24\"x1\" | 48\"x24\"x1\" | 48\"x48\"x1\"",
        "applications": "Green Buildings | Eco Studios | Schools | LEED Projects"
    },
    {
        "id": "aerospace-composite-acoustic-panels",
        "name": "Aerospace Composite Acoustic Panels",
        "title": "Aerospace Composite Acoustic Panels | High-Performance Soundproofing | DUMI",
        "description": "Premium acoustic panels using aerospace-grade composite materials. Exceptional sound transmission loss (STC 45+). For professional recording and broadcast applications.",
        "keywords": "aerospace acoustic panels, composite soundproofing, high performance acoustic, STC rated panels, professional sound isolation",
        "h2_features": "STC 45+ Rating | Aerospace Materials | Maximum Isolation | Professional Grade",
        "price": "From $149/piece",
        "specs": "24\"x48\"x3\" | 48\"x48\"x4\" | Custom configurations",
        "applications": "Professional Studios | Broadcast Booths | Film Scoring Stages | Concert Halls"
    },
    {
        "id": "magnetic-mount-acoustic-panels",
        "name": "Magnetic Mount Acoustic Panels",
        "title": "Magnetic Mount Acoustic Panels | Quick-Install Sound Panels | DUMI",
        "description": "Revolutionary magnetic mounting system for quick and easy acoustic panel installation. No adhesive, no drilling. Steel backing plate included. Perfect for temporary setups.",
        "keywords": "magnetic mount acoustic panels, quick install acoustic, steel backing panels, magnetic sound panels, tool-free acoustic installation",
        "h2_features": "Magnetic Mounting | No Drilling | Steel Backing Included | Repositionable",
        "price": "From $59/piece",
        "specs": "24\"x24\"x2\" | 24\"x48\"x2\" | Multiple colors",
        "applications": "Temporary Studios | Apartment Studios | Rental Spaces | Trade Shows"
    },
    {
        "id": "chevron-pattern-acoustic-panels",
        "name": "Chevron Pattern Acoustic Panels",
        "title": "Chevron Pattern Acoustic Panels | Decorative Wood Slat Panels | DUMI",
        "description": "Stylish chevron pattern wood slat acoustic panels. Combines modern geometric design with excellent sound diffusion and absorption. Real wood veneer finish.",
        "keywords": "chevron acoustic panels, wood slat panels, decorative acoustic, geometric pattern panels, modern acoustic design",
        "h2_features": "Real Wood Veneer | Chevron Pattern | Modern Design | Dual Function",
        "price": "From $79/piece",
        "specs": "96\"x48\" | 48\"x24\" | Custom lengths | Oak/Walnut/Mahogany",
        "applications": "Feature Walls | Luxury Studios | Corporate Lobbies | Retail Spaces"
    },
    {
        "id": "anti-vibration-acoustic-mounts",
        "name": "Anti-Vibration Acoustic Mounts",
        "title": "Anti-Vibration Acoustic Mounts | Decoupling Sound Isolation | DUMI",
        "description": "Professional anti-vibration mounts for decoupling walls, ceilings, and floors. Essential for sound isolation and preventing structural noise transmission.",
        "keywords": "anti-vibration mounts, acoustic decoupling, sound isolation mounts, vibration dampening, structural soundproofing",
        "h2_features": "Decoupling Design | High Deflection | Load Bearing | Sound Isolation STC +10",
        "price": "From $12/mount",
        "specs": "Standard (2\"x2\") | Heavy Duty (4\"x4\") | Various Load Ratings",
        "applications": "Wall Decoupling | Floor Isolation | Ceiling Hanging | Studio Construction"
    },
    {
        "id": "micro-perforated-acoustic-panels",
        "name": "Micro-Perforated Acoustic Panels",
        "title": "Micro-Perforated Acoustic Panels | Seamless Sound Absorption | DUMI",
        "description": "Elegant micro-perforated metal acoustic panels with nearly invisible perforation patterns. Ideal for venues requiring both aesthetics and acoustics. Custom patterns available.",
        "keywords": "micro perforated panels, metal acoustic panels, seamless acoustic, concert hall panels, architectural acoustic",
        "h2_features": "Micro-Perforation Pattern | Metal Construction | Seamless Look | NRC 0.70+",
        "price": "From $89/piece",
        "specs": "24\"x48\" | 48\"x48\" | Aluminum/Steel | Custom Patterns",
        "applications": "Concert Halls | Theaters | Museums | Corporate Atriums"
    },
    {
        "id": "fiberglass-acoustic-panel-3-inch",
        "name": "3-Inch Thick Fiberglass Acoustic Panels",
        "title": "3-Inch Thick Fiberglass Acoustic Panels | Maximum Sound Absorption | DUMI",
        "description": "Ultra-thick 3-inch fiberglass acoustic panels for maximum low-frequency absorption. NRC 0.95 rating. Essential for critical listening environments and professional studios.",
        "keywords": "3 inch acoustic panels, thick fiberglass panels, maximum absorption, low frequency treatment, NRC 0.95 acoustic panels",
        "h2_features": "3\" Thick Fiberglass | NRC 0.95 | Low Frequency Control | Professional Grade",
        "price": "From $79/piece",
        "specs": "24\"x24\"x3\" | 24\"x48\"x3\" | 48\"x48\"x3\"",
        "applications": "Professional Studios | Mastering Rooms | Home Theater | Recording Booths"
    }
]

def generate_product_html(product):
    """Generate complete HTML for a product page"""
    
    slug = product["id"]
    json_ld_name_safe = product["name"].replace("'", "\\'")
    desc_safe = product["description"].replace('"', '\\"')
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product["title"]}</title>
    <link rel="canonical" href="https://dumi-panel.com/products/{slug}.html">
    <meta name="description" content="{product["description"]}">
    <meta name="keywords" content="{product["keywords"]}">
    <meta name="robots" content="index, follow">
    
    <link rel="stylesheet" href="../css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{product["name"]}",
  "description": "{product["description"]}",
  "brand": {{
    "@type": "Brand",
    "name": "DUMI"
  }},
  "category": "Acoustic Panels / Soundproofing",
  "keywords": "{product["keywords"]}",
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "0",
    "availability": "https://schema.org/InStock"
  }}
}}
</script>
    <meta property="og:title" content="{product["title"]}">
    <meta property="og:description" content="{product["description"]}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="https://dumi-panel.com/products/{slug}.html">
    <meta property="og:image" content="https://dumi-panel.com/../images/akupanelcn/default-acoustic.jpg">
    <meta name="twitter:card" content="summary_large_image">
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
                    <img src="../images/akupanelcn/default-acoustic.jpg" alt="{product["name"]} - {product["description"]}" style="width: 100%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                </div>
                <div>
                    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: #2c3e50;">{product["name"]}</h1>
                    <p style="font-size: 1.2rem; color: #7f8c8d; margin-bottom: 30px;">{product["description"]}</p>
                    <div style="font-size: 2rem; font-weight: 700; color: #e74c3c; margin-bottom: 30px;">{product["price"]}</div>
                    <div style="margin: 30px 0;">
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span style="color: #2c3e50;"><strong>Free Global Shipping</strong> - Delivered to your door</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span style="color: #2c3e50;"><strong>Professional Quality</strong> - Trusted by studios worldwide</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span style="color: #2c3e50;"><strong>Factory Direct</strong> - Competitive wholesale pricing</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
                            <span style="color: #3498db; margin-right: 10px;">✓</span>
                            <span style="color: #2c3e50;"><strong>Custom Options</strong> - Sizes and configurations available</span>
                        </div>
                    </div>
                    <a href="../index.html#contact" class="btn btn-primary" style="display: inline-block; padding: 15px 40px; font-size: 1.1rem; text-decoration: none; background: #3498db; color: white; border-radius: 5px; transition: background 0.3s;">Contact for Quote</a>
                </div>
            </div>

            <div style="background: #f8f9fa; padding: 40px; border-radius: 10px; margin-bottom: 30px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px; color: #2c3e50;">Product Specifications</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <h3 style="font-size: 1.1rem; color: #3498db; margin-bottom: 10px;">Dimensions</h3>
                        <p style="color: #7f8c8d;">{product["specs"]}</p>
                    </div>
                    <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <h3 style="font-size: 1.1rem; color: #3498db; margin-bottom: 10px;">Key Features</h3>
                        <p style="color: #7f8c8d;">{product["h2_features"]}</p>
                    </div>
                </div>
            </div>

            <div style="background: #f8f9fa; padding: 40px; border-radius: 10px; margin-bottom: 30px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px; color: #2c3e50;">Applications</h2>
                <p style="color: #7f8c8d; font-size: 1.1rem; line-height: 1.8;">{product["applications"]}</p>
            </div>

            <div style="background: #f8f9fa; padding: 40px; border-radius: 10px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px; color: #2c3e50;">Why Choose {product["name"]}?</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                    <div>
                        <h3 style="font-size: 1.2rem; color: #3498db; margin-bottom: 10px;">Superior Sound Control</h3>
                        <p style="color: #7f8c8d; line-height: 1.7;">Professional-grade acoustic treatment designed for optimal sound absorption and diffusion. Perfect for critical listening environments.</p>
                    </div>
                    <div>
                        <h3 style="font-size: 1.2rem; color: #3498db; margin-bottom: 10px;">Easy Installation</h3>
                        <p style="color: #7f8c8d; line-height: 1.7;">Comes with all necessary mounting hardware. Our team can provide installation guidance for DIY or professional setup.</p>
                    </div>
                    <div>
                        <h3 style="font-size: 1.2rem; color: #3498db; margin-bottom: 10px;">Global Shipping</h3>
                        <p style="color: #7f8c8d; line-height: 1.7;">We ship worldwide with reliable logistics partners. Professional packaging ensures your panels arrive in perfect condition.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>DUMI</h3>
                    <p>Professional Sound Solutions</p>
                    <p>Your trusted partner for acoustic treatment worldwide.</p>
                </div>
                <div class="footer-section">
                    <h3>Products</h3>
                    <ul>
                        <li><a href="../products.html">All Products</a></li>
                        <li><a href="../products/acoustic-bass-traps.html">Bass Traps</a></li>
                        <li><a href="../products/fabric-acoustic-baffle-24x48x2.html">Acoustic Baffles</a></li>
                        <li><a href="../products/acoustic-foam-panel-12x12x2.html">Acoustic Foam</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Support</h3>
                    <ul>
                        <li><a href="../index.html#contact">Contact Us</a></li>
                        <li><a href="../index.html#about">About DUMI</a></li>
                        <li><a href="../index.html#applications">Applications</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <p>Email: info@dumi-panel.com</p>
                    <p>Global Shipping Available</p>
                    <p>Factory Direct Pricing</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 DUMI. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

def update_sitemap():
    """Update sitemap.xml with new products"""
    sitemap_path = "/Users/carstauto/.openclaw/workspace/dumi-panel/sitemap.xml"
    
    # Read existing sitemap
    with open(sitemap_path, 'r') as f:
        content = f.read()
    
    # Find the products section (before closing urlset)
    new_urls = ""
    for product in products:
        slug = product["id"]
        new_urls += f'''  <url>
    <loc>{BASE_URL}/products/{slug}.html</loc>
    <lastmod>2026-05-08</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
'''
    
    # Insert new URLs before the closing </urlset>
    content = content.replace('</urlset>', new_urls + '</urlset>')
    
    # Write updated sitemap
    with open(sitemap_path, 'w') as f:
        f.write(content)
    
    return len(products)

def main():
    print("=" * 60)
    print("DUMI-PANEL.COM - Batch Product Generator")
    print("Date: 2026-05-08 | Products: 15")
    print("=" * 60)
    
    created = []
    for product in products:
        slug = product["id"]
        filepath = os.path.join(PRODUCTS_DIR, f"{slug}.html")
        
        if os.path.exists(filepath):
            print(f"⚠️  Skipped (exists): {slug}")
            continue
        
        html = generate_product_html(product)
        with open(filepath, 'w') as f:
            f.write(html)
        
        print(f"✅ Created: {slug}")
        created.append(slug)
    
    print(f"\n📦 Created {len(created)} new products")
    
    # Update sitemap
    count = update_sitemap()
    print(f"📝 Updated sitemap.xml with {count} new URLs")
    
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review generated HTML files in products/")
    print("2. Commit changes to Git")
    print("3. Push to GitHub")
    print("4. Submit sitemap to Google Search Console")

if __name__ == "__main__":
    main()
