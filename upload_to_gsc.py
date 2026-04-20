#!/usr/bin/env python3
"""
DUMI PANEL - Google Search Console URL Submission Script
https://dumi-panel.com
"""

SITE_URL = "https://dumi-panel.com"
SITEMAP_URL = "https://dumi-panel.com/sitemap.xml"

PRODUCT_SLUGS = [
    "polyester-fiber-acoustic-panels",
    "melamine-foam-panels",
    "glass-fiber-acoustic-panels",
    "acoustic-baffles",
    "mass-loaded-vinyl-panels",
    "composite-soundproof-panels",
    "acoustic-partition-walls",
    "resilient-channel-systems",
    "acoustic-plasterboard",
    "marine-acoustic-panels",
    "high-density-foam-panels",
    "industrial-soundproof-panels",
    "fabric-acoustic-panels",
    "perforated-metal-panels",
    "micropore-acoustic-panels",
    "echo-absorbers",
    "sound-diffusers",
    "concertina-foam-panels",
    "stretch-fabric-ceiling",
]

if __name__ == "__main__":
    print("DUMI PANEL - Google Search Console Submission")
    print("=" * 50)
    print(f"\n📋 Sitemap: {SITEMAP_URL}")
    print("   ✅ Sitemap 已更新 - Google 会自动发现新页面\n")
    
    print(f"🔍 {len(PRODUCT_SLUGS)}个新产品页URL:\n")
    for i, slug in enumerate(PRODUCT_SLUGS, 1):
        url = f"{SITE_URL}/products/{slug}.html"
        print(f"  {i:2d}. {url}")
    
    print(f"\n✅ 共 {len(PRODUCT_SLUGS)} 个新产品页需要提交到 GSC")
    print("\n📝 操作步骤:")
    print("  1. 登录 Google Search Console: https://search.google.com/search-console")
    print("  2. 选择 dumi-panel.com 属性")
    print("  3. 点击 'Sitemaps' -> 确认 sitemap.xml 已提交")
    print("  4. 点击 'URL Inspection' -> 逐个提交 -> '请求编入索引'")
    print("  5. 或使用 GSC API 完成自动化提交")
    print("\n💡 提示: Sitemap 已更新，Google 通常在24-48小时内自动发现新页面")