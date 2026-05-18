#!/usr/bin/env python3
"""Add 20 new acoustic panel products to dumi-panel.com"""

new_products = [
    {
        "id": "diffuser-acoustic-panels",
        "title": "Diffuser Acoustic Panels",
        "description": "QRD and skyline diffusers that scatter sound waves evenly across frequencies. Perfect for achieving balanced acoustics in recording studios and concert halls.",
        "price": "From $75/piece",
        "material": "MDF + Wood Veneer",
        "thickness": "100mm, 150mm",
        "sizes": "600x600mm, 1200x1200mm",
        "finish": "Natural wood, painted white, black",
        "fire_rating": "B1",
        "nrc": "0.55-0.70",
        "features": ["QRD skyline diffuser design", "Uniform sound diffusion", "Premium wood finish", "Wall mounting hardware included", "Professional studio quality"],
        "applications": ["Recording studios", "Concert halls", "Home theaters", "Broadcast rooms", "Music practice rooms"]
    },
    {
        "id": "transparent-acoustic-panels",
        "title": "Transparent Acoustic Panels",
        "description": "Crystal-clear acoustic panels that maintain visual openness while providing effective sound absorption. Ideal for modern glass offices and retail spaces.",
        "price": "From $120/m²",
        "material": "Acrylic + Sound-absorbing Core",
        "thickness": "20mm, 30mm",
        "sizes": "1200x2400mm, custom",
        "finish": "Clear, frosted, tinted",
        "fire_rating": "B1",
        "nrc": "0.65-0.80",
        "features": ["See-through acoustic solution", "Modern aesthetic design", "UV resistant materials", "Flexible installation options", "Maintains natural light flow"],
        "applications": ["Glass offices", "Retail stores", "Reception areas", "Museums", "Galleries"]
    },
    {
        "id": "spray-applied-acoustic",
        "title": "Spray Applied Acoustic Coating",
        "description": "Professional spray-on acoustic finish for seamless ceiling and wall applications. Perfect for irregular surfaces and large area coverage.",
        "price": "From $25/m²",
        "material": "Mineral Fiber + Binder",
        "thickness": "12mm, 25mm, 50mm",
        "sizes": "Coverage: 1.5-3m²/kg",
        "finish": "White, gray, custom colors",
        "fire_rating": "A2",
        "nrc": "0.70-0.90",
        "features": ["Seamless application", "Fills irregular surfaces", "Quick installation", "No visible joints or seams", "Excellent coverage rate"],
        "applications": ["Industrial facilities", "Swimming pools", "Sports arenas", "Warehouses", "Churches"]
    },
    {
        "id": "wood-wool-acoustic-panels",
        "title": "Wood Wool Acoustic Panels",
        "description": "Eco-friendly cement-bonded wood wool panels with excellent acoustic properties and natural wood aesthetic. Sustainable choice for green building projects.",
        "price": "From $35/m²",
        "material": "Wood Wool + Cement",
        "thickness": "25mm, 35mm, 50mm",
        "sizes": "600x600mm, 1200x600mm, 2400x1200mm",
        "finish": "Natural wood, painted",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.70-0.85",
        "features": ["100% natural materials", "Excellent durability", "Moisture resistant", "Breathable construction", "Carbon neutral production"],
        "applications": ["Schools", "Hospitals", "Libraries", "Sports centers", "Eco-buildings"]
    },
    {
        "id": "foam-acoustic-panels",
        "title": "Acoustic Foam Panels",
        "description": "High-density acoustic foam panels for professional soundproofing and studio treatment. Wedge and pyramid profiles for optimal sound absorption.",
        "price": "From $20/piece",
        "material": "Open-cell Polyurethane Foam",
        "thickness": "30mm, 50mm, 75mm",
        "sizes": "300x300mm, 600x600mm",
        "finish": "Black, charcoal, burgundy",
        "fire_rating": "B1",
        "nrc": "0.75-0.95",
        "features": ["High sound absorption coefficient", "Lightweight and easy to install", "Cost-effective solution", "Various profile options", "Ideal for studios"],
        "applications": ["Recording studios", "Podcasts", "Home theaters", "Gaming rooms", "Music practice"]
    },
    {
        "id": "hemp-acoustic-panels",
        "title": "Hemp Acoustic Panels",
        "description": "Natural hemp fiber acoustic panels with exceptional sustainability credentials. Biodegradable and non-toxic for healthy indoor environments.",
        "price": "From $45/m²",
        "material": "100% Natural Hemp Fiber",
        "thickness": "40mm, 60mm, 80mm",
        "sizes": "600x600mm, 1200x600mm",
        "finish": "Natural beige, custom dye",
        "fire_rating": "B2",
        "nrc": "0.80-0.90",
        "features": ["Fully biodegradable materials", "Non-toxic and VOC-free", "Excellent acoustic performance", "Natural pest resistant", "Carbon negative production"],
        "applications": ["Wellness centers", "Yoga studios", "Eco-offices", "Nurseries", "Green buildings"]
    },
    {
        "id": "recycled-pet-acoustic",
        "title": "Recycled PET Acoustic Panels",
        "description": "Acoustic panels made from 100% recycled plastic bottles. High performance with environmental benefits for sustainable architecture projects.",
        "price": "From $38/m²",
        "material": "Recycled PET Fiber",
        "thickness": "12mm, 24mm, 48mm",
        "sizes": "600x600mm, 1200x2400mm, custom",
        "finish": "Colorful woven texture",
        "fire_rating": "B1",
        "nrc": "0.75-0.90",
        "features": ["Made from recycled bottles", "Excellent sound absorption", "Wide color selection", "Lightweight and flexible", "Fully recyclable again"],
        "applications": ["Offices", "Schools", "Hotels", "Libraries", "Public buildings"]
    },
    {
        "id": "micro-perforated-panels",
        "title": "Micro Perforated Acoustic Panels",
        "description": "Ultra-thin micro-perforated metal panels with revolutionary acoustic performance. Ideal for ceiling and wall applications where space is limited.",
        "price": "From $85/m²",
        "material": "Aluminum + Micro-perforated Surface",
        "thickness": "5mm, 8mm, 12mm",
        "sizes": "300x300mm to 1200x600mm",
        "finish": "RAL powder coating",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.60-0.85",
        "features": ["Super thin profile", "Elegant appearance", "High durability", "Ceiling or wall mount", "Excellent for limited space"],
        "applications": ["Elevators", "Conference rooms", "Medical facilities", "Clean rooms", "Restaurants"]
    },
    {
        "id": "active-bass-traps",
        "title": "Active Subwoofer Bass Traps",
        "description": "Specialized low-frequency absorption panels designed for subwoofer and bass management in studios and home theaters.",
        "price": "From $150/piece",
        "material": "High-density Mineral Wool + Membrane",
        "thickness": "200mm, 300mm",
        "sizes": "600x600mm, 600x1200mm",
        "finish": "Fabric wrapped",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.90-1.00",
        "features": ["Extended low-frequency absorption", "Corner mounting design", "Professional bass management", "Dense acoustic core", "Maximum bass control"],
        "applications": ["Recording studios", "Home theaters", "Mixing rooms", "Subwoofer enclosures"]
    },
    {
        "id": "concrete-acoustic-panels",
        "title": "Concrete Acoustic Panels",
        "description": "Heavy-duty precast concrete panels with built-in acoustic properties. Industrial strength for demanding environments.",
        "price": "From $120/m²",
        "material": "Reinforced Concrete + Resonators",
        "thickness": "50mm, 75mm, 100mm",
        "sizes": "600x600mm to 2400x1200mm",
        "finish": "Raw concrete, polished, colored",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.65-0.85",
        "features": ["Extreme durability", "Industrial aesthetic", "Weather resistant", "High mass construction", "Long service life"],
        "applications": ["Parking structures", "Industrial facilities", "Sports venues", "Transit stations", "Outdoor areas"]
    },
    {
        "id": "suspended-acoustic-rafts",
        "title": "Suspended Acoustic Rafts",
        "description": "Floating ceiling islands for open-plan acoustic treatment. Suspended from ceilings to absorb sound without affecting ceiling void.",
        "price": "From $200/piece",
        "material": "Mineral Wool + Steel Frame",
        "thickness": "100mm, 150mm, 200mm",
        "sizes": "1200x1200mm, 2400x1200mm",
        "finish": "Fabric wrapped, painted",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.85-1.00",
        "features": ["Suspended ceiling solution", "No ceiling void needed", "Modern visual impact", "Variable height mounting", "Excellent absorption"],
        "applications": ["Open offices", "Atriums", "Restaurants", "Lobbies", "Shopping centers"]
    },
    {
        "id": "movable-baffle-walls",
        "title": "Movable Acoustic Baffle Walls",
        "description": "Free-standing portable acoustic baffle walls for flexible room division and sound control. Perfect for event spaces and multi-purpose halls.",
        "price": "From $350/piece",
        "material": "High-density Fiber Glass",
        "thickness": "100mm",
        "sizes": "1200x2400mm, custom",
        "finish": "Fabric wrapped",
        "fire_rating": "A2",
        "nrc": "0.90-1.00",
        "features": ["Mobile and portable", "No installation required", "Adjustable positioning", "Strong sound blocking", "Easy storage"],
        "applications": ["Event venues", "Exhibition halls", "Conference centers", "Hotels", "Banquet halls"]
    },
    {
        "id": "acoustic-plaster-systems",
        "title": "Acoustic Plaster Systems",
        "description": "Spray-applied acoustic plaster for seamless ceiling and wall finishes. Perfect for curved surfaces and architectural designs.",
        "price": "From $40/m²",
        "material": "Vermiculite + Acoustic Binder",
        "thickness": "15mm, 25mm, 35mm",
        "sizes": "Coverage varies by thickness",
        "finish": "Smooth, textured",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.60-0.85",
        "features": ["Seamless finish", "Conforms to any shape", "No joints or seams", "Smooth architectural look", "Durable surface"],
        "applications": ["Museums", "Theaters", "Churches", "Auditoriums", "Cinemas"]
    },
    {
        "id": "felt-acoustic-tiles",
        "title": "Felt Acoustic Tiles",
        "description": "Decorative felt tiles with integrated sound absorption. Contemporary design with excellent acoustic performance.",
        "price": "From $35/m²",
        "material": "Recycled Wool/Polyester Felt",
        "thickness": "12mm, 20mm, 30mm",
        "sizes": "300x300mm, 600x600mm, 1200x600mm",
        "finish": "Multiple colors, patterns",
        "fire_rating": "B1",
        "nrc": "0.65-0.85",
        "features": ["Modern decorative design", "Easy clip installation", "Mix-and-match colors", "Lightweight construction", "Eco-friendly materials"],
        "applications": ["Offices", "Hotels", "Restaurants", "Retail", "Residential"]
    },
    {
        "id": "ceramic-acoustic-tiles",
        "title": "Ceramic Acoustic Tiles",
        "description": "Innovative acoustic ceramic tiles combining aesthetic appeal with sound absorption. Waterproof and durable for wet areas.",
        "price": "From $60/m²",
        "material": "Porous Ceramic",
        "thickness": "20mm, 30mm, 40mm",
        "sizes": "300x300mm, 600x600mm",
        "finish": "Glazed, unglazed, custom",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.60-0.80",
        "features": ["Waterproof construction", "High durability", "Hygienic surface", "Thermal mass benefits", "Long-lasting finish"],
        "applications": ["Swimming pools", "Spas", "Bathrooms", "Kitchens", "Food processing"]
    },
    {
        "id": "aerogel-acoustic-panels",
        "title": "Aerogel Acoustic Panels",
        "description": "Ultra-high-performance aerogel insulation panels for maximum soundproofing in minimal thickness. Space-age technology for critical applications.",
        "price": "From $200/m²",
        "material": "Silica Aerogel + Acoustic Facing",
        "thickness": "10mm, 20mm, 30mm",
        "sizes": "600x600mm, 1200x600mm",
        "finish": "White film, fabric faced",
        "fire_rating": "A1 (non-combustible)",
        "nrc": "0.50-0.75",
        "features": ["Extremely thin profile", "Superior insulation", "High-tech materials", "Minimal thickness", "Premium performance"],
        "applications": ["Cryogenic facilities", "High-precision labs", "Recording studios", "Home theaters", "Marine applications"]
    },
    {
        "id": "mass-loaded-vinyl",
        "title": "Mass Loaded Vinyl Soundproofing",
        "description": "High-density flexible vinyl sheets for effective sound blocking. Flexible and easy to install on walls, floors, and ceilings.",
        "price": "From $25/m²",
        "material": "Mass Loaded Vinyl (MLV)",
        "thickness": "2mm, 3mm, 4mm",
        "sizes": "1.2m x 5m rolls",
        "finish": "Black, gray",
        "fire_rating": "B1",
        "stc": "26-38",
        "features": ["Flexible and conformable", "Excellent sound blocking", "Thin profile", "Easy to cut and install", "Versatile applications"],
        "applications": ["Wall soundproofing", "Floor underlayment", "Ceiling decoupling", "Pipe wrapping", "Vehicle soundproofing"]
    },
    {
        "id": "door-acoustic-blankets",
        "title": "Door Acoustic Blankets",
        "description": "Removable soundproof blankets for doors. Quick deployment solution for recording booths and temporary isolation.",
        "price": "From $180/piece",
        "material": "Mass Loaded Vinyl + Fiber Glass",
        "thickness": "50mm",
        "sizes": "900x2100mm, custom",
        "finish": "Black vinyl, aluminum trim",
        "fire_rating": "A2",
        "stc": "35-40",
        "features": ["Hangs on door frame", "Effective sound blocking", "Portable and removable", "Quick setup", "Professional quality"],
        "applications": ["Recording booths", "Broadcast studios", "Practice rooms", "Home studios", "Event spaces"]
    },
    {
        "id": "acoustic-channel-strips",
        "title": "Acoustic Furring Channel Strips",
        "description": "Metal furring channels for creating acoustic separation in wall and ceiling constructions. Essential for decoupling soundproofing systems.",
        "price": "From $8/meter",
        "material": "Galvanized Steel",
        "thickness": "0.5mm, 0.7mm",
        "sizes": "50mm x 2.5m, 75mm x 2.5m",
        "finish": "Galvanized",
        "fire_rating": "A1 (non-combustible)",
        "features": ["Creates acoustic break", "Reduces structure-borne sound", "Easy to install", "Compatible with boards", "Professional specification"],
        "applications": ["Wall soundproofing", "Ceiling soundproofing", "Floor systems", "Industrial隔音", "Renovation projects"]
    },
    {
        "id": "acoustic-isolation-clips",
        "title": "Acoustic Isolation Clips",
        "description": "Specialized acoustic decoupling clips for wall and ceiling soundproofing. Creates mechanical separation to block sound transmission.",
        "price": "From $5/piece",
        "material": "Rubber + Galvanized Steel",
        "thickness": "25mm, 35mm",
        "sizes": "Standard mounting spacing: 600mm",
        "finish": "Yellow rubber, zinc plated",
        "fire_rating": "B1",
        "features": ["Decouples structural connection", "Reduces vibration transfer", "Easy retrofit option", "Compatible with various boards", "Effective sound isolation"],
        "applications": ["Wall soundproofing", "Ceiling soundproofing", "Floor isolation", "Studio construction", "Home theater build"]
    }
]

