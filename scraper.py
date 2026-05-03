#!/usr/bin/env python3
"""
🌟 ROYAL SCENT - Luxury Perfume Store Generator
Ultra Premium Glass Morphism Design with Admin Protection
"""

import os
import json
import base64

def create_directory_structure():
    """إنشاء هيكل المجلدات"""
    directories = ['css', 'js', 'images', 'assets']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ تم إنشاء مجلد: {directory}")

def create_index_html():
    """إنشاء ملف index.html بتصميم Glass Morphism"""
    html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ROYAL SCENT | متجر العطور الفاخرة</title>
    <meta name="description" content="متجر العطور الفاخرة - أفخم العطور العالمية بتصميم زجاجي عصري">
    <link rel="stylesheet" href="css/glass-morphism.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/bubbles.css">
    <link rel="stylesheet" href="css/admin.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=Playfair+Display:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
    <!-- Animated Bubbles Background -->
    <div class="bubbles-container">
        <div class="bubble bubble-1"></div>
        <div class="bubble bubble-2"></div>
        <div class="bubble bubble-3"></div>
        <div class="bubble bubble-4"></div>
        <div class="bubble bubble-5"></div>
        <div class="bubble bubble-6"></div>
        <div class="bubble bubble-7"></div>
        <div class="bubble bubble-8"></div>
        <div class="bubble bubble-9"></div>
        <div class="bubble bubble-10"></div>
    </div>

    <!-- Floating Particles -->
    <div class="particles" id="particles"></div>

    <!-- Glass Navigation Bar -->
    <nav class="glass-nav">
        <div class="nav-container">
            <div class="logo-section">
                <div class="logo-icon">
                    <i class="fas fa-crown"></i>
                </div>
                <span class="logo-text">ROYAL SCENT</span>
            </div>
            <div class="nav-links">
                <a href="#home" class="nav-link active">الرئيسية</a>
                <a href="#products" class="nav-link">المنتجات</a>
                <a href="#about" class="nav-link">من نحن</a>
                <a href="#contact" class="nav-link">اتصل بنا</a>
                <div class="cart-icon-wrapper" onclick="toggleCart()">
                    <div class="cart-icon">
                        <i class="fas fa-shopping-bag"></i>
                        <span class="cart-badge" id="cartCount">0</span>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-section">
        <div class="hero-content">
            <div class="glass-card hero-card">
                <span class="premium-badge">✨ مجموعة حصرية 2024</span>
                <h1 class="hero-title">
                    اكتشف عالم<br>
                    <span class="gold-text">العطور الفاخرة</span>
                </h1>
                <p class="hero-description">
                    مجموعة حصرية من أجود العطور العالمية المصممة خصيصاً للأذواق الراقية
                </p>
                <div class="hero-actions">
                    <button class="glass-btn primary-btn" onclick="scrollToSection('products')">
                        <i class="fas fa-shopping-bag"></i>
                        تسوق الآن
                    </button>
                    <button class="glass-btn secondary-btn" onclick="scrollToSection('about')">
                        <i class="fas fa-info-circle"></i>
                        اكتشف المزيد
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
        <div class="features-grid">
            <div class="glass-card feature-card">
                <div class="feature-icon">
                    <i class="fas fa-rocket"></i>
                </div>
                <h3>توصيل سريع</h3>
                <p>توصيل خلال 24 ساعة لجميع المدن</p>
            </div>
            <div class="glass-card feature-card">
                <div class="feature-icon">
                    <i class="fas fa-shield-check"></i>
                </div>
                <h3>منتجات أصلية</h3>
                <p>ضمان الجودة والأصالة 100%</p>
            </div>
            <div class="glass-card feature-card">
                <div class="feature-icon">
                    <i class="fas fa-gift"></i>
                </div>
                <h3>تغليف فاخر</h3>
                <p>تغليف هدايا مميز وأنيق</p>
            </div>
            <div class="glass-card feature-card">
                <div class="feature-icon">
                    <i class="fas fa-headset"></i>
                </div>
                <h3>دعم متواصل</h3>
                <p>خدمة عملاء على مدار الساعة</p>
            </div>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="products-section">
        <div class="section-header">
            <span class="section-badge">منتجاتنا</span>
            <h2 class="section-title">مجموعتنا <span class="gold-text">الفاخرة</span></h2>
            <p class="section-description">اكتشف تشكيلتنا المميزة من أفخم العطور العالمية</p>
        </div>

        <div class="filter-buttons">
            <button class="filter-btn active" onclick="filterProducts('all')">
                <i class="fas fa-th-large"></i> الكل
            </button>
            <button class="filter-btn" onclick="filterProducts('oud')">
                <i class="fas fa-tree"></i> عود
            </button>
            <button class="filter-btn" onclick="filterProducts('musk')">
                <i class="fas fa-feather"></i> مسك
            </button>
            <button class="filter-btn" onclick="filterProducts('floral')">
                <i class="fas fa-flower"></i> زهري
            </button>
            <button class="filter-btn" onclick="filterProducts('oriental')">
                <i class="fas fa-moon"></i> شرقي
            </button>
        </div>

        <div class="products-grid" id="productsGrid">
            <!-- Products loaded dynamically -->
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about-section">
        <div class="about-content">
            <div class="about-text">
                <span class="section-badge">من نحن</span>
                <h2>قصة <span class="gold-text">الفخامة</span></h2>
                <p>نحن نقدم أرقى العطور المستوحاة من التراث العربي الأصيل، نمزج بين العراقة والحداثة لنقدم لكم تجربة فريدة من نوعها في عالم العطور الفاخرة.</p>
                <div class="stats-grid">
                    <div class="glass-card stat-card">
                        <span class="stat-number">+1000</span>
                        <span class="stat-label">عميل سعيد</span>
                    </div>
                    <div class="glass-card stat-card">
                        <span class="stat-number">+500</span>
                        <span class="stat-label">منتج حصري</span>
                    </div>
                    <div class="glass-card stat-card">
                        <span class="stat-number">+50</span>
                        <span class="stat-label">مدينة</span>
                    </div>
                </div>
            </div>
            <div class="about-image">
                <div class="glass-card image-frame">
                    <div class="frame-content">
                        <i class="fas fa-spray-can-sparkles"></i>
                        <span>ROYAL<br>SCENT</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="section-header">
            <span class="section-badge">اتصل بنا</span>
            <h2 class="section-title">تواصل <span class="gold-text">معنا</span></h2>
        </div>
        <form class="glass-card contact-form" id="contactForm">
            <div class="form-row">
                <div class="input-group">
                    <i class="fas fa-user"></i>
                    <input type="text" placeholder="الاسم الكامل" required>
                </div>
                <div class="input-group">
                    <i class="fas fa-envelope"></i>
                    <input type="email" placeholder="البريد الإلكتروني" required>
                </div>
            </div>
            <div class="input-group">
                <i class="fas fa-comment"></i>
                <textarea placeholder="رسالتك..." rows="5" required></textarea>
            </div>
            <button type="submit" class="glass-btn primary-btn">
                <i class="fas fa-paper-plane"></i>
                إرسال الرسالة
            </button>
        </form>
    </section>

    <!-- Admin Lock Button -->
    <button class="admin-trigger" onclick="showAdminLock()" title="لوحة التحكم">
        <i class="fas fa-lock"></i>
    </button>

    <!-- Admin Lock Modal -->
    <div id="adminLockModal" class="modal glass-modal">
        <div class="glass-card lock-card">
            <div class="lock-header">
                <div class="lock-icon">
                    <i class="fas fa-shield-halved"></i>
                </div>
                <h2>لوحة التحكم</h2>
                <p>أدخل رمز الدخول للمتابعة</p>
            </div>
            <div class="pin-input-container">
                <div class="pin-inputs">
                    <input type="password" maxlength="1" class="pin-input" id="pin1" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)">
                    <input type="password" maxlength="1" class="pin-input" id="pin2" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)">
                    <input type="password" maxlength="1" class="pin-input" id="pin3" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)">
                    <input type="password" maxlength="1" class="pin-input" id="pin4" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)">
                </div>
                <div id="pinError" class="pin-error"></div>
            </div>
            <div class="lock-actions">
                <button class="glass-btn secondary-btn" onclick="closeAdminLock()">
                    <i class="fas fa-times"></i>
                    إلغاء
                </button>
                <button class="glass-btn primary-btn" onclick="verifyPin()">
                    <i class="fas fa-arrow-right"></i>
                    دخول
                </button>
            </div>
        </div>
    </div>

    <!-- Admin Panel -->
    <div id="adminPanel" class="admin-panel glass-panel">
        <div class="panel-header">
            <div class="panel-title">
                <i class="fas fa-crown"></i>
                <h2>إدارة المنتجات</h2>
            </div>
            <button class="close-panel" onclick="closeAdminPanel()">
                <i class="fas fa-times"></i>
            </button>
        </div>
        
        <form id="productForm" class="admin-form">
            <!-- صورة المنتج -->
            <div class="form-section">
                <h3><i class="fas fa-image"></i> صورة المنتج</h3>
                <div class="upload-glass" id="uploadArea">
                    <input type="file" id="imageUpload" accept="image/*" hidden onchange="handleImageUpload(event)">
                    <div class="upload-content">
                        <i class="fas fa-cloud-upload-alt upload-main-icon"></i>
                        <p>اسحب وأفلت الصورة هنا</p>
                        <span class="upload-divider">أو</span>
                        <button type="button" class="glass-btn secondary-btn" onclick="document.getElementById('imageUpload').click()">
                            <i class="fas fa-folder-open"></i>
                            اختر صورة
                        </button>
                        <p class="upload-hint">يدعم PNG, JPG, WEBP حتى 10MB</p>
                    </div>
                </div>
                <div id="uploadProgress" class="upload-progress"></div>
                <div id="imagePreview" class="image-preview-glass"></div>
                <input type="hidden" id="productImage" required>
            </div>

            <!-- تفاصيل المنتج -->
            <div class="form-section">
                <h3><i class="fas fa-info-circle"></i> تفاصيل المنتج</h3>
                
                <div class="input-glass">
                    <i class="fas fa-tag"></i>
                    <input type="text" id="productName" placeholder="اسم المنتج" required>
                </div>
                
                <div class="input-glass">
                    <i class="fas fa-money-bill-wave"></i>
                    <input type="number" id="productPrice" placeholder="السعر (ريال)" required>
                </div>
                
                <div class="input-glass">
                    <i class="fas fa-layer-group"></i>
                    <select id="productCategory" required>
                        <option value="">اختر التصنيف...</option>
                        <option value="oud">🪵 عود</option>
                        <option value="musk">🤍 مسك</option>
                        <option value="floral">🌸 زهري</option>
                        <option value="oriental">🌙 شرقي</option>
                    </select>
                </div>
                
                <div class="input-glass">
                    <i class="fas fa-align-left"></i>
                    <textarea id="productDescription" placeholder="وصف المنتج..." rows="4" required></textarea>
                </div>
            </div>

            <!-- أزرار التحكم -->
            <div class="form-actions">
                <button type="submit" class="glass-btn primary-btn">
                    <i class="fas fa-plus-circle"></i>
                    إضافة المنتج
                </button>
                <button type="button" class="glass-btn secondary-btn" onclick="resetAdminForm()">
                    <i class="fas fa-redo"></i>
                    مسح النموذج
                </button>
            </div>
        </form>
    </div>

    <!-- Shopping Cart Modal -->
    <div id="cartModal" class="modal glass-modal">
        <div class="glass-card cart-card">
            <div class="cart-header">
                <h2><i class="fas fa-shopping-bag"></i> سلة التسوق</h2>
                <button class="close-cart" onclick="toggleCart()">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div id="cartItems" class="cart-items">
                <div class="empty-cart-state">
                    <i class="fas fa-shopping-bag"></i>
                    <p>سلة التسوق فارغة</p>
                    <span>ابدأ التسوق وأضف منتجاتك المفضلة</span>
                </div>
            </div>
            <div class="cart-footer">
                <div class="cart-total">
                    <span>المجموع:</span>
                    <span id="cartTotal" class="total-price">0 ريال</span>
                </div>
                <button class="glass-btn primary-btn full-width" onclick="checkout()">
                    <i class="fas fa-credit-card"></i>
                    إتمام الشراء
                </button>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="glass-footer">
        <div class="footer-content">
            <div class="footer-brand">
                <i class="fas fa-crown"></i>
                <h3>ROYAL SCENT</h3>
                <p>متجر العطور الفاخرة</p>
            </div>
            <div class="footer-links">
                <h4>روابط سريعة</h4>
                <a href="#home">الرئيسية</a>
                <a href="#products">المنتجات</a>
                <a href="#about">من نحن</a>
                <a href="#contact">اتصل بنا</a>
            </div>
            <div class="footer-contact">
                <h4>تواصل معنا</h4>
                <p><i class="fas fa-envelope"></i> info@royalscent.com</p>
                <p><i class="fas fa-phone"></i> +966 50 000 0000</p>
                <div class="social-icons">
                    <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
                    <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="social-icon"><i class="fab fa-whatsapp"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2024 ROYAL SCENT - جميع الحقوق محفوظة</p>
        </div>
    </footer>

    <!-- Toast Notifications -->
    <div id="toastContainer" class="toast-container"></div>

    <script src="js/products.js"></script>
    <script src="js/admin.js"></script>
    <script src="js/app.js"></script>
