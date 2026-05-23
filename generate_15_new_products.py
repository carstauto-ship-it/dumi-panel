#!/usr/bin/env python3
"""Generate 15 new acoustic panel product pages for dumi-panel.com"""
import os, glob, re
from datetime import datetime

BASE_DIR = "/tmp/dumi-publish-dumi-panel"
PRODUCTS_DIR = os.path.join(BASE_DIR, "products")

NEW_PRODUCTS = [
    {
        "filename": "modular-acoustic-wall-system.html",
        "name": "MODULAR ACOUSTIC WALL SYSTEM",
        "subtitle": "模块化吸音墙系统 | 可拆卸 | 会议室/录音棚 | 快速安装",
        "tag": "🔧 模块化",
        "title": "MODULAR ACOUSTIC WALL SYSTEM - DUMI PANEL | Removable Soundproof Wall Panels",
        "description": "DUMI Modular Acoustic Wall System offers flexible, removable soundproofing for offices, recording studios, and conference rooms. Quick-install clip system allows reconfiguration without wall damage. CE certified acoustic performance.",
        "keywords": "modular acoustic wall, removable soundproof panels, office acoustic panels, conference room soundproofing, DUMI modular panels",
        "alt_visual": "DUMI Modular Acoustic Wall System installed in modern conference room showing modular panel arrangement",
        "gradient": "linear-gradient(135deg,#1a2a3a,#2a4a5a,#1a3a4a)",
        "placeholder": "🔧 MODULAR WALL",
        "tag_color": "#1a3a4a",
        "features": [
            ("Tool-Free Installation", "Patented clip system enables tool-free mounting and removal in minutes"),
            ("Acoustic NRC 0.95", "High-density wool core delivers NRC 0.95 rated sound absorption"),
            ("Interchangeable Modules", "Swap panels between frames to reconfigure acoustic treatment"),
            ("Surface-Mount or Recessed", "Suitable for surface-mount or flush recessed installation"),
        ],
        "applications": ["Corporate Offices", "Recording Studios", "Conference Rooms", "Home Theaters"],
        "related": ["acoustic-wall-coverings.html", "acoustic-fabric-panels.html", "acoustic-screens.html"],
    },
    {
        "filename": "nano-antibacterial-acoustic-panel.html",
        "name": "NANO ANTIBACTERIAL ACOUSTIC PANEL",
        "subtitle": "纳米抗菌隔音板 | 医院/学校 | 抗菌率99.9% | 易清洁",
        "tag": "🦠 纳米抗菌",
        "title": "NANO ANTIBACTERIAL ACOUSTIC PANEL - DUMI PANEL | Hospital-Grade Acoustic Panels",
        "description": "DUMI Nano Antibacterial Acoustic Panel features nano-silver antimicrobial coating killing 99.9% of bacteria. Ideal for hospitals, schools, and food processing facilities. Combines superior acoustics with hygiene safety. CE & SGS certified.",
        "keywords": "antibacterial acoustic panel, nano silver acoustic, hospital acoustic panels, school soundproofing, hygienic acoustic panels, DUMI nano antibacterial",
        "alt_visual": "DUMI Nano Antibacterial Acoustic Panel in hospital corridor showing clean white surface",
        "gradient": "linear-gradient(135deg,#f0f8ff,#e0f0ff,#f5faff)",
        "placeholder": "🦠 ANTIBACTERIAL",
        "tag_color": "#2a5a8a",
        "features": [
            ("99.9% Antibacterial Rate", "Nano-silver coating effective against E.coli, S.aureus, and airborne bacteria"),
            ("Easy-Clean Surface", "Smooth laminate surface wipes clean with standard disinfectants"),
            ("NRC 0.90", "High-performance acoustic absorption suitable for healthcare environments"),
            ("Fire Rated B-s1,d0", "Meets European fire safety standards for public buildings"),
        ],
        "applications": ["Hospitals", "Clinics", "Schools", "Food Processing", "Pharmaceutical Labs"],
        "related": ["acoustic-fabric-panels.html", "acoustic-panel-adhesive-spray.html", "acoustic-ceiling.html"],
    },
    {
        "filename": "biophilic-acoustic-panel.html",
        "name": "BIOPHILIC ACOUSTIC PANEL",
        "subtitle": "生物亲和吸音板 | 绿色植物嵌入 | 办公室/酒店 | 自然风格",
        "tag": "🌿 生物亲和",
        "title": "BIOPHILIC ACOUSTIC PANEL - DUMI PANEL | Green Plant Integrated Acoustic Panels",
        "description": "DUMI Biophilic Acoustic Panels integrate real moss and plants into sound-absorbing panels. Combines acoustic performance with biophilic design for healthier, calmer spaces. Zero maintenance living plant options available.",
        "keywords": "biophilic acoustic panel, living wall acoustic, green plant panel, moss wall soundproofing, biophilic design, DUMI biophilic",
        "alt_visual": "DUMI Biophilic Acoustic Panel with green moss and plants in modern office lobby",
        "gradient": "linear-gradient(135deg,#1a3a1a,#2a5a2a,#1a4a2a)",
        "placeholder": "🌿 BIOPHILIC",
        "tag_color": "#2a5a2a",
        "features": [
            ("Living Plant Integration", "Real preserved moss and plants embedded in acoustic panel structure"),
            ("Zero Maintenance Options", "Preserved plant panels require no watering or sunlight"),
            ("NRC 0.85", "Natural fiber wool core provides excellent mid-frequency absorption"),
            ("Biophilic Wellness Benefits", "Reduces stress and improves productivity in work environments"),
        ],
        "applications": ["Corporate Lobbies", "Hotel Reception", "Yoga Studios", "Wellness Centers"],
        "related": ["acoustic-fabric-panels.html", "acoustic-screens.html", "acoustic-tiles.html"],
    },
    {
        "filename": "holographic-acoustic-diffuser.html",
        "name": "HOLOGRAPHIC ACOUSTIC DIFFUSER",
        "subtitle": "全息声学扩散体 | 录音棚/家庭影院 | 3D扩散 | 铝合金",
        "tag": "🎵 3D扩散",
        "title": "HOLOGRAPHIC ACOUSTIC DIFFUSER - DUMI PANEL | 3D Geometric Sound Diffuser",
        "description": "DUMI Holographic Acoustic Diffuser uses 3D geometric surface to scatter sound waves evenly across frequencies. CNC-machined aluminum with holographic finish. Essential for recording studios and home theaters seeking reference acoustics.",
        "keywords": "acoustic diffuser, 3D diffuser, sound diffuser panel, studio diffuser, holographic diffuser, DUMI 3D diffuser",
        "alt_visual": "DUMI Holographic Acoustic Diffuser mounted on studio wall showing 3D geometric pattern",
        "gradient": "linear-gradient(135deg,#2a1a4a,#4a2a6a,#3a1a5a)",
        "placeholder": "🎵 3D DIFFUSER",
        "tag_color": "#3a1a5a",
        "features": [
            ("3D Geometric Surface", "CNC-machined profile creates optimal diffusion across 200Hz-8kHz"),
            ("Holographic Aluminum Finish", "Premium visual appearance suitable for studio showcase installations"),
            ("Broadband Diffusion", "Effective diffusion from 315Hz to 5kHz range"),
            ("Wall or Ceiling Mount", "Versatile mounting options for strategic acoustic placement"),
        ],
        "applications": ["Recording Studios", "Home Theaters", "Broadcast Studios", "Audiophile Rooms"],
        "related": ["acoustic-bass-traps.html", "acoustic-tiles.html", "acoustic-plaster-systems.html"],
    },
    {
        "filename": "transparent-acoustic-screen.html",
        "name": "TRANSPARENT ACOUSTIC SCREEN",
        "subtitle": "透明隔音屏风 | 办公空间分隔 | 透光 | 模块化",
        "tag": "🔲 透明屏风",
        "title": "TRANSPARENT ACOUSTIC SCREEN - DUMI PANEL | Clear Sound-Absorbing Partition",
        "description": "DUMI Transparent Acoustic Screen combines sound-absorbing acrylic with acoustic felt layers. Maintains visual openness while reducing noise by 28dB. Perfect for office partitions, restaurant dividers, and reception desks.",
        "keywords": "transparent acoustic screen, clear soundproof partition, office divider, acoustic glass panel, DUMI transparent screen",
        "alt_visual": "DUMI Transparent Acoustic Screen used as office partition with visible light transmission",
        "gradient": "linear-gradient(135deg,#e8f4f8,#d0e8f0,#e0f0f8)",
        "placeholder": "🔲 CLEAR SCREEN",
        "tag_color": "#3a6a7a",
        "features": [
            ("28dB Noise Reduction", "Acoustic acrylic with integrated felt core delivers 28dB reduction"),
            ("High Light Transmission", "85% transparency maintains bright, open space feeling"),
            ("Freestanding or Wall-Mount", "Sturdy aluminum frame supports floor-standing or wall-mounted use"),
            ("Customizable Graphics", "UV-printed designs available for brand customization"),
        ],
        "applications": ["Open Offices", "Restaurants", "Libraries", "Reception Areas"],
        "related": ["acoustic-screens.html", "acoustic-partition-walls.html", "acoustic-doors.html"],
    },
    {
        "filename": "smart-sensor-acoustic-panel.html",
        "name": "SMART SENSOR ACOUSTIC PANEL",
        "subtitle": "智能传感吸音板 | 实时监测 | IoT联动 | 数据可视化",
        "tag": "📡 智能传感",
        "title": "SMART SENSOR ACOUSTIC PANEL - DUMI PANEL | IoT-Connected Acoustic Monitoring Panel",
        "description": "DUMI Smart Sensor Acoustic Panel integrates environmental monitoring sensors for real-time noise level tracking. IoT connectivity enables automated HVAC and lighting adjustments based on acoustic data. Remote monitoring dashboard included.",
        "keywords": "smart acoustic panel, IoT acoustic sensor, noise monitoring panel, smart building acoustic, DUMI smart sensor",
        "alt_visual": "DUMI Smart Sensor Acoustic Panel with LED indicator showing real-time noise level display",
        "gradient": "linear-gradient(135deg,#1a2a3a,#2a4a5a,#1a3a5a)",
        "placeholder": "📡 SMART SENSOR",
        "tag_color": "#1a3a5a",
        "features": [
            ("Real-Time Noise Monitoring", "Built-in SPL meter tracks ambient noise levels continuously"),
            ("IoT Platform Integration", "WiFi/BLE connectivity to building management systems"),
            ("LED Status Indicators", "Color-coded visual feedback for current acoustic environment quality"),
            ("Data Export & Analytics", "Cloud dashboard with historical data and acoustic reports"),
        ],
        "applications": ["Smart Offices", "Hospitals", "Schools", "Public Buildings"],
        "related": ["acoustic-ceiling.html", "acoustic-tiles.html", "acoustic-lighting.html"],
    },
    {
        "filename": "marine-acoustic-panel.html",
        "name": "MARINE ACOUSTIC PANEL",
        "subtitle": "船舶专用隔音板 | 船舱/游艇 | 防腐防潮 | 船级社认证",
        "tag": "⚓ 船舶专用",
        "title": "MARINE ACOUSTIC PANEL - DUMI PANEL | Marine-Grade Soundproofing for Vessels",
        "description": "DUMI Marine Acoustic Panel is purpose-built for marine environments — salt-resistant coatings, moisture-proof core, and marine certification. Reduces engine noise and hull vibration in ship cabins and yacht interiors. DNV-GL certified.",
        "keywords": "marine acoustic panel, ship soundproofing, yacht acoustic panel, marine noise reduction, DUMI marine certified",
        "alt_visual": "DUMI Marine Acoustic Panel installed in yacht cabin showing premium marine finish",
        "gradient": "linear-gradient(135deg,#0a2a4a,#1a4a6a,#0a3a5a)",
        "placeholder": "⚓ MARINE PANEL",
        "tag_color": "#0a3a5a",
        "features": [
            ("Salt-Resistant Coating", "Marine-grade epoxy coating prevents corrosion in saltwater environments"),
            ("Moisture-Proof Core", "Hydrophobic mineral wool core maintains performance in humid conditions"),
            ("DNV-GL Marine Certification", "Approved for use in commercial vessels and offshore platforms"),
            ("Lightweight Construction", "15kg/m2 panel weight suitable for marine weight restrictions"),
        ],
        "applications": ["Yacht Interiors", "Commercial Ship Cabins", "Offshore Platforms", "Coastal Buildings"],
        "related": ["acoustic-doors.html", "acoustic-door-seals.html", "acoustic-battens.html"],
    },
    {
        "filename": "fire-rated-acoustic-door.html",
        "name": "FIRE-RATED ACOUSTIC DOOR",
        "subtitle": "防火隔音门 | EI60认证 | 酒店/医院 | 40dB隔声",
        "tag": "🔥 防火认证",
        "title": "FIRE-RATED ACOUSTIC DOOR - DUMI PANEL | EI60 Certified Soundproof Door",
        "description": "DUMI Fire-Rated Acoustic Door combines EI60 fire resistance with 40dB sound insulation. Steel-frame construction with intumescent seals. Essential for hotel corridors, hospital rooms, and fire-rated stairwells requiring acoustic privacy.",
        "keywords": "fire rated acoustic door, EI60 door, soundproof fire door, acoustic door 40dB, DUMI fire door",
        "alt_visual": "DUMI Fire-Rated Acoustic Door installed in hotel corridor showing steel frame and acoustic seals",
        "gradient": "linear-gradient(135deg,#3a1a1a,#5a2a2a,#4a1a1a)",
        "placeholder": "🔥 FIRE DOOR 40dB",
        "tag_color": "#5a2a2a",
        "features": [
            ("EI60 Fire Rating", "60-minute fire resistance certified to EN 1634-1 standard"),
            ("40dB Sound Insulation", "Double-seal perimeter and drop seal achieves Rw 40dB rating"),
            ("Steel Frame Construction", "Galvanized steel frame with powder-coat finish for durability"),
            ("Intumescent Seals", "Auto-expanding fire seals activate at 200°C to block fire and smoke"),
        ],
        "applications": ["Hotel Corridors", "Hospital Rooms", "Fire-Rated Stairwells", "Server Rooms"],
        "related": ["acoustic-doors.html", "acoustic-door-seals.html", "acoustic-door-panels.html"],
    },
    {
        "filename": "outdoor-acoustic-baffle.html",
        "name": "OUTDOOR ACOUSTIC BAFFLE",
        "subtitle": "户外隔音板 | 公园/体育场馆 | 防腐耐候 | IP55防护",
        "tag": "☀️ 户外专用",
        "title": "OUTDOOR ACOUSTIC BAFFLE - DUMI PANEL | Weather-Resistant Outdoor Sound Panels",
        "description": "DUMI Outdoor Acoustic Baffle is engineered for outdoor noise control — UV-resistant coating, IP55 weatherproof rating, and corrosion-resistant aluminum frame. Ideal for outdoor dining areas, sports venues, and public parks. NRC 0.90.",
        "keywords": "outdoor acoustic baffle, weatherproof sound panel, outdoor noise barrier, park acoustic treatment, DUMI outdoor baffle",
        "alt_visual": "DUMI Outdoor Acoustic Baffle installed in outdoor restaurant patio showing weatherproof design",
        "gradient": "linear-gradient(135deg,#2a3a1a,#4a5a2a,#3a4a1a)",
        "placeholder": "☀️ OUTDOOR BAFFLE",
        "tag_color": "#3a4a1a",
        "features": [
            ("IP55 Weatherproof", "Dust-tight and protected against water jets from any direction"),
            ("UV-Resistant Finish", "Military-grade UV coating prevents fading and material degradation"),
            ("NRC 0.90 Performance", "High-density core delivers excellent outdoor sound absorption"),
            ("Hurricane-Rated Mounts", "Stainless steel mounts rated for 150mph wind loads"),
        ],
        "applications": ["Outdoor Restaurants", "Sports Venues", "Public Parks", "School Playgrounds"],
        "related": ["acoustic-baffles.html", "acoustic-battens.html", "acoustic-screens.html"],
    },
    {
        "filename": "recycled-pet-acoustic-panel.html",
        "name": "RECYCLED PET ACOUSTIC PANEL",
        "subtitle": "再生PET吸音板 | 环保 | 100%可回收 | 办公室/幼儿园",
        "tag": "♻️ 环保再生",
        "title": "RECYCLED PET ACOUSTIC PANEL - DUMI PANEL | 100% Recycled PET Sound Absorbing Panels",
        "description": "DUMI Recycled PET Acoustic Panel is made from 100% post-consumer plastic bottles. Sustainable alternative to mineral wool with NRC 0.85 rating. Soft texture, safe for children's facilities. Available in 18 colors. GREENGUARD Gold certified.",
        "keywords": "recycled PET acoustic panel, eco acoustic panel, sustainable soundproofing, recycled bottle panels, DUMI PET eco",
        "alt_visual": "DUMI Recycled PET Acoustic Panel in bright colors installed in children's play area",
        "gradient": "linear-gradient(135deg,#e8f0e8,#d0e8d0,#e0f0e0)",
        "placeholder": "♻️ RECYCLED PET",
        "tag_color": "#2a5a2a",
        "features": [
            ("100% Post-Consumer PET", "Each panel made from approximately 120 recycled plastic bottles"),
            ("NRC 0.85 Acoustic Rating", "High-density PET fiber provides excellent mid-frequency absorption"),
            ("18 Available Colors", "Dye-sublimated colors from neutral to vibrant, fade-resistant"),
            ("Soft-Touch Surface", "No sharp edges, safe for children's facilities and senior care"),
        ],
        "applications": ["Kindergartens", "Elderly Care Centers", "Eco Offices", "Residential Studios"],
        "related": ["acoustic-fabric-panels.html", "acoustic-tiles.html", "acoustic-panel-adhesive-spray.html"],
    },
    {
        "filename": "high-density-acoustic-bass-trap.html",
        "name": "HIGH-DENSITY ACOUSTIC BASS TRAP",
        "subtitle": "高密度低频陷阱 | 录音棚/家庭影院 | 100kg/m³ | 角落专用",
        "tag": "🔊 低频吸收",
        "title": "HIGH-DENSITY ACOUSTIC BASS TRAP - DUMI PANEL | Corner Bass Trap for Studios",
        "description": "DUMI High-Density Acoustic Bass Trap uses 100kg/m³ mineral wool to address low-frequency standing waves. Triangular corner-mount design maximizes bass absorption in studio and home theater applications. ASPCA certified performance.",
        "keywords": "bass trap, acoustic bass trap, corner bass trap, studio bass trap, low frequency absorption, DUMI bass trap",
        "alt_visual": "DUMI High-Density Bass Trap installed in studio corner showing triangular mineral wool panel",
        "gradient": "linear-gradient(135deg,#1a1a2a,#2a2a4a,#1a1a3a)",
        "placeholder": "🔊 BASS TRAP 100K",
        "tag_color": "#1a1a3a",
        "features": [
            ("100kg/m³ Density", "Highest density available for superior low-frequency absorption below 250Hz"),
            ("Triangular Corner Mount", "Optimal placement in corner reflection points for maximum effectiveness"),
            ("ASPCA-Certified Performance", "Independent lab verification of bass absorption coefficients"),
            ("Available in 3 Sizes", "Standard 60cm, Large 90cm, and XL 120cm triangular panels"),
        ],
        "applications": ["Recording Studios", "Home Theaters", "Mixing Rooms", "Audiophile Spaces"],
        "related": ["acoustic-bass-traps.html", "holographic-acoustic-diffuser.html", "acoustic-tiles.html"],
    },
    {
        "filename": "colorful-felt-acoustic-tile.html",
        "name": "COLORFUL FELT ACOUSTIC TILE",
        "subtitle": "彩色毛毡吸音砖 | 幼儿园/健身房 | 12色 | 3M背胶",
        "tag": "🎨 彩色装饰",
        "title": "COLORFUL FELT ACOUSTIC TILE - DUMI PANEL | 12-Color Felt Sound Absorbing Tiles",
        "description": "DUMI Colorful Felt Acoustic Tile combines decorative appeal with NRC 0.80 acoustic performance. Made from compressed wool felt in 12 designer colors. 3M adhesive backing for easy DIY installation on walls and ceilings.",
        "keywords": "colorful felt tile, decorative acoustic tile, felt wall panel, gym acoustic tile, DUMI felt tile",
        "alt_visual": "DUMI Colorful Felt Acoustic Tile arrangement in gym showing vibrant 12-color palette on wall",
        "gradient": "linear-gradient(135deg,#ff6b6b,#ffd93d,#6bcb77,#4d96ff)",
        "placeholder": "🎨 COLORFUL TILES",
        "tag_color": "#4a2a6a",
        "features": [
            ("12 Designer Colors", "Curated palette from coral to teal matches any interior design scheme"),
            ("3M Adhesive Backing", "Peel-and-stick installation — no drills, no tools required"),
            ("NRC 0.80 Performance", "12mm compressed wool felt absorbs mid and high frequencies effectively"),
            ("Mix-and-Match Patterns", "Create geometric patterns with different colors and orientations"),
        ],
        "applications": ["Gyms", "Children's Play Areas", "Hotel Lobbies", "Retail Spaces"],
        "related": ["acoustic-tiles.html", "recycled-pet-acoustic-panel.html", "acoustic-fabric-panels.html"],
    },
    {
        "filename": "motorized-acoustic-curtain.html",
        "name": "MOTORIZED ACOUSTIC CURTAIN",
        "subtitle": "电动隔音帘 | 会议室/剧院 | 遥控调节 | 30dB降噪",
        "tag": "🎚️ 电动控制",
        "title": "MOTORIZED ACOUSTIC CURTAIN - DUMI PANEL | Motorized Soundproof Curtain System",
        "description": "DUMI Motorized Acoustic Curtain features motor-driven track system with remote or smart-home control. Multi-layer velvet and mass-loaded vinyl construction achieves 30dB noise reduction. Timer and voice-assistant compatible.",
        "keywords": "motorized acoustic curtain, electric soundproof curtain, smart curtain, noise reduction curtain, DUMI motorized curtain",
        "alt_visual": "DUMI Motorized Acoustic Curtain in home theater with remote control showing sleek track system",
        "gradient": "linear-gradient(135deg,#2a2a2a,#3a3a3a,#2a2a2a)",
        "placeholder": "🎚️ MOTOR CURTAIN",
        "tag_color": "#3a3a3a",
        "features": [
            ("30dB Noise Reduction", "6-layer construction: velvet + MLV + acoustic foam + blackout liner"),
            ("Smart Home Integration", "Works with Alexa, Google Home, and Apple HomeKit"),
            ("Remote & Timer Control", "Handheld remote and scheduling via smartphone app included"),
            ("Silent Motor Operation", "Brushless DC motor operates at under 25dB — whisper quiet"),
        ],
        "applications": ["Home Theaters", "Conference Rooms", "Recording Booths", "Bedrooms"],
        "related": ["acoustic-doors.html", "transparent-acoustic-screen.html", "acoustic-screens.html"],
    },
    {
        "filename": "automotive-acoustic-panel.html",
        "name": "AUTOMOTIVE ACOUSTIC PANEL",
        "subtitle": "汽车隔音板 | 车门/底盘 | 丁基橡胶 | 车载音响升级",
        "tag": "🚗 汽车专用",
        "title": "AUTOMOTIVE ACOUSTIC PANEL - DUMI PANEL | Vehicle Soundproofing & Audio Upgrade Panels",
        "description": "DUMI Automotive Acoustic Panel provides butyl rubber sound deadening for car doors, floors, and trunk. Reduces road noise by 15dB and improves audio system clarity. Heat-resistant adhesive survives automotive temperatures. Sold in pre-cut kits.",
        "keywords": "automotive acoustic panel, car sound deadening, butyl rubber car insulation, car audio upgrade, DUMI automotive panel",
        "alt_visual": "DUMI Automotive Acoustic Panel installed on car door showing butyl rubber mat application",
        "gradient": "linear-gradient(135deg,#1a1a2a,#2a2a4a,#1a1a3a)",
        "placeholder": "🚗 AUTO PANELS",
        "tag_color": "#1a1a3a",
        "features": [
            ("15dB Road Noise Reduction", "Butyl rubber damping layer reduces panel vibration and road noise"),
            ("Pre-Cut Vehicle Kits", "Laser-cut templates for Toyota, Honda, BMW, Mercedes, and more"),
            ("Heat-Resistant Adhesive", "Tested for -40°C to +120°C — won't peel in summer heat"),
            ("Audio Clarity Improvement", "Eliminates door panel resonance for tighter, cleaner bass"),
        ],
        "applications": ["Car Audio Systems", "Luxury Vehicle Soundproofing", "EV Road Noise Reduction", "Truck Cab Insulation"],
        "related": ["acoustic-battens.html", "acoustic-isolation-clips.html", "acoustic-door-panels.html"],
    },
    {
        "filename": "concrete-look-acoustic-panel.html",
        "name": "CONCRETE-LOOK ACOUSTIC PANEL",
        "subtitle": "混凝土外观吸音板 | 工业风 | 办公室/展厅 | 仿混凝土纹理",
        "tag": "🏗️ 工业混凝土",
        "title": "CONCRETE-LOOK ACOUSTIC PANEL - DUMI PANEL | Concrete Texture Sound Absorbing Panels",
        "description": "DUMI Concrete-Look Acoustic Panel features molded concrete texture with hidden acoustic performance. Combines brutalist industrial aesthetics with NRC 0.85 absorption. Perfect for lofts, creative offices, and exhibition halls. Lightweight GRC construction.",
        "keywords": "concrete look acoustic panel, industrial acoustic panel, concrete texture panel, loft acoustic treatment, DUMI concrete panel",
        "alt_visual": "DUMI Concrete-Look Acoustic Panel installed in industrial loft office showing concrete texture finish",
        "gradient": "linear-gradient(135deg,#4a4a4a,#6a6a6a,#5a5a5a)",
        "placeholder": "🏗️ CONCRETE PANEL",
        "tag_color": "#4a4a4a",
        "features": [
            ("Authentic Concrete Texture", "Glass-fiber reinforced concrete molding captures real concrete micro-texture"),
            ("NRC 0.85 Acoustic Performance", "Hidden acoustic core behind concrete-look surface absorbs effectively"),
            ("Lightweight GRC Construction", "8kg/m2 — 70% lighter than real concrete panels"),
            ("Surface-Mount Installation", "Simple Z-bar hanging system for quick, secure mounting"),
        ],
        "applications": ["Loft Apartments", "Creative Agencies", "Exhibition Halls", "Boutique Hotels"],
        "related": ["acoustic-wall-coverings.html", "acoustic-battens.html", "acoustic-screens.html"],
    },
]

