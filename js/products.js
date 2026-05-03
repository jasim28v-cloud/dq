// Products Database
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
    alert(`🛍️ شكراً لتسوقك مع ROYAL SCENT!\n💰 المجموع: ${total} ريال\n📦 عدد المنتجات: ${cart.length}\n\nسيتم التواصل معك لتأكيد الطلب`);
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
