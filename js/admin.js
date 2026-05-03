// Admin Security
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
