#!/usr/bin/env python3
"""DUMI PANEL - Generate 30+ new acoustic product pages (date-based rotation pool)
Categories: Acoustic panels, Wood slat, PET felt, 3D wall, Ceiling baffles
"""
import os, hashlib
from datetime import datetime

BASE_DIR = "/tmp/dumi-publish-dumi-panel/products"
TODAY = datetime.now().strftime("%Y-%m-%d")

# 30+ product pool (daily rotate 15)
PRODUCT_POOL = [
    {"filename":"studio-acoustic-foam-pro.html","name":"STUDIO ACOUSTIC FOAM PRO","subtitle":"录音棚专业吸音棉 | 录音棚级 | 驻波消除","tag":"🎙️ 录音棚","title":"STUDIO ACOUSTIC FOAM PRO - DUMI PANEL | Professional Studio Foam","description":"DUMI PANEL Studio Acoustic Foam Pro delivers professional recording studio quality sound absorption. Pyramidal design eliminates standing waves and flutter echoes. CE certified for home studios and professional recording environments.","keywords":"studio foam, recording studio panels, acoustic foam pro, DUMI studio panels, sound absorption","alt_visual":"DUMI Studio Acoustic Foam Pro in recording studio","gradient":"linear-gradient(135deg,#1a1a2e,#2a2a4e,#1a1a2e)","placeholder":"🎙️ STUDIO","tag_color":"#2a2a4e","features":[("NRC 0.95", "Studio-grade sound absorption coefficient"),("Pyramidal Design", "Eliminates standing waves and flutter echoes"),("Fire Retardant", "Class A fire rating per ASTM E84"),("Easy Install", "Self-adhesive backing for quick mounting")], "applications":["录音棚", "家庭录音室", "播客室", "音乐教室"], "related":["acoustic-foam-classic.html","nrc-95-panel.html"]},
    {"filename":"nrc-95-panel.html","name":"NRC 0.95 PANEL","subtitle":"NRC 0.95高吸音板 | 顶级吸音 | 静音空间","tag":"🔇 NRC95","title":"NRC 0.95 PANEL - DUMI PANEL | Maximum Sound Absorption","description":"DUMI PANEL NRC 0.95 panel achieves the highest sound absorption rating possible. Ideal for spaces requiring maximum noise reduction: home theaters, conference rooms, libraries. CE certified.","keywords":"NRC 0.95, high absorption panel, DUMI acoustic, maximum sound reduction","alt_visual":"DUMI NRC 0.95 high-absorption acoustic panel","gradient":"linear-gradient(135deg,#0d47a1,#1565c0,#1976d2)","placeholder":"🔇 NRC95","tag_color":"#1565c0","features":[("NRC 0.95", "Industry-leading absorption coefficient"),("50mm Thick", "Premium thickness for deep absorption"),("Eco Wool", "Recycled PET and natural wool blend"),("Custom Sizes", "Available in 8 standard sizes")], "applications":["家庭影院", "会议室", "图书馆", "录音室"], "related":["studio-acoustic-foam-pro.html","polyester-fiber-panel.html"]},
    {"filename":"wood-slat-walnut.html","name":"WOOD SLAT WALNUT","subtitle":"胡桃木实木条板 | 豪华质感 | 自然纹理","tag":"🪵 胡桃木","title":"WOOD SLAT WALNUT - DUMI PANEL | Premium Walnut Slat Wall","description":"DUMI PANEL Wood Slat Walnut features premium walnut wood slats on acoustic felt backing. Combines natural luxury with NRC 0.85 sound absorption. Perfect for high-end residential and commercial interiors.","keywords":"walnut slat panel, wood acoustic, DUMI walnut, premium slat wall, designer panels","alt_visual":"DUMI Wood Slat Walnut panel in luxury living room","gradient":"linear-gradient(135deg,#3e2723,#5d4037,#6d4c41)","placeholder":"🪵 WALNUT","tag_color":"#5d4037","features":[("Real Walnut Veneer", "Premium walnut wood on acoustic felt"),("NRC 0.85", "Excellent sound absorption"),("Easy Install", "Interlocking tongue-and-groove system"),("Sustainable", "FSC certified wood sourcing")], "applications":["豪华客厅", "高端酒店", "餐厅", "办公大堂"], "related":["wood-slat-oak.html","wood-slat-ash.html"]},
    {"filename":"wood-slat-oak.html","name":"WOOD SLAT OAK","subtitle":"橡木实木条板 | 经典风格 | 经久耐用","tag":"🪵 橡木","title":"WOOD SLAT OAK - DUMI PANEL | Classic Oak Slat Wall","description":"DUMI PANEL Wood Slat Oak delivers classic American oak aesthetic with acoustic performance. Natural wood grain on felt backing. Ideal for traditional and modern interiors.","keywords":"oak slat panel, wood acoustic, DUMI oak, classic slat wall","alt_visual":"DUMI Wood Slat Oak panel in modern office","gradient":"linear-gradient(135deg,#5d4037,#795548,#8d6e63)","placeholder":"🪵 OAK","tag_color":"#795548","features":[("Real Oak Veneer", "Authentic American oak appearance"),("NRC 0.80", "Strong sound absorption"),("Multiple Finishes", "Natural, stained, or painted"),("20yr Warranty", "Industry-leading product warranty")], "applications":["家庭影院", "餐厅", "高端办公", "酒店"], "related":["wood-slat-walnut.html","wood-slat-ash.html"]},
    {"filename":"wood-slat-ash.html","name":"WOOD SLAT ASH","subtitle":"白蜡木实木条板 | 浅色清新 | 现代北欧","tag":"🪵 白蜡","title":"WOOD SLAT ASH - DUMI PANEL | Light Ash Slat Wall","description":"DUMI PANEL Wood Slat Ash features light-colored ash wood for modern Scandinavian aesthetics. Combines bright natural wood with sound absorption.","keywords":"ash slat panel, light wood acoustic, DUMI ash, Scandinavian slat wall","alt_visual":"DUMI Wood Slat Ash panel in Scandinavian interior","gradient":"linear-gradient(135deg,#bcaaa4,#d7ccc8,#efebe9)","placeholder":"🪵 ASH","tag_color":"#a1887f","features":[("Light Ash Tone", "Bright natural wood color"),("NRC 0.82", "Effective sound absorption"),("Scandinavian Style", "Modern minimal design"),("Eco-Friendly", "Sustainable forestry practices")], "applications":["北欧风格住宅", "现代办公", "咖啡馆", "精品店"], "related":["wood-slat-walnut.html","wood-slat-oak.html"]},
    {"filename":"pet-felt-12mm.html","name":"PET FELT 12MM","subtitle":"12mm聚酯纤维板 | 多色可选 | 性价比高","tag":"🌈 PET","title":"PET FELT 12MM - DUMI PANEL | Colored PET Acoustic Panel","description":"DUMI PANEL PET Felt 12mm offers colorful acoustic solutions with recycled PET material. 24 colors available, ideal for creative interiors. CE certified, fire rated.","keywords":"PET felt panel, 12mm acoustic, DUMI PET, colorful acoustic, recycled panels","alt_visual":"DUMI PET Felt 12mm panel in colorful office design","gradient":"linear-gradient(135deg,#e91e63,#9c27b0,#3f51b5)","placeholder":"🌈 PET12","tag_color":"#9c27b0","features":[("24 Color Options", "Largest color range in industry"),("Recycled PET", "60% recycled content, eco-friendly"),("NRC 0.75", "Effective sound absorption"),("Lightweight", "Easy to handle and install")], "applications":["创意办公室", "学校", "儿童房", "公共空间"], "related":["pet-felt-24mm.html","pet-felt-9mm.html"]},
    {"filename":"pet-felt-24mm.html","name":"PET FELT 24MM","subtitle":"24mm厚聚酯纤维板 | 高吸音 | 强降噪","tag":"🌈 PET24","title":"PET FELT 24MM - DUMI PANEL | High-Performance PET Acoustic","description":"DUMI PANEL PET Felt 24mm delivers superior sound absorption with double thickness. Perfect for noisy environments requiring maximum noise reduction.","keywords":"PET 24mm, thick acoustic panel, DUMI high-perf, maximum absorption","alt_visual":"DUMI PET Felt 24mm thick acoustic panel","gradient":"linear-gradient(135deg,#1976d2,#0d47a1,#1565c0)","placeholder":"🌈 PET24","tag_color":"#0d47a1","features":[("24mm Thick", "Double thickness for high absorption"),("NRC 0.90", "Near-perfect sound absorption"),("Recycled Material", "60% recycled PET, sustainable"),("Custom Cut", "Any size available")], "applications":["会议室", "电话亭", "开放办公室", "餐厅"], "related":["pet-felt-12mm.html","pet-felt-9mm.html"]},
    {"filename":"pet-felt-9mm.html","name":"PET FELT 9MM","subtitle":"9mm聚酯纤维板 | 薄型设计 | 轻盈经济","tag":"🌈 PET9","title":"PET FELT 9MM - DUMI PANEL | Thin PET Acoustic","description":"DUMI PANEL PET Felt 9mm is the economical thin option for basic sound absorption. Ideal for budget projects and large area coverage.","keywords":"PET 9mm, thin acoustic, DUMI economy, budget panels","alt_visual":"DUMI PET Felt 9mm panel thin design","gradient":"linear-gradient(135deg,#26a69a,#4db6ac,#80cbc4)","placeholder":"🌈 PET9","tag_color":"#26a69a","features":[("9mm Thin", "Lightweight and economical"),("NRC 0.60", "Basic sound absorption"),("Multiple Colors", "12 color options available"),("Budget Friendly", "Cost-effective for large projects")], "applications":["学校", "办公楼", "零售店", "仓库"], "related":["pet-felt-12mm.html","pet-felt-24mm.html"]},
    {"filename":"3d-wave-panel.html","name":"3D WAVE PANEL","subtitle":"3D波浪造型板 | 立体视觉 | 装饰吸音","tag":"🌊 3D波浪","title":"3D WAVE PANEL - DUMI PANEL | 3D Wave Acoustic Design","description":"DUMI PANEL 3D Wave Panel creates stunning visual depth while providing effective sound absorption. Modern 3D design for feature walls.","keywords":"3D wave panel, dimensional acoustic, DUMI 3D, decorative sound panel","alt_visual":"DUMI 3D Wave Panel in modern hotel lobby","gradient":"linear-gradient(135deg,#1976d2,#42a5f5,#90caf9)","placeholder":"🌊 WAVE","tag_color":"#1976d2","features":[("3D Wave Design", "Eye-catching dimensional texture"),("NRC 0.70", "Good sound absorption"),("Paintable", "Custom color options available"),("Modular", "Easy to install and reconfigure")], "applications":["酒店大堂", "餐厅", "特色墙", "办公前台"], "related":["3d-cubic-panel.html","3d-peak-panel.html"]},
    {"filename":"3d-cubic-panel.html","name":"3D CUBIC PANEL","subtitle":"3D立方体造型 | 几何美学 | 现代设计","tag":"🧊 3D立方","title":"3D CUBIC PANEL - DUMI PANEL | 3D Cubic Design Acoustic","description":"DUMI PANEL 3D Cubic Panel offers geometric modern design with sound absorption. Perfect for contemporary interiors seeking visual impact.","keywords":"3D cubic panel, geometric acoustic, DUMI 3D cubic, modern design panels","alt_visual":"DUMI 3D Cubic Panel geometric wall design","gradient":"linear-gradient(135deg,#37474f,#546e7a,#78909c)","placeholder":"🧊 CUBIC","tag_color":"#37474f","features":[("3D Cubic Design", "Modern geometric aesthetic"),("NRC 0.65", "Effective sound absorption"),("12 Color Options", "Versatile color palette"),("Modular Tiles", "Easy installation")], "applications":["现代办公室", "精品店", "展览空间", "艺术画廊"], "related":["3d-wave-panel.html","3d-peak-panel.html"]},
    {"filename":"3d-peak-panel.html","name":"3D PEAK PANEL","subtitle":"3D山峰造型 | 立体声学 | 戏剧效果","tag":"⛰️ 3D山峰","title":"3D PEAK PANEL - DUMI PANEL | 3D Peak Acoustic","description":"DUMI PANEL 3D Peak Panel creates dramatic mountain-like visual effect with sound absorption. Eye-catching feature for modern interiors.","keywords":"3D peak panel, mountain acoustic, DUMI 3D peak, dramatic panels","alt_visual":"DUMI 3D Peak Panel dramatic wall design","gradient":"linear-gradient(135deg,#5d4037,#795548,#a1887f)","placeholder":"⛰️ PEAK","tag_color":"#5d4037","features":[("3D Peak Texture", "Dramatic mountain-like design"),("NRC 0.70", "Effective sound absorption"),("Natural Tones", "Earthy color palette"),("Statement Piece", "Creates focal point")], "applications":["酒店大堂", "办公前台", "餐厅", "会所"], "related":["3d-wave-panel.html","3d-cubic-panel.html"]},
    {"filename":"ceiling-baffle-linear.html","name":"CEILING BAFFLE LINEAR","subtitle":"线性天花隔音板 | 悬挂式 | 大空间","tag":"⬇️ 天花","title":"CEILING BAFFLE LINEAR - DUMI PANEL | Linear Ceiling Baffle","description":"DUMI PANEL Ceiling Baffle Linear provides sound absorption for large open spaces. Hangs vertically from ceiling. Perfect for offices, restaurants, and atriums.","keywords":"ceiling baffle, linear acoustic, DUMI baffle, hanging sound panel","alt_visual":"DUMI Ceiling Baffle Linear in modern office","gradient":"linear-gradient(135deg,#0277bd,#01579b,#0277bd)","placeholder":"⬇️ BAFFLE","tag_color":"#01579b","features":[("Linear Design", "Modern aesthetic lines"),("Hangs From Ceiling", "No wall modification needed"),("NRC 0.85", "High vertical absorption"),("Multiple Lengths", "1m, 2m, 3m options")], "applications":["开放式办公室", "中庭", "餐厅", "体育馆"], "related":["ceiling-baffle-curved.html","ceiling-cloud.html"]},
    {"filename":"ceiling-baffle-curved.html","name":"CEILING BAFFLE CURVED","subtitle":"曲线天花隔音板 | 优雅造型 | 艺术感","tag":"🌀 曲线","title":"CEILING BAFFLE CURVED - DUMI PANEL | Curved Ceiling Baffle","description":"DUMI PANEL Ceiling Baffle Curved combines acoustic performance with sculptural beauty. Curved panels create flowing visual interest.","keywords":"curved ceiling baffle, DUMI curved, artistic acoustic, design panels","alt_visual":"DUMI Curved Ceiling Baffle in designer restaurant","gradient":"linear-gradient(135deg,#ad1457,#c2185b,#ad1457)","placeholder":"🌀 CURVED","tag_color":"#ad1457","features":[("Curved Design", "Sculptural curved profile"),("Hanging System", "Easy ceiling installation"),("NRC 0.85", "High performance absorption"),("Designer Look", "Statement ceiling piece")], "applications":["高端餐厅", "精品酒店", "艺术空间", "办公大堂"], "related":["ceiling-baffle-linear.html","ceiling-cloud.html"]},
    {"filename":"ceiling-cloud.html","name":"CEILING CLOUD","subtitle":"云形天花吸音板 | 漂浮造型 | 顶部装饰","tag":"☁️ 云形","title":"CEILING CLOUD - DUMI PANEL | Ceiling Cloud Baffle","description":"DUMI PANEL Ceiling Cloud baffles float like clouds, providing acoustic absorption with artistic ceiling design. Perfect for modern creative spaces.","keywords":"ceiling cloud, floating baffle, DUMI cloud, artistic ceiling","alt_visual":"DUMI Ceiling Cloud baffles in modern creative office","gradient":"linear-gradient(135deg,#e1f5fe,#b3e5fc,#81d4fa)","placeholder":"☁️ CLOUD","tag_color":"#0277bd","features":[("Cloud Shape", "Floating cloud-like design"),("Multiple Sizes", "Various dimensions available"),("NRC 0.80", "Effective absorption"),("Custom Colors", "Match any interior palette")], "applications":["创意办公", "展览空间", "学校礼堂", "画廊"], "related":["ceiling-baffle-linear.html","ceiling-baffle-curved.html"]},
    {"filename":"bass-trap-corner.html","name":"BASS TRAP CORNER","subtitle":"角落低频陷阱 | 驻波消除 | HiFi房必备","tag":"🔊 低频","title":"BASS TRAP CORNER - DUMI PANEL | Corner Bass Trap","description":"DUMI PANEL Bass Trap Corner eliminates low-frequency standing waves in room corners. Essential for home theaters, recording studios, and HiFi rooms.","keywords":"bass trap, corner absorber, DUMI bass, low frequency, HiFi acoustic","alt_visual":"DUMI Bass Trap Corner in home theater","gradient":"linear-gradient(135deg,#311b92,#4527a0,#5e35b1)","placeholder":"🔊 BASS","tag_color":"#311b92","features":[("Low-Frequency Absorption", "Targets 40-200Hz problematic range"),("Corner Placement", "Maximizes room mode reduction"),("NRC 1.0 at 80Hz", "Industry-leading bass absorption"),("Professional Grade", "Used in recording studios worldwide")], "applications":["家庭影院", "HiFi房", "录音棚", "音乐制作室"], "related":["diffuser-quadratic.html","bass-trap-standalone.html"]},
    {"filename":"diffuser-quadratic.html","name":"DIFFUSER QUADRATIC","subtitle":"二次余数扩散器 | 声场扩散 | 录音棚级","tag":"🌐 扩散器","title":"DIFFUSER QUADRATIC - DUMI PANEL | Quadratic Residue Diffuser","description":"DUMI PANEL Diffuser Quadratic scatters sound waves for even distribution without deadening the room. Used in professional recording studios and audiophile listening rooms.","keywords":"diffuser, quadratic residue, DUMI diffusion, studio diffuser, sound scattering","alt_visual":"DUMI Quadratic Diffuser in recording studio","gradient":"linear-gradient(135deg,#4a148c,#6a1b9a,#7b1fa2)","placeholder":"🌐 DIFFUSE","tag_color":"#4a148c","features":[("QRD Design", "Mathematical precision diffuser"),("Scatters Sound", "Eliminates flutter echo"),("Wood Material", "Premium wood construction"),("Studio Quality", "Used in professional studios")], "applications":["录音棚", "HiFi房", "音乐教室", "聆听室"], "related":["bass-trap-corner.html","diffuser-1d.html"]},
    {"filename":"diffuser-1d.html","name":"DIFFUSER 1D","subtitle":"一维扩散器 | 线性声学处理 | HiFi级","tag":"📏 1D","title":"DIFFUSER 1D - DUMI PANEL | 1D Linear Diffuser","description":"DUMI PANEL 1D Diffuser provides linear sound diffusion for HiFi listening rooms. Combines absorption and diffusion for balanced acoustics.","keywords":"1D diffuser, linear diffusion, DUMI HiFi, balanced acoustic","alt_visual":"DUMI 1D Diffuser in audiophile room","gradient":"linear-gradient(135deg,#1a237e,#283593,#3949ab)","placeholder":"📏 1D","tag_color":"#1a237e","features":[("1D Design", "Linear diffusion pattern"),("Wood Construction", "Premium hardwood"),("Balanced Sound", "Mixes diffusion and absorption"),("Audiophile Grade", "High-end HiFi standard")], "applications":["HiFi房", "聆听室", "高端家庭影院", "录音棚"], "related":["diffuser-quadratic.html","bass-trap-corner.html"]},
    {"filename":"polyester-fiber-panel.html","name":"POLYESTER FIBER PANEL","subtitle":"聚酯纤维吸音板 | 经济实惠 | 多场景","tag":"💠 聚酯","title":"POLYESTER FIBER PANEL - DUMI PANEL | Polyester Acoustic","description":"DUMI PANEL Polyester Fiber Panel offers cost-effective sound absorption for large-scale projects. Recycled material, multiple colors, easy install.","keywords":"polyester fiber, budget acoustic, DUMI polyester, large project panels","alt_visual":"DUMI Polyester Fiber Panel in school classroom","gradient":"linear-gradient(135deg,#00838f,#0097a7,#00acc1)","placeholder":"💠 POLY","tag_color":"#00838f","features":[("100% Polyester", "Recycled fiber material"),("NRC 0.70", "Effective sound absorption"),("18 Colors", "Wide color selection"),("Eco-Certified", "OEKO-TEX certified")], "applications":["学校", "办公楼", "酒店", "公共空间"], "related":["pet-felt-12mm.html","pet-felt-24mm.html"]},
    {"filename":"acoustic-foam-classic.html","name":"ACOUSTIC FOAM CLASSIC","subtitle":"经典吸音棉 | 性价比高 | DIY友好","tag":"🧽 经典","title":"ACOUSTIC FOAM CLASSIC - DUMI PANEL | Classic Studio Foam","description":"DUMI PANEL Acoustic Foam Classic is the entry-level foam for home studios and hobby spaces. Easy DIY installation with self-adhesive backing.","keywords":"acoustic foam, classic studio, DUMI foam, DIY acoustic, hobby room","alt_visual":"DUMI Acoustic Foam Classic in home studio","gradient":"linear-gradient(135deg,#37474f,#546e7a,#607d8b)","placeholder":"🧽 CLASSIC","tag_color":"#37474f","features":[("Classic Egg Crate", "Time-tested design"),("Self-Adhesive", "Peel-and-stick installation"),("NRC 0.50", "Basic sound absorption"),("Budget Friendly", "Entry-level pricing")], "applications":["家庭工作室", "播客", "游戏室", "家庭影院"], "related":["studio-acoustic-foam-pro.html","nrc-95-panel.html"]},
    {"filename":"wood-slat-black.html","name":"WOOD SLAT BLACK","subtitle":"黑色实木条板 | 现代高级感 | 时尚空间","tag":"🖤 黑木","title":"WOOD SLAT BLACK - DUMI PANEL | Black Wood Slat","description":"DUMI PANEL Wood Slat Black features black-stained real wood slats for high-end modern interiors. Combines luxury aesthetic with NRC 0.80 sound absorption.","keywords":"black slat panel, modern wood, DUMI black, designer acoustic","alt_visual":"DUMI Wood Slat Black in modern luxury interior","gradient":"linear-gradient(135deg,#000000,#1a1a1a,#2c2c2c)","placeholder":"🖤 BLACK","tag_color":"#000000","features":[("Black Stain", "Deep black wood finish"),("NRC 0.80", "Strong sound absorption"),("Real Wood", "Authentic wood material"),("Modern Look", "High-end contemporary style")], "applications":["豪华住宅", "精品酒店", "高端办公", "会所"], "related":["wood-slat-walnut.html","wood-slat-oak.html"]},
    {"filename":"wood-slat-teak.html","name":"WOOD SLAT TEAK","subtitle":"柚木实木条板 | 热带奢华 | 永恒经典","tag":"🪵 柚木","title":"WOOD SLAT TEAK - DUMI PANEL | Teak Slat Wall","description":"DUMI PANEL Wood Slat Teak features premium Burmese teak wood for tropical luxury. Naturally water-resistant, ideal for spa and high-humidity environments.","keywords":"teak slat panel, tropical wood, DUMI teak, luxury slat wall","alt_visual":"DUMI Teak Slat Panel in luxury spa","gradient":"linear-gradient(135deg,#6d4c41,#795548,#8d6e63)","placeholder":"🪵 TEAK","tag_color":"#6d4c41","features":[("Premium Teak", "Genuine Burmese teak wood"),("Water Resistant", "Suitable for humid environments"),("NRC 0.85", "Excellent sound absorption"),("Natural Oils", "Ages beautifully over time")], "applications":["Spa水疗", "豪华浴室", "海滨酒店", "高端餐厅"], "related":["wood-slat-walnut.html","wood-slat-oak.html"]},
    {"filename":"fabric-wrapped-panel.html","name":"FABRIC WRAPPED PANEL","subtitle":"布艺包覆吸音板 | 优雅质感 | 多色可选","tag":"🧵 布艺","title":"FABRIC WRAPPED PANEL - DUMI PANEL | Fabric Acoustic Panel","description":"DUMI PANEL Fabric Wrapped Panel offers elegant fabric finish on acoustic core. 50+ fabric colors and patterns. Perfect for upscale interiors.","keywords":"fabric wrapped, fabric acoustic, DUMI fabric, elegant panel","alt_visual":"DUMI Fabric Wrapped Panel in luxury hotel","gradient":"linear-gradient(135deg,#5e35b1,#7b1fa2,#9c27b0)","placeholder":"🧵 FABRIC","tag_color":"#5e35b1","features":[("50+ Fabric Options", "Largest fabric selection"),("NRC 0.85", "High sound absorption"),("Custom Fabric", "Accept customer-provided fabric"),("Furniture Grade", "Designer quality finish")], "applications":["豪华酒店", "高端办公", "会议室", "贵宾室"], "related":["wood-slat-walnut.html","polyester-fiber-panel.html"]},
    {"filename":"wood-slat-pine.html","name":"WOOD SLAT PINE","subtitle":"松木实木条板 | 自然北欧 | 温暖质感","tag":"🪵 松木","title":"WOOD SLAT PINE - DUMI PANEL | Pine Slat Wall","description":"DUMI PANEL Wood Slat Pine features Scandinavian-style pine wood slats. Light natural color with subtle grain pattern. Perfect for warm minimalist interiors.","keywords":"pine slat panel, Scandinavian wood, DUMI pine, Nordic slat wall","alt_visual":"DUMI Pine Slat Panel in Scandinavian interior","gradient":"linear-gradient(135deg,#a1887f,#bcaaa4,#d7ccc8)","placeholder":"🪵 PINE","tag_color":"#a1887f","features":[("Natural Pine", "Authentic Scandinavian pine"),("NRC 0.80", "Effective sound absorption"),("Light Tone", "Bright warm color"),("Eco-Certified", "Sustainable forestry")], "applications":["北欧住宅", "精品咖啡馆", "现代办公", "展示空间"], "related":["wood-slat-ash.html","wood-slat-walnut.html"]},
    {"filename":"wood-slat-cherry.html","name":"WOOD SLAT CHERRY","subtitle":"樱桃木实木条板 | 红色调温暖 | 经典美式","tag":"🪵 樱桃","title":"WOOD SLAT CHERRY - DUMI PANEL | Cherry Wood Slat","description":"DUMI PANEL Wood Slat Cherry features American cherry wood with warm reddish tones. Classic American design with modern acoustic performance.","keywords":"cherry slat panel, American wood, DUMI cherry, classic slat wall","alt_visual":"DUMI Cherry Slat Panel in American traditional interior","gradient":"linear-gradient(135deg,#bf360c,#d84315,#e64a19)","placeholder":"🪵 CHERRY","tag_color":"#bf360c","features":[("American Cherry", "Genuine American cherry wood"),("Reddish Tones", "Warm natural color"),("NRC 0.82", "Effective sound absorption"),("Ages Gracefully", "Develops patina over time")], "applications":["美式住宅", "传统办公", "餐厅", "图书馆"], "related":["wood-slat-walnut.html","wood-slat-oak.html"]},
    {"filename":"micro-perforated-panel.html","name":"MICRO PERFORATED PANEL","subtitle":"微孔吸音板 | 视觉隐形 | 高科技吸音","tag":"🔬 微孔","title":"MICRO PERFORATED PANEL - DUMI PANEL | Micro Perforated Acoustic","description":"DUMI PANEL Micro Perforated Panel uses millions of tiny holes for sound absorption. Visually nearly invisible while providing NRC 0.75 absorption.","keywords":"micro perforated, invisible acoustic, DUMI micro, high-tech panel","alt_visual":"DUMI Micro Perforated Panel nearly invisible installation","gradient":"linear-gradient(135deg,#455a64,#546e7a,#607d8b)","placeholder":"🔬 MICRO","tag_color":"#455a64","features":[("Micro Perforations", "Tens of thousands of tiny holes"),("Visually Invisible", "Maintains surface appearance"),("NRC 0.75", "Effective absorption"),("Custom Patterns", "Various perforation designs")], "applications":["博物馆", "高端展厅", "礼堂", "会议室"], "related":["acoustic-foam-classic.html","wood-slat-walnut.html"]},
    {"filename":"magnetic-acoustic-panel.html","name":"MAGNETIC ACOUSTIC PANEL","subtitle":"磁性可拆卸吸音板 | 灵活布局 | 创意空间","tag":"🧲 磁性","title":"MAGNETIC ACOUSTIC PANEL - DUMI PANEL | Magnetic Removable","description":"DUMI PANEL Magnetic Acoustic Panel uses magnetic attachment for tool-free installation and easy reconfiguration. Perfect for creative and changing spaces.","keywords":"magnetic acoustic, removable panel, DUMI magnetic, reconfigurable","alt_visual":"DUMI Magnetic Acoustic Panel in creative office","gradient":"linear-gradient(135deg,#d32f2f,#c62828,#b71c1c)","placeholder":"🧲 MAG","tag_color":"#d32f2f","features":[("Magnetic Mount", "No tools required for installation"),("Reconfigurable", "Easy layout changes"),("NRC 0.70", "Good sound absorption"),("Multiple Colors", "8 color options")], "applications":["创意办公室", "展览空间", "学校", "联合办公"], "related":["modular-acoustic-wall-system.html","acoustic-foam-classic.html"]},
    {"filename":"outdoor-acoustic-panel.html","name":"OUTDOOR ACOUSTIC PANEL","subtitle":"户外吸音板 | 防水防晒 | 庭院露台","tag":"☀️ 户外","title":"OUTDOOR ACOUSTIC PANEL - DUMI PANEL | Weather-Resistant","description":"DUMI PANEL Outdoor Acoustic Panel is weather-resistant for exterior applications. Waterproof, UV-resistant, ideal for patios, pool areas, and outdoor entertainment.","keywords":"outdoor acoustic, weather-resistant, DUMI outdoor, patio panels","alt_visual":"DUMI Outdoor Acoustic Panel on patio","gradient":"linear-gradient(135deg,#f57c00,#fb8c00,#ff9800)","placeholder":"☀️ OUTDOOR","tag_color":"#f57c00","features":[("Weather Resistant", "Waterproof and UV-stable"),("Outdoor Rated", "Withstands -40 to 80°C"),("NRC 0.65", "Good outdoor absorption"),("Multiple Mounts", "Wall, fence, or freestanding")], "applications":["庭院", "露台", "泳池区", "户外餐厅"], "related":["polyester-fiber-panel.html","fabric-wrapped-panel.html"]},
    {"filename":"transparent-acoustic-panel.html","name":"TRANSPARENT ACOUSTIC PANEL","subtitle":"透明吸音板 | 视觉无遮挡 | 现代建筑","tag":"💎 透明","title":"TRANSPARENT ACOUSTIC PANEL - DUMI PANEL | See-Through Sound","description":"DUMI PANEL Transparent Acoustic Panel combines clear acrylic with acoustic perforations for see-through sound absorption. Ideal for modern architecture and partitions.","keywords":"transparent acoustic, see-through panel, DUMI transparent, modern partition","alt_visual":"DUMI Transparent Acoustic Panel in modern office partition","gradient":"linear-gradient(135deg,#e3f2fd,#bbdefb,#90caf9)","placeholder":"💎 CLEAR","tag_color":"#0277bd","features":[("Clear Acrylic", "Transparent panel design"),("NRC 0.60", "Effective absorption"),("Modern Look", "Minimal aesthetic"),("Light Transmission", "Maintains natural light")], "applications":["现代办公", "会议室", "展示空间", "高端零售"], "related":["micro-perforated-panel.html","glass-acoustic.html"]},
    {"filename":"color-acoustic-baffle.html","name":"COLOR ACOUSTIC BAFFLE","subtitle":"彩色悬挂吸音板 | 活泼设计 | 儿童空间","tag":"🌈 彩色","title":"COLOR ACOUSTIC BAFFLE - DUMI PANEL | Colorful Hanging","description":"DUMI PANEL Color Acoustic Baffle offers vibrant colored hanging acoustic panels. Perfect for schools, kindergartens, and playful spaces. 12 colors available.","keywords":"color baffle, hanging acoustic, DUMI color, school panels, kindergarten","alt_visual":"DUMI Color Acoustic Baffle in kindergarten","gradient":"linear-gradient(135deg,#ff4081,#7c4dff,#18ffff)","placeholder":"🌈 COLOR","tag_color":"#ff4081","features":[("12 Vibrant Colors", "Bright playful palette"),("Hanging Design", "No wall needed"),("NRC 0.75", "Effective absorption"),("Child Safe", "Non-toxic materials")], "applications":["幼儿园", "学校", "儿童医院", "游乐场"], "related":["ceiling-cloud.html","pet-felt-12mm.html"]},
    {"filename":"modular-acoustic-tile.html","name":"MODULAR ACOUSTIC TILE","subtitle":"模块化吸音砖 | 拼装组合 | 灵活设计","tag":"🧩 模块","title":"MODULAR ACOUSTIC TILE - DUMI PANEL | Modular Tile System","description":"DUMI PANEL Modular Acoustic Tile offers snap-together modular system for custom patterns. Mix and match colors, sizes, and textures for unique walls.","keywords":"modular tile, snap-together, DUMI modular, custom pattern acoustic","alt_visual":"DUMI Modular Acoustic Tile in modern lobby","gradient":"linear-gradient(135deg,#00897b,#00acc1,#0097a7)","placeholder":"🧩 TILE","tag_color":"#00897b","features":[("Snap Together", "No adhesive required"),("Custom Patterns", "Mix colors and sizes"),("NRC 0.70", "Effective absorption"),("Removable", "Take apart and rearrange")], "applications":["办公大堂", "学校", "创意空间", "展览"], "related":["modular-acoustic-wall-system.html","3d-cubic-panel.html"]},
    {"filename":"art-acoustic-panel.html","name":"ART ACOUSTIC PANEL","subtitle":"艺术画吸音板 | 装饰吸音 | 艺术空间","tag":"🎨 艺术","title":"ART ACOUSTIC PANEL - DUMI PANEL | Printable Art Acoustic","description":"DUMI PANEL Art Acoustic Panel combines acoustic performance with custom printed art. Create your own art walls that also absorb sound. UV-printed designs.","keywords":"art acoustic, printable panel, DUMI art, custom print acoustic","alt_visual":"DUMI Art Acoustic Panel in gallery","gradient":"linear-gradient(135deg,#e91e63,#9c27b0,#673ab7)","placeholder":"🎨 ART","tag_color":"#e91e63","features":[("Custom Art Print", "Your images on acoustic panel"),("NRC 0.75", "Effective sound absorption"),("UV Print Process", "Fade-resistant colors"),("Multiple Sizes", "From 30x30cm to 120x240cm")], "applications":["画廊", "酒店", "办公室", "创意空间"], "related":["fabric-wrapped-panel.html","magnetic-acoustic-panel.html"]},
    {"filename":"hexagon-acoustic-tile.html","name":"HEXAGON ACOUSTIC TILE","subtitle":"六边形吸音砖 | 蜂巢效果 | 装饰墙","tag":"⬡ 六边","title":"HEXAGON ACOUSTIC TILE - DUMI PANEL | Hexagon Pattern","description":"DUMI PANEL Hexagon Acoustic Tile creates stunning honeycomb patterns while providing sound absorption. Modular hexagon design for feature walls.","keywords":"hexagon tile, honeycomb pattern, DUMI hexagon, decorative acoustic","alt_visual":"DUMI Hexagon Acoustic Tile honeycomb wall","gradient":"linear-gradient(135deg,#fbc02d,#f9a825,#f57f17)","placeholder":"⬡ HEX","tag_color":"#f57f17","features":[("Hexagon Shape", "Modern honeycomb pattern"),("NRC 0.70", "Effective sound absorption"),("Modular", "Easy to combine"),("12 Colors", "Versatile palette")], "applications":["办公室", "咖啡馆", "精品店", "特色墙"], "related":["3d-cubic-panel.html","modular-acoustic-tile.html"]},
]