</body>
</html>'''
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ تم إنشاء: index.html")

def create_glass_morphism_css():
    """تنسيقات Glass Morphism الأساسية"""
    css = '''/* ========================================
   GLASS MORPHISM DESIGN SYSTEM
   Ultra Premium Apple Style
   ======================================== */

:root {
    /* Glass Colors */
    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    --glass-blur: blur(20px);
    
    /* Gold Theme */
    --gold: #D4AF37;
    --gold-light: #F4E4C1;
    --gold-dark: #B8960C;
    --gold-gradient: linear-gradient(135deg, #D4AF37 0%, #F4E4C1 50%, #B8960C 100%);
    
    /* Background */
    --bg-primary: #0a0a0a;
    --bg-secondary: #1a1a1a;
    
    /* Text */
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --text-gold: #D4AF37;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Cairo', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    overflow-x: hidden;
    min-height: 100vh;
    position: relative;
}

/* ========================================
   GLASS CARD COMPONENT
   ======================================== */
.glass-card {
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    box-shadow: var(--glass-shadow);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
    border-color: rgba(212, 175, 55, 0.3);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2), 0 0 40px rgba(212, 175, 55, 0.1);
    transform: translateY(-2px);
}

/* ========================================
   GLASS BUTTON
   ======================================== */