def generate_html(product):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product['title']} | DUMI Acoustic Solutions</title>
    <meta name="description" content="{product['description']} - {product['price']}">
    <meta name="keywords" content="acoustic panel, soundproofing, {product['id'].replace('-', ' ')}, noise control, sound absorption">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{product['title']}",
  "description": "{product['description']}",
  "brand": {{ "@type": "Brand", "name": "DUMI" }},
  "offers": {{ "@type": "Offer", "priceCurrency": "USD", "price": "0", "availability": "https://schema.org/InStock" }}
}}
</script>
    <meta property="og:title" content="{product['title']} | DUMI Acoustic Solutions">
    <meta property="og:description" content="{product['description']}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="https://dumi-panel.com/products/{product['id']}.html">
</head>
<body>
    <header class="header"><div class="container"><div class="header-inner"><a href="../index.html" class="logo"><span class="logo-icon">🔇</span><div class="logo-text"><span class="logo-brand">DUMI</span><span class="logo-tagline">Professional Acoustic Solutions</span></div></a><nav class="nav"><ul class="nav-menu"><li><a href="../index.html" class="nav-link">Home</a></li><li><a href="../products.html" class="nav-link">Products</a></li><li><a href="../index.html#contact" class="nav-link">Contact</a></li></ul></nav></div></div></header>
    <section class="product-detail" style="padding: 60px 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px;">
                <div><img src="../images/akupanelcn/fabric-1.jpg" alt="{product['title']}" style="width: 100%; border-radius: 10px;" onerror="this.src='../images/placeholder.jpg'"></div>
                <div>
                    <h1>{product['title']}</h1>
                    <p class="product-subtitle">DUMI Professional Acoustic Solutions</p>
                    <div class="product-detail-desc"><p>{product['description']}</p></div>
                    <div style="font-size: 1.8rem; color: var(--primary-color, #2c3e50); margin: 20px 0;">{product['price']}</div>
                    <div class="product-features">'''

    for feature in product['features']:
        html += f'''
                        <div class="product-feature-item"><span class="feature-icon">✓</span><div><strong>{feature}</strong></div></div>'''

    html += f'''
                    </div>
                    <div class="product-cta"><a href="../index.html#contact" class="btn-primary">Get a Quote →</a></div>
                </div>
            </div>
            <div style="margin-top: 60px; background: var(--light-color, #f8f9fa); padding: 40px; border-radius: 10px;">
                <h2 style="margin-bottom: 30px;">Technical Specifications</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
                    <div style="background: white; padding: 15px; border-radius: 5px;"><strong>Material:</strong> {product['material']}</div>
                    <div style="background: white; padding: 15px; border-radius: 5px;"><strong>Thickness:</strong> {product['thickness']}</div>
                    <div style="background: white; padding: 15px; border-radius: 5px;"><strong>Sizes:</strong> {product['sizes']}</div>
                    <div style="background: white; padding: 15px; border-radius: 5px;"><strong>Finish:</strong> {product['finish']}</div>
                    <div style="background: white; padding: 15px; border-radius: 5px;"><strong>Fire Rating:</strong> {product['fire_rating']}</div>'''

    if 'nrc' in product:
        html += f'''
                    <div style="background: white; padding: 15px; border-radius: 5px;"><strong>NRC:</strong> {product['nrc']}</div>'''

    html += f'''
                </div>
            </div>
            <div style="margin-top: 60px;">
                <h2 style="margin-bottom: 30px;">Applications</h2>
                <div style="display: flex; flex-wrap: wrap; gap: 15px;">'''

    for app in product['applications']:
        html += f'''
                    <span style="padding: 10px 20px; background: var(--primary-color, #2c3e50); color: white; border-radius: 20px;">{app}</span>'''

    html += '''
                </div>
            </div>
        </div>
    </section>
    <footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><h2>DUMI</h2><p>Professional Acoustic Solutions Expert · Factory Direct</p></div><div class="footer-contact"><h4>Contact</h4><p>📧 carstauto2010@gmail.com</p><p>📱 +86-13001727017</p></div></div><div class="footer-bottom"><p>© 2026 DUMI. All rights reserved.</p></div></div></footer>