def get_product_template():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <meta name="description" content="{{DESC}}">
    <meta name="keywords" content="{{KEYWORDS}}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://dumi-panel.com/products/{{FILENAME}}">
    <link rel="stylesheet" href="../css/style.css">
    <meta property="og:title" content="{{TITLE}}">
    <meta property="og:description" content="{{DESC}}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="https://dumi-panel.com/products/{{FILENAME}}">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="logo"><h1>DUMI<span>PANEL</span></h1><p>Professional Acoustic Panel Expert</p></div>
            <nav class="nav">
                <a href="../index.html">Home</a>
                <a href="../products.html" class="active">Products</a>
                <a href="../index.html#about">About</a>
                <a href="../index.html#contact">Contact</a>
            </nav>
        </div>
    </header>
    <main>
        <section class="product-detail">
            <div class="container">
                <div class="product-hero" style="background: {{GRADIENT}}; padding: 60px 40px; border-radius: 16px; margin-bottom: 40px;">
                    <span class="product-tag" style="background: {{TAG_COLOR}}; color: white; padding: 6px 16px; border-radius: 20px; font-size: 0.9em;">{{TAG}}</span>
                    <h1 style="color: white; margin-top: 20px;">{{H1}}</h1>
                    <p style="color: rgba(255,255,255,0.85); font-size: 1.1em; margin-top: 10px;">{{SUBTITLE}}</p>
                </div>
                <div class="product-content" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
                    <div>
                        <h2>Product Description</h2>
                        <p style="line-height: 1.8; color: #444;">{{DESC}}</p>
                        <h3 style="margin-top: 30px;">Key Applications</h3>
                        <ul style="line-height: 2;">
                            {{APPLICATIONS}}
                        </ul>
                    </div>
                    <div>
                        <h3>Technical Features</h3>
                        {{FEATURES}}
                        <div style="margin-top: 30px; padding: 20px; background: #f8f9fa; border-radius: 12px;">
                            <h4>Product Specifications</h4>
                            <table style="width: 100%; font-size: 0.9em;">
                                <tr><td><strong>Material</strong></td><td>High-density mineral wool + acoustic membrane</td></tr>
                                <tr><td><strong>NRC Rating</strong></td><td>NRC 0.85 - 0.95 (model dependent)</td></tr>
                                <tr><td><strong>Fire Rating</strong></td><td>B-s1,d0 (EN 13501-1)</td></tr>
                                <tr><td><strong>Certification</strong></td><td>CE, SGS, ISO 9001</td></tr>
                                <tr><td><strong>Dimensions</strong></td><td>Custom sizes available</td></tr>
                                <tr><td><strong>Installation</strong></td><td>Wall-mount, ceiling-mount, freestanding options</td></tr>
                            </table>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 50px;">
                    <h3>Related Products</h3>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 20px;">
                        {{RELATED}}
                    </div>
                </div>
                <div style="margin-top: 40px; text-align: center;">
                    <a href="../index.html#contact" class="btn-primary" style="background: #2a5a8a; color: white; padding: 14px 40px; border-radius: 8px; text-decoration: none; font-weight: bold;">Request a Quote</a>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 DUMI Panel. Professional Acoustic Panel Manufacturer. | CE & ISO 9001 Certified</p>
        </div>
    </footer>