.glass-btn {
    padding: 1rem 2rem;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 1px solid var(--glass-border);
    font-family: 'Cairo', sans-serif;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.glass-btn.primary-btn {
    background: var(--gold-gradient);
    color: #000;
    border: none;
    box-shadow: 0 8px 32px rgba(212, 175, 55, 0.3);
}

.glass-btn.primary-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(212, 175, 55, 0.5);
}

.glass-btn.secondary-btn {
    background: rgba(255, 255, 255, 0.05);
    color: var(--text-primary);
}

.glass-btn.secondary-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(212, 175, 55, 0.5);
}

/* ========================================
   GLASS NAVIGATION
   ======================================== */
.glass-nav {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1200px;
    background: var(--glass-bg);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border: 1px solid var(--glass-border);
    border-radius: 50px;
    padding: 1rem 2rem;
    z-index: 1000;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.glass-nav.scrolled {
    top: 10px;
    background: rgba(10, 10, 10, 0.8);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-section {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.logo-icon {
    width: 45px;
    height: 45px;
    background: var(--gold-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #000;
    font-size: 1.3rem;
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.5);
    animation: logoGlow 3s ease-in-out infinite;
}

@keyframes logoGlow {
    0%, 100% { box-shadow: 0 0 20px rgba(212, 175, 55, 0.3); }
    50% { box-shadow: 0 0 40px rgba(212, 175, 55, 0.6); }
}

.logo-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 900;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 2px;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    position: relative;
    padding: 0.5rem 0;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gold-gradient);
    transition: width 0.3s ease;
}

.nav-link:hover,
.nav-link.active {
    color: var(--text-primary);
}

.nav-link:hover::after,
.nav-link.active::after {
    width: 100%;
}

.cart-icon-wrapper {
    position: relative;
    cursor: pointer;
}

.cart-icon {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}

.cart-icon:hover {
    background: rgba(212, 175, 55, 0.2);
    border-color: rgba(212, 175, 55, 0.5);
}

.cart-badge {
    position: absolute;
    top: -5px;
    right: -5px;
    width: 22px;
    height: 22px;
    background: var(--gold-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: bold;
    color: #000;
}

/* ========================================
   GOLD TEXT GRADIENT
   ======================================== */
.gold-text {
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ========================================
   ANIMATIONS
   ======================================== */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

.animate-fadeInUp {
    animation: fadeInUp 0.6s ease forwards;
}

/* ========================================
   SCROLLBAR STYLING
   ======================================== */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
}

::-webkit-scrollbar-thumb {
    background: var(--gold-gradient);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--gold-light);
}
'''
    
    with open('css/glass-morphism.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/glass-morphism.css")

def create_bubbles_css():
    """خلفية الفقاعات المتحركة"""
    css = '''/* ========================================
   ANIMATED BUBBLES BACKGROUND
   ======================================== */

.bubbles-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.bubble {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, 
        rgba(255, 255, 255, 0.1),
        rgba(212, 175, 55, 0.05),
        transparent 70%);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(5px);
    animation: floatBubble linear infinite;
}