</body>
</html>'''
    return html

if __name__ == "__main__":
    import os
    import subprocess
    from datetime import datetime
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    created_files = []
    for product in new_products:
        html = generate_html(product)
        filepath = f"products/{product['id']}.html"
        with open(filepath, 'w') as f:
            f.write(html)
        created_files.append(filepath)
        print(f"Created: {filepath}")
    
    # Update sitemap.xml
    with open("sitemap.xml", 'r') as f:
        sitemap = f.read()
    
    today = datetime.now().strftime("%Y-%m-%d")
    new_urls = ""
    for product in new_products:
        new_urls += f'''
    <url>
        <loc>https://dumi-panel.com/products/{product['id']}.html</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>'''
    
    sitemap = sitemap.replace("</urlset>", new_urls + "\n</urlset>")
    with open("sitemap.xml", 'w') as f:
        f.write(sitemap)
    print(f"Updated sitemap.xml with {len(new_products)} new URLs")
    
    # Update products.html
    product_cards = ""
    for product in new_products:
        product_cards += f'''
                <div class="product-card">
                    <a href="products/{product['id']}.html">
                        <div class="product-image">
                            <img src="images/akupanelcn/fabric-1.jpg" alt="{product['title']}" onerror="this.src='images/placeholder.jpg'">
                        </div>
                        <div class="product-info">
                            <h3>{product['title']}</h3>
                            <p>{product['description'][:100]}...</p>
                            <div class="product-price">{product['price']}</div>
                        </div>
                    </a>
                </div>'''
    
    with open("products.html", 'r') as f:
        products_html = f.read()
    
    # Find the product grid section and add new products
    products_html = products_html.replace("</section>\n    <!-- Footer -->", product_cards + "\n            </div>\n        </div>\n    </section>\n    <!-- Footer -->")
    
    with open("products.html", 'w') as f:
        f.write(products_html)
    print("Updated products.html")
    
    # Git commit and push
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Add 20 new acoustic panel products - {today}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("\n✅ Git push completed!")
    
    print(f"\n{'='*50}")
    print(f"Total products added: {len(new_products)}")
    print(f"Created files: {len(created_files)}")
    print(f"{'='*50}")