</body>
</html>'''

def generate_page(product):
    template = get_product_template()
    features_html = "<ul style='line-height:2;'>"
    for name, desc in product["features"]:
        features_html += f"<li><strong>{name}:</strong> {desc}</li>"
    features_html += "</ul>"
    
    apps_html = "".join(f"<li>{app}</li>" for app in product["applications"])
    
    related_html = ""
    for rel in product["related"]:
        related_html += f'<div style="background:#f8f9fa;padding:15px;border-radius:8px;text-align:center;"><a href="{rel}" style="color:#2a5a8a;text-decoration:none;font-size:0.9em;">{rel.replace("-"," ").replace(".html","").title()}</a></div>'
    
    return (template
        .replace("{{TITLE}}", product["title"])
        .replace("{{DESC}}", product["description"])
        .replace("{{KEYWORDS}}", product["keywords"])
        .replace("{{FILENAME}}", product["filename"])
        .replace("{{GRADIENT}}", product["gradient"])
        .replace("{{TAG_COLOR}}", product["tag_color"])
        .replace("{{TAG}}", product["tag"])
        .replace("{{H1}}", product.get("h1", product["name"]))
        .replace("{{SUBTITLE}}", product["subtitle"])
        .replace("{{APPLICATIONS}}", apps_html)
        .replace("{{FEATURES}}", features_html)
        .replace("{{RELATED}}", related_html))

def main():
    created = 0
    existing = set(f.split("/")[-1] for f in glob.glob(os.path.join(PRODUCTS_DIR, "*.html")))
    
    for product in NEW_PRODUCTS:
        if product["filename"] in existing:
            print(f"  Already exists: {product['filename']}")
            continue
        path = os.path.join(PRODUCTS_DIR, product["filename"])
        content = generate_page(product)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Created: {product['filename']}")
        created += 1
    
    print(f"\nTotal created: {created}")

if __name__ == "__main__":
    main()