.bubble-1 { width: 150px; height: 150px; left: 10%; animation-duration: 15s; animation-delay: 0s; }
.bubble-2 { width: 100px; height: 100px; left: 25%; animation-duration: 18s; animation-delay: 2s; }
.bubble-3 { width: 200px; height: 200px; left: 40%; animation-duration: 20s; animation-delay: 4s; }
.bubble-4 { width: 120px; height: 120px; left: 55%; animation-duration: 16s; animation-delay: 1s; }
.bubble-5 { width: 80px; height: 80px; left: 70%; animation-duration: 22s; animation-delay: 3s; }
.bubble-6 { width: 180px; height: 180px; left: 85%; animation-duration: 19s; animation-delay: 5s; }
.bubble-7 { width: 90px; height: 90px; left: 15%; animation-duration: 17s; animation-delay: 2.5s; }
.bubble-8 { width: 160px; height: 160px; left: 50%; animation-duration: 21s; animation-delay: 1.5s; }
.bubble-9 { width: 110px; height: 110px; left: 75%; animation-duration: 23s; animation-delay: 3.5s; }
.bubble-10 { width: 140px; height: 140px; left: 35%; animation-duration: 24s; animation-delay: 4.5s; }

@keyframes floatBubble {
    0% {
        transform: translateY(100vh) scale(0);
        opacity: 0;
    }
    10% {
        opacity: 0.8;
    }
    50% {
        transform: translateY(50vh) translateX(50px) scale(1);
        opacity: 0.6;
    }
    90% {
        opacity: 0.2;
    }
    100% {
        transform: translateY(-20vh) translateX(-50px) scale(0.5);
        opacity: 0;
    }
}

/* Floating Particles */
.particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: var(--gold);
    border-radius: 50%;
    animation: particleFloat linear infinite;
    box-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
}

@keyframes particleFloat {
    0% {
        transform: translateY(100vh) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    90% {
        opacity: 0.5;
    }
    100% {
        transform: translateY(-20vh) rotate(720deg);
        opacity: 0;
    }
}
'''
    
    with open('css/bubbles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/bubbles.css")

def create_style_css():
    """تنسيقات الموقع الرئيسية"""
    css = '''/* ========================================
   MAIN STYLES - ROYAL SCENT
   ======================================== */

/* Hero Section */
.hero-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    position: relative;
    z-index: 1;
}

.hero-card {
    max-width: 700px;
    padding: 4rem;
    text-align: center;
    animation: fadeInUp 1s ease;
}

.premium-badge {
    display: inline-block;
    padding: 0.5rem 2rem;
    background: rgba(212, 175, 55, 0.15);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 50px;
    color: var(--gold);
    font-weight: 600;
    margin-bottom: 2rem;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    margin-bottom: 1.5rem;
    line-height: 1.3;
}

.hero-description {
    color: var(--text-secondary);
    font-size: 1.2rem;
    margin-bottom: 2.5rem;
    line-height: 1.8;
}

.hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

/* Features Section */
.features-section {
    padding: 5rem 2rem;
    position: relative;
    z-index: 1;
}