def generate_product_page(p):
    """Generate product HTML page using same structure as existing panel products"""
    features_html = ""
    for title, desc in p["features"]:
        features_html += f'''
        <div class="product-feature-item">
            <span class="feature-icon">✓</span>
            <div><strong>{title}</strong><p>{desc}</p></div>
        </div>'''

    app_html = "".join(f'<span>{a}</span>' for a in p["applications"])
    related_html = "".join(f'<a href="{r}" class="related-card"><span class="related-icon">→</span><span>{r.replace(".html","").replace("-"," ").title()}</span></a>\n' for r in p["related"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p["title"]}</title>
    <meta name="description" content="{p["description"]}">
    <meta name="keywords" content="{p["keywords"]}">
    <meta name="robots" content="index, follow">
    <meta name="last-modified" content="{TODAY}">
    <meta property="article:modified_time" content="{TODAY}T00:00:00+00:00">
    <meta property="og:title" content="{p["title"]}">
    <meta property="og:description" content="{p["description"]}">
    <meta property="og:type" content="product">
    <link rel="canonical" href="https://dumi-panel.com/products/{p["filename"]}">
    <link rel="stylesheet" href="../css/style.css">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "{p["name"]}",
        "description": "{p["description"]}",
        "brand": {{"@type": "Brand", "name": "DUMI PANEL"}},
        "offers": {{"@type": "Offer", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "seller": {{"@type": "Organization", "name": "DUMI PANEL"}}}}
    }}
    </script>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="logo"><h1>DUMI<span>PANEL</span></h1><p>Acoustic Panel Expert</p></div>
            <nav class="nav"><a href="../index.html">Home</a><a href="../index.html#products">Products</a><a href="../index.html#services">Services</a><a href="../index.html#about">About</a><a href="../index.html#contact">Contact</a></nav>
        </div>
    </header>
    <section class="product-detail">
        <div class="container">
            <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="../index.html#products">Products</a> / {p["name"]}</div>
            <div class="product-detail-grid">
                <div class="product-detail-img">
                    <div class="product-detail-visual" style="background: {p["gradient"]};">
                        <img src="../images/{p["filename"].replace(".html","")}.webp" alt="{p["alt_visual"]}" style="width:100%;height:100%;object-fit:cover;border-radius:12px;" onerror="this.style.display='none';this.parentElement.innerHTML='<div style=\\'display:flex;align-items:center;justify-content:center;height:100%;font-size:48px;color:rgba(255,255,255,0.15);\\'>{p["placeholder"]}</div>'">
                    </div>
                </div>
                <div class="product-detail-info">
                    <div class="product-detail-tag" style="background:{p["tag_color"]};">{p["tag"]}</div>
                    <h1>{p["name"]}™</h1>
                    <p class="product-subtitle">{p["subtitle"]}</p>
                    <div class="product-detail-desc">
                        <p>{p["description"]}</p>
                    </div>
                    <div class="product-features">
                        <h3>Features</h3>
                        {features_html}
                    </div>
                    <div class="product-applications">
                        <h3>Applications</h3>
                        <div class="application-tags">{app_html}</div>
                    </div>
                    <div class="product-cta">
                        <a href="../index.html#contact" class="btn-primary">Get Quote</a>
                        <a href="tel:+861****8877" class="btn-secondary">Call Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="related-products">
        <div class="container">
            <h2>Related Products</h2>
            <div class="related-grid">{related_html}</div>
        </div>
    </section>
    <footer class="footer">
        <div class="container">
            <p>© 2026 DUMI PANEL. All Rights Reserved. | Professional Acoustic Solutions</p>
            <p class="last-updated">Last updated: {TODAY}</p>
            <div class="dumi-sister-sites" style="margin-top:24px;padding-top:24px;border-top:1px solid var(--border)">
                <p style="color:var(--muted);font-size:0.9rem;margin-bottom:12px">DUMI Sister Sites — All 1,000+ Printer Farm Family:</p>
                <ul style="list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:12px;justify-content:center">
                    <li><a href="https://dumi-3d.com" target="_blank" rel="noopener">🎯 DUMI 3D - 3D Printing Farm</a></li>
                    <li><a href="https://dumi-auto.com" target="_blank" rel="noopener">🚗 DUMI Auto - PPF & Car Protection</a></li>
                    <li><a href="https://dumi-sheepskin.com" target="_blank" rel="noopener">🐑 DUMI Sheepskin - Medical Grade</a></li>
                    <li><a href="https://dumi-panel.com" target="_blank" rel="noopener">🔊 DUMI Panel - Acoustic Solutions</a></li>
                    <li><a href="https://www.amazon.ca/dp/B0DY1BN22D" target="_blank" rel="noopener">🛒 Amazon CA - Car Seat Cover</a></li>
                </ul>
            </div>
        </div>
    </footer>
    <style>
        .product-detail {{ padding: 60px 0; }}
        .product-detail-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 30px; }}
        .product-detail-visual {{ aspect-ratio: 4/3; border-radius: 12px; display: flex; align-items: center; justify-content: center; }}
        .product-detail-tag {{ display: inline-block; color: white; padding: 4px 12px; border-radius: 4px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }}
        .product-detail-info h1 {{ font-size: 42px; font-weight: 800; color: #1a1a2e; margin-bottom: 10px; letter-spacing: 2px; }}
        .product-subtitle {{ font-size: 16px; color: #888; margin-bottom: 25px; }}
        .product-detail-desc {{ background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 25px; border-left: 4px solid {p["tag_color"]}; }}
        .product-detail-desc p {{ color: #555; line-height: 1.8; }}
        .product-features {{ margin-bottom: 25px; }}
        .product-feature-item {{ display: flex; align-items: flex-start; gap: 12px; margin-bottom: 14px; }}
        .feature-icon {{ background: {p["tag_color"]}; color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; margin-top: 2px; }}
        .product-feature-item strong {{ display: block; font-size: 14px; color: #1a1a2e; }}
        .product-feature-item p {{ font-size: 12px; color: #888; }}
        .product-applications h3 {{ font-size: 16px; font-weight: 700; color: #1a1a2e; margin-bottom: 12px; }}
        .application-tags {{ display: flex; flex-wrap: wrap; gap: 8px; }}
        .application-tags span {{ background: #1a1a2e; color: white; padding: 6px 14px; border-radius: 4px; font-size: 13px; }}
        .product-cta {{ display: flex; gap: 15px; margin-top: 30px; }}
        .related-products {{ padding: 60px 0; }}
        @media (max-width: 768px) {{ .product-detail-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</body>
</html>'''


def main():
    """Generate 15 products from 32+ pool based on today's day hash"""
    day_hash = int(hashlib.md5(TODAY.encode()).hexdigest(), 16)
    n = len(PRODUCT_POOL)
    start = day_hash % n
    selected = [PRODUCT_POOL[(start + i) % n] for i in range(15)]

    for p in selected:
        path = os.path.join(BASE_DIR, p["filename"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(generate_product_page(p))
        print(f"✅ Created/Updated: {p['filename']}")

    print(f"\n📦 Pool: {len(PRODUCT_POOL)} products | Today's 15 picked")


if __name__ == "__main__":
    main()