.features-grid {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.feature-card {
    padding: 2.5rem;
    text-align: center;
    animation: fadeInUp 0.6s ease forwards;
    animation-delay: calc(var(--i) * 0.1s);
}

.feature-icon {
    width: 70px;
    height: 70px;
    margin: 0 auto 1.5rem;
    background: var(--gold-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    color: #000;
}

.feature-card h3 {
    margin-bottom: 0.5rem;
    font-size: 1.3rem;
}

.feature-card p {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* Products Section */
.products-section {
    padding: 5rem 2rem;
    position: relative;
    z-index: 1;
}

.section-header {
    text-align: center;
    margin-bottom: 3rem;
}

.section-badge {
    display: inline-block;
    padding: 0.5rem 1.5rem;
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid rgba(212, 175, 55, 0.2);
    border-radius: 50px;
    color: var(--gold);
    font-weight: 600;
    margin-bottom: 1rem;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    margin-bottom: 1rem;
}

.section-description {
    color: var(--text-secondary);
    font-size: 1.1rem;
}

.filter-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 0.8rem 1.5rem;
    border-radius: 50px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: 'Cairo', sans-serif;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    backdrop-filter: blur(10px);
}

.filter-btn.active,
.filter-btn:hover {
    background: var(--gold-gradient);
    color: #000;
    border-color: transparent;
}

.products-grid {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
}

.product-card {
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease forwards;
}

.product-badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    padding: 0.3rem 1rem;
    background: var(--gold-gradient);
    color: #000;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 700;
    z-index: 2;
}

.product-image-wrapper {
    position: relative;
    overflow: hidden;
    border-radius: 20px 20px 0 0;
}

.product-image {
    width: 100%;
    height: 350px;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.product-card:hover .product-image {
    transform: scale(1.1);
}

.product-info {
    padding: 1.5rem;
}

.product-name {
    font-size: 1.5rem;
    color: var(--gold);
    margin-bottom: 0.5rem;
}

.product-description {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.product-price {
    font-size: 2rem;
    font-weight: 900;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.product-actions {
    display: flex;
    gap: 0.5rem;
}

.product-actions .glass-btn {
    flex: 1;
    padding: 0.8rem;
    font-size: 0.9rem;
    justify-content: center;
}

/* About Section */
.about-section {
    padding: 5rem 2rem;
    position: relative;
    z-index: 1;
}

.about-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

.about-text h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.about-text p {
    color: var(--text-secondary);
    line-height: 1.8;
    margin-bottom: 2rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}

.stat-card {
    text-align: center;
    padding: 1.5rem;
}

.stat-number {
    font-size: 1.8rem;
    font-weight: 900;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block;
}

.stat-label {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.image-frame {
    height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.frame-content {
    text-align: center;
    font-size: 2rem;
    color: var(--gold);
}

.frame-content i {
    font-size: 5rem;
    margin-bottom: 1rem;
}

/* Contact Section */
.contact-section {
    padding: 5rem 2rem;
    position: relative;
    z-index: 1;
}

.contact-form {
    max-width: 600px;
    margin: 0 auto;
    padding: 3rem;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
}

.input-group {
    position: relative;
    margin-bottom: 1rem;
}

.input-group i {
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
}

.input-group input,
.input-group textarea {
    width: 100%;
    padding: 1rem 3rem 1rem 1rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    border-radius: 15px;
    color: var(--text-primary);
    font-family: 'Cairo', sans-serif;
    transition: all 0.3s ease;
}

.input-group input:focus,
.input-group textarea:focus {
    outline: none;
    border-color: var(--gold);
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.1);
}

/* Footer */
.glass-footer {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border-top: 1px solid var(--glass-border);
    padding: 4rem 2rem 2rem;
    position: relative;
    z-index: 1;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.footer-brand i {
    font-size: 2rem;
    color: var(--gold);
}

.social-icons {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.social-icon {
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-secondary);
    transition: all 0.3s ease;
    text-decoration: none;
}

.social-icon:hover {
    background: var(--gold-gradient);
    color: #000;
    border-color: transparent;
}

.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    margin-top: 2rem;
    border-top: 1px solid var(--glass-border);
    color: var(--text-secondary);
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    z-index: 2000;
    align-items: center;
    justify-content: center;
}

.modal.active {
    display: flex;
}

/* Toast Notifications */
.toast-container {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 3000;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.toast {
    padding: 1rem 2rem;
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: 15px;
    color: var(--text-primary);
    animation: slideInRight 0.3s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.toast.success {
    border-color: rgba(76, 175, 80, 0.5);
}

.toast.error {
    border-color: rgba(244, 67, 54, 0.5);
}

@keyframes slideInRight {
    from {
        transform: translateX(100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

/* Full Width */
.full-width {
    width: 100%;
    justify-content: center;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2.5rem;
    }
    
    .about-content {
        grid-template-columns: 1fr;
    }
    
    .products-grid {
        grid-template-columns: 1fr;
    }
    
    .form-row {
        grid-template-columns: 1fr;
    }
    
    .glass-nav {
        width: 95%;
        padding: 0.8rem 1rem;
    }
}
'''
    
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/style.css")

def create_admin_css():
    """تنسيقات لوحة التحكم وقفل PIN"""
    css = '''/* ========================================
   ADMIN PANEL & PIN LOCK STYLES
   ======================================== */

/* Admin Trigger Button */
.admin-trigger {
    position: fixed;
    bottom: 30px;
    left: 30px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 2px solid var(--glass-border);
    color: var(--gold);
    font-size: 1.5rem;
    cursor: pointer;
    z-index: 999;
    transition: all 0.3s ease;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.admin-trigger:hover {
    transform: scale(1.1);
    border-color: var(--gold);
    box-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
}

/* PIN Lock Modal */
.glass-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    z-index: 2000;
    align-items: center;
    justify-content: center;
}

.glass-modal.active {
    display: flex;
}

.lock-card {
    width: 90%;
    max-width: 450px;
    padding: 3rem;
    text-align: center;
    animation: scaleIn 0.3s ease;
}

@keyframes scaleIn {
    from {
        transform: scale(0.9);
        opacity: 0;
    }
    to {
        transform: scale(1);
        opacity: 1;
    }
}

.lock-header {
    margin-bottom: 2rem;
}

.lock-icon {
    width: 80px;
    height: 80px;
    margin: 0 auto 1.5rem;
    background: var(--gold-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: #000;
    box-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

.lock-header h2 {
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
}

.lock-header p {
    color: var(--text-secondary);
}

/* PIN Input */
.pin-input-container {
    margin-bottom: 2rem;
}

.pin-inputs {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-bottom: 1rem;
}

.pin-input {
    width: 60px;
    height: 60px;
    text-align: center;
    font-size: 1.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: 2px solid var(--glass-border);
    border-radius: 15px;
    color: var(--text-primary);
    transition: all 0.3s ease;
    font-family: 'Cairo', sans-serif;
}

.pin-input:focus {
    outline: none;
    border-color: var(--gold);
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
}

.pin-input.filled {
    background: rgba(212, 175, 55, 0.1);
    border-color: var(--gold);
}

.pin-error {
    color: #f44336;
    font-size: 0.9rem;
    min-height: 20px;
}

.lock-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

/* Admin Panel */
.admin-panel {
    position: fixed;
    top: 0;
    left: -100%;
    width: 100%;
    max-width: 500px;
    height: 100vh;
    background: rgba(10, 10, 10, 0.95);
    backdrop-filter: blur(30px);
    border-right: 1px solid var(--glass-border);
    z-index: 2001;
    transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    overflow-y: auto;
}

.admin-panel.active {
    left: 0;
}

.panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    border-bottom: 1px solid var(--glass-border);
    position: sticky;
    top: 0;
    background: rgba(10, 10, 10, 0.95);
    backdrop-filter: blur(30px);
    z-index: 10;
}

.panel-title {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--gold);
}

.close-panel {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.close-panel:hover {
    background: rgba(244, 67, 54, 0.2);
    border-color: #f44336;
    color: #f44336;
}

/* Admin Form */
.admin-form {
    padding: 1.5rem;
}

.form-section {
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
}

.form-section h3 {
    margin-bottom: 1.5rem;
    color: var(--gold);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
}

/* Upload Area */
.upload-glass {
    border: 2px dashed rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    background: rgba(255, 255, 255, 0.02);
}

.upload-glass:hover,
.upload-glass.highlight {
    border-color: var(--gold);
    background: rgba(212, 175, 55, 0.05);
}

.upload-main-icon {
    font-size: 3rem;
    color: var(--gold);
    margin-bottom: 1rem;
}

.upload-divider {
    display: block;
    margin: 0.5rem 0;
    color: var(--text-secondary);
}

.upload-hint {
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
}

.upload-progress {
    margin-top: 1rem;
}

.image-preview-glass {
    margin-top: 1rem;
    border-radius: 15px;
    overflow: hidden;
    border: 1px solid var(--glass-border);
}

.image-preview-glass img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

/* Input Glass */
.input-glass {
    position: relative;
    margin-bottom: 1rem;
}

.input-glass i {
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    z-index: 1;
}

.input-glass input,
.input-glass select,
.input-glass textarea {
    width: 100%;
    padding: 1rem 3rem 1rem 1rem;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--glass-border);
    border-radius: 15px;
    color: var(--text-primary);
    font-family: 'Cairo', sans-serif;
    transition: all 0.3s ease;
}

.input-glass select {
    cursor: pointer;
}

.input-glass select option {
    background: #1a1a1a;
    color: var(--text-primary);
}

.input-glass input:focus,
.input-glass select:focus,
.input-glass textarea:focus {
    outline: none;
    border-color: var(--gold);
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.1);
}

.input-glass textarea {
    resize: vertical;
    min-height: 100px;
}

/* Form Actions */
.form-actions {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}

.form-actions .glass-btn {
    flex: 1;
    justify-content: center;
}

/* Cart Styles */
.cart-card {
    width: 90%;
    max-width: 500px;
    max-height: 80vh;
    overflow-y: auto;
    animation: scaleIn 0.3s ease;
}

.cart-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    border-bottom: 1px solid var(--glass-border);
}

.cart-header h2 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--gold);
}

.close-cart {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

.cart-items {
    padding: 1.5rem;
}

.empty-cart-state {
    text-align: center;
    padding: 3rem;
    color: var(--text-secondary);
}

.empty-cart-state i {
    font-size: 4rem;
    color: var(--gold);
    margin-bottom: 1rem;
    opacity: 0.5;
}

.cart-footer {
    padding: 1.5rem;
    border-top: 1px solid var(--glass-border);
}

.cart-total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.total-price {
    font-weight: 900;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

@media (max-width: 768px) {
    .admin-panel {
        max-width: 100%;
    }
    
    .pin-inputs {
        gap: 0.5rem;
    }
    
    .pin-input {
        width: 50px;
        height: 50px;
        font-size: 1.2rem;
    }
}
'''
    
    with open('css/admin.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/admin.css")

def create_products_js():
    """ملف المنتجات"""
    js = '''// Products Database
const productsDB = [
    {
        id: 1,
        name: "عطر رويال عود",
        price: 1200,
        category: "oud",
        description: "عطر فاخر يجمع بين خشب العود الطبيعي والمسك الأبيض مع لمسات من الورد الطائفي",
        image: "https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/royal-oud",
        badge: "الأكثر مبيعاً"
    },
    {
        id: 2,
        name: "عطر ديوان المسك",
        price: 950,
        category: "musk",
        description: "مزيج ساحر من المسك الأبيض والعنبر مع نغمات الفانيليا والزعفران",
        image: "https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/diwan-musk",
        badge: "جديد"
    },
    {
        id: 3,
        name: "عطر أميري",
        price: 1500,
        category: "oud",
        description: "تركيبة ملكية من العود الكمبودي والورد البلغاري مع خشب الصندل",
        image: "https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/amiri",
        badge: "حصري"
    },
    {
        id: 4,
        name: "عطر ليالي الشرق",
        price: 850,
        category: "oriental",
        description: "عطر شرقي أصيل يمزج بين الياسمين والعنبر مع قاعدة من الباتشولي",
        image: "https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/oriental-nights",
        badge: ""
    },
    {
        id: 5,
        name: "عطر زهور الربيع",
        price: 750,
        category: "floral",
        description: "باقة من أزهار الربيع مع لمسات من الفواكه المنعشة والمسك الأبيض",
        image: "https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/spring-flowers",
        badge: ""
    },
    {
        id: 6,
        name: "عطر المسك الأبيض",
        price: 1100,
        category: "musk",
        description: "مسك أبيض نقي مع لمسات من العنبر والورد الجوري",
        image: "https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/white-musk",
        badge: "مميز"
    }
];

let products = JSON.parse(localStorage.getItem('royalProducts')) || productsDB;
let cart = JSON.parse(localStorage.getItem('royalCart')) || [];

function saveProducts() {
    localStorage.setItem('royalProducts', JSON.stringify(products));
}

function saveCart() {
    localStorage.setItem('royalCart', JSON.stringify(cart));
}

function displayProducts(filterCategory = 'all') {
    const grid = document.getElementById('productsGrid');
    if (!grid) return;
    
    const filtered = filterCategory === 'all' 
        ? products 
        : products.filter(p => p.category === filterCategory);
    
    grid.innerHTML = filtered.map(product => `
        <div class="glass-card product-card">
            ${product.badge ? `<span class="product-badge">${product.badge}</span>` : ''}
            <div class="product-image-wrapper">
                <img src="${product.image}" alt="${product.name}" class="product-image" 
                     onerror="this.src='https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/placeholder'">
            </div>
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                <p class="product-description">${product.description}</p>
                <div class="product-price">${product.price} ريال</div>
                <div class="product-actions">
                    <button class="glass-btn primary-btn" onclick="addToCart(${product.id})">
                        <i class="fas fa-shopping-cart"></i> إضافة للسلة
                    </button>
                    <a href="${product.image}" download class="glass-btn secondary-btn" title="تحميل الصورة">
                        <i class="fas fa-download"></i>
                    </a>
                </div>
            </div>
        </div>
    `).join('');
}

function filterProducts(category) {
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    event.target.closest('.filter-btn').classList.add('active');
    displayProducts(category);
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push({...product});
        saveCart();
        updateCartCount();
        showToast('✅ تمت إضافة المنتج إلى السلة', 'success');
    }
}

function updateCartCount() {
    const count = document.getElementById('cartCount');
    if (count) {
        count.textContent = cart.length;
    }
}

function toggleCart() {
    const modal = document.getElementById('cartModal');
    modal.classList.toggle('active');
    if (modal.classList.contains('active')) {
        displayCartItems();
    }
}

function displayCartItems() {
    const container = document.getElementById('cartItems');
    const total = document.getElementById('cartTotal');
    
    if (!container || !total) return;
    
    if (cart.length === 0) {
        container.innerHTML = `
            <div class="empty-cart-state">
                <i class="fas fa-shopping-bag"></i>
                <p>سلة التسوق فارغة</p>
                <span>ابدأ التسوق وأضف منتجاتك المفضلة</span>
            </div>`;
        total.textContent = '0 ريال';
        return;
    }
    
    container.innerHTML = cart.map((item, index) => `
        <div style="display: flex; gap: 1rem; padding: 1rem; margin-bottom: 0.5rem; 
                    background: rgba(255,255,255,0.03); border-radius: 15px; border: 1px solid rgba(255,255,255,0.05);">
            <img src="${item.image}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 10px;"
                 onerror="this.src='https://res.cloudinary.com/dmla61v7n/image/upload/v1/perfume-store/placeholder'">
            <div style="flex: 1;">
                <strong style="color: var(--gold);">${item.name}</strong>
                <p style="color: var(--text-secondary); font-size: 0.9rem;">${item.price} ريال</p>
            </div>
            <button onclick="removeFromCart(${index})" 
                    style="background: none; border: none; color: #f44336; cursor: pointer; padding: 0.5rem;">
                <i class="fas fa-trash"></i>
            </button>
        </div>
    `).join('');
    
    const sum = cart.reduce((s, item) => s + item.price, 0);
    total.textContent = `${sum} ريال`;
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
    updateCartCount();
    displayCartItems();
    showToast('🗑️ تم حذف المنتج', 'error');
}

function checkout() {
    if (cart.length === 0) {
        showToast('⚠️ السلة فارغة', 'error');
        return;
    }
    const total = cart.reduce((s, item) => s + item.price, 0);
    alert(`🛍️ شكراً لتسوقك مع ROYAL SCENT!\\n💰 المجموع: ${total} ريال\\n📦 عدد المنتجات: ${cart.length}\\n\\nسيتم التواصل معك لتأكيد الطلب`);
    cart = [];
    saveCart();
    updateCartCount();
    toggleCart();
    showToast('🎉 تم إتمام الطلب بنجاح!', 'success');
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    displayProducts();
    updateCartCount();
});
'''
    
    with open('js/products.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✅ تم إنشاء: js/products.js")

def create_admin_js():
    """ملف لوحة التحكم مع PIN"""
    js = '''// Admin Security
const ADMIN_PIN = '1234';

function showAdminLock() {
    document.getElementById('adminLockModal').classList.add('active');
    document.getElementById('pin1').focus();
    document.querySelectorAll('.pin-input').forEach(input => {
        input.value = '';
        input.classList.remove('filled');
    });
    document.getElementById('pinError').textContent = '';
}

function closeAdminLock() {
    document.getElementById('adminLockModal').classList.remove('active');
}

function pinInput(input) {
    if (input.value) {
        input.classList.add('filled');
        const next = input.nextElementSibling;
        if (next && next.classList.contains('pin-input')) {
            next.focus();
        }
    } else {
        input.classList.remove('filled');
    }
}

function handlePinKey(event, input) {
    if (event.key === 'Backspace' && !input.value) {
        const prev = input.previousElementSibling;
        if (prev && prev.classList.contains('pin-input')) {
            prev.focus();
        }
    }
    if (event.key === 'Enter') {
        verifyPin();
    }
}

function verifyPin() {
    const pin = Array.from(document.querySelectorAll('.pin-input'))
        .map(input => input.value)
        .join('');
    
    if (pin === ADMIN_PIN) {
        document.getElementById('adminLockModal').classList.remove('active');
        document.getElementById('adminPanel').classList.add('active');
        showToast('✅ تم الدخول إلى لوحة التحكم', 'success');
    } else {
        document.getElementById('pinError').textContent = '❌ رمز الدخول غير صحيح';
        document.querySelectorAll('.pin-input').forEach(input => {
            input.value = '';
            input.classList.remove('filled');
        });
        document.getElementById('pin1').focus();
        showToast('❌ رمز خاطئ! الرجاء المحاولة مرة أخرى', 'error');
    }
}

function closeAdminPanel() {
    document.getElementById('adminPanel').classList.remove('active');
    showToast('👋 تم الخروج من لوحة التحكم', 'success');
}

// Cloudinary Upload
async function handleImageUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const uploadArea = document.getElementById('uploadArea');
    const progress = document.getElementById('uploadProgress');
    const preview = document.getElementById('imagePreview');

    uploadArea.style.opacity = '0.5';
    progress.innerHTML = '<div style="color: var(--gold);"><i class="fas fa-spinner fa-spin"></i> جاري رفع الصورة...</div>';

    const formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', 'perfume-store');
    formData.append('cloud_name', 'dmla61v7n');

    try {
        const response = await fetch('https://api.cloudinary.com/v1_1/dmla61v7n/image/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        document.getElementById('productImage').value = data.secure_url;
        preview.innerHTML = `<img src="${data.secure_url}" alt="Preview">`;
        progress.innerHTML = '<div style="color: #4CAF50;"><i class="fas fa-check-circle"></i> ✅ تم رفع الصورة بنجاح!</div>';
        showToast('✅ تم رفع الصورة بنجاح!', 'success');
    } catch (error) {
        progress.innerHTML = '<div style="color: #f44336;"><i class="fas fa-times-circle"></i> ❌ فشل رفع الصورة</div>';
        showToast('❌ فشل رفع الصورة', 'error');
    } finally {
        uploadArea.style.opacity = '1';
    }
}

// Add Product
document.getElementById('productForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const newProduct = {
        id: Date.now(),
        name: document.getElementById('productName').value,
        price: parseInt(document.getElementById('productPrice').value),
        category: document.getElementById('productCategory').value,
        description: document.getElementById('productDescription').value,
        image: document.getElementById('productImage').value,
        badge: 'جديد'
    };
    
    products.push(newProduct);
    saveProducts();
    displayProducts();
    resetAdminForm();
    showToast('🎉 تم إضافة المنتج بنجاح!', 'success');
});

function resetAdminForm() {
    document.getElementById('productForm').reset();
    document.getElementById('imagePreview').innerHTML = '';
    document.getElementById('uploadProgress').innerHTML = '';
    document.getElementById('uploadArea').style.opacity = '1';
}

// Toast System
function showToast(message, type = '') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'slideInRight 0.3s ease reverse';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}
'''
    
    with open('js/admin.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✅ تم إنشاء: js/admin.js")

def create_app_js():
    """ملف التطبيق الرئيسي"""
    js = '''// Main Application
document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

function initApp() {
    // Navbar scroll
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.glass-nav');
        if (window.scrollY > 100) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Close modals on outside click
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('glass-modal')) {
            e.target.classList.remove('active');
        }
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal.active').forEach(m => m.classList.remove('active'));
        }
    });

    // Contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            showToast('✅ تم إرسال رسالتك بنجاح!', 'success');
            contactForm.reset();
        });
    }

    // Drag and drop for upload
    const uploadArea = document.getElementById('uploadArea');
    if (uploadArea) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, preventDefaults);
        });
        
        ['dragenter', 'dragover'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => uploadArea.classList.add('highlight'));
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => uploadArea.classList.remove('highlight'));
        });
        
        uploadArea.addEventListener('drop', (e) => {
            const file = e.dataTransfer.files[0];
            if (file && file.type.startsWith('image/')) {
                const input = document.getElementById('imageUpload');
                const dt = new DataTransfer();
                dt.items.add(file);
                input.files = dt.files;
                input.dispatchEvent(new Event('change'));
            }
        });
    }
}

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}
'''
    
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✅ تم إنشاء: js/app.js")

def main():
    print("🌟 بدء إنشاء متجر ROYAL SCENT الفاخر...")
    print("=" * 50)
    
    create_directory_structure()
    create_index_html()
    create_glass_morphism_css()
    create_bubbles_css()
    create_style_css()
    create_admin_css()
    create_products_js()
    create_admin_js()
    create_app_js()
    
    print("=" * 50)
    print("🎉 تم إنشاء جميع الملفات بنجاح!")
    print("🔐 رمز الدخول للوحة التحكم: 1234")
    print("📁 الملفات المنشأة:")
    print("   ├── index.html")
    print("   ├── css/glass-morphism.css")
    print("   ├── css/bubbles.css")
    print("   ├── css/style.css")
    print("   ├── css/admin.css")
    print("   ├── js/products.js")
    print("   ├── js/admin.js")
    print("   └── js/app.js")
    print("=" * 50)

if __name__ == "__main__":
    main()
