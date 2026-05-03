# scraper.py - VK Clone Generator (Complete)
import json
import os
import shutil
from datetime import datetime

def generate_vk_site():
    """توليد موقع VK كامل"""
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # ========== 1. FIREBASE CONFIG ==========
    firebase_js = '''// firebase.js - إعدادات Firebase + Cloudinary
const firebaseConfig = {
    apiKey: "AIzaSyCFTMtaIp9ld3UKmscT8MBxfCKh5_-fOcM",
    authDomain: "amre-3fae9.firebaseapp.com",
    databaseURL: "https://amre-3fae9-default-rtdb.firebaseio.com",
    projectId: "amre-3fae9",
    storageBucket: "amre-3fae9.firebasestorage.app",
    messagingSenderId: "573470407576",
    appId: "1:573470407576:web:3a24d023cbb10d6ce309ed"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const cloudinaryConfig = {
    cloudName: "da457cqma",
    uploadPreset: "do33_x"
};

const ADMIN_EMAIL = "jasim28v@gmail.com";
let currentUser = null;
'''
    
    # ========== 2. CSS ==========
    css = '''/* style.css - VK Ultra Glass Design */
:root {
    --vk-blue: #4a76a8;
    --vk-dark: #1a1a2e;
    --vk-glass: rgba(255,255,255,0.05);
    --vk-glass-hover: rgba(255,255,255,0.12);
    --vk-border: rgba(255,255,255,0.06);
    --vk-text: #e2e8f0;
    --vk-text-secondary: #94a3b8;
    --aurora-1: rgba(74,118,168,0.15);
    --aurora-2: rgba(99,102,241,0.1);
    --aurora-3: rgba(168,85,247,0.08);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: 'Tajawal', sans-serif;
    background: #0a0a1a;
    min-height: 100vh;
    color: var(--vk-text);
    display: flex;
}
.sidebar {
    width: 250px;
    height: 100vh;
    position: fixed;
    right: 0;
    top: 0;
    background: rgba(10,10,26,0.8);
    backdrop-filter: blur(40px);
    border-left: 1px solid var(--vk-border);
    padding: 20px 15px;
    z-index: 100;
    overflow-y: auto;
}
.sidebar-logo {
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(135deg, #4a76a8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 30px;
    text-align: center;
}
.sidebar-nav { list-style: none; }
.sidebar-nav li { margin-bottom: 5px; }
.sidebar-nav a {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 15px;
    border-radius: 12px;
    color: var(--vk-text-secondary);
    text-decoration: none;
    transition: all 0.3s;
    font-size: 14px;
}
.sidebar-nav a:hover, .sidebar-nav a.active {
    background: var(--vk-glass-hover);
    color: white;
}
.sidebar-nav a.active { background: rgba(74,118,168,0.2); border-right: 3px solid var(--vk-blue); }
.main-content {
    flex: 1;
    margin-right: 250px;
    padding: 20px;
    min-height: 100vh;
}
.header {
    background: rgba(10,10,26,0.6);
    backdrop-filter: blur(40px);
    border: 1px solid var(--vk-border);
    border-radius: 16px;
    padding: 15px 20px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.header-search {
    background: var(--vk-glass);
    border: 1px solid var(--vk-border);
    border-radius: 12px;
    padding: 10px 15px;
    color: white;
    width: 300px;
    outline: none;
}
.header-search::placeholder { color: #64748b; }
.header-user { display: flex; align-items: center; gap: 10px; }
.header-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--vk-blue);
    cursor: pointer;
}
.card {
    background: rgba(255,255,255,0.02);
    backdrop-filter: blur(30px);
    border: 1px solid var(--vk-border);
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 20px;
    transition: all 0.4s;
}
.card:hover {
    background: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.12);
}
.card-header { display: flex; align-items: center; gap: 12px; margin-bottom: 15px; }
.card-avatar { width: 45px; height: 45px; border-radius: 50%; object-fit: cover; }
.card-name { font-weight: 700; color: white; }
.card-time { font-size: 11px; color: #64748b; }
.post-text { color: #cbd5e1; line-height: 1.8; margin-bottom: 15px; }
.post-image { width: 100%; max-height: 400px; object-fit: cover; border-radius: 12px; margin-bottom: 15px; }
.post-actions { display: flex; gap: 20px; padding-top: 15px; border-top: 1px solid var(--vk-border); }
.post-actions button {
    background: none;
    border: none;
    color: var(--vk-text-secondary);
    cursor: pointer;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 5px;
    transition: all 0.3s;
}
.post-actions button:hover { color: var(--vk-blue); }
.btn {
    padding: 10px 20px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    font-family: 'Tajawal', sans-serif;
    font-size: 14px;
    transition: all 0.3s;
}
.btn-primary { background: linear-gradient(135deg, #4a76a8, #6366f1); color: white; }
.btn-primary:hover { box-shadow: 0 8px 30px rgba(74,118,168,0.4); transform: translateY(-2px); }
.btn-glass { background: var(--vk-glass); border: 1px solid var(--vk-border); color: var(--vk-text-secondary); }
.btn-glass:hover { background: var(--vk-glass-hover); color: white; }
.modal {
    display: none;
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(5px);
    z-index: 1000;
    align-items: center;
    justify-content: center;
}
.modal.active { display: flex; }
.modal-content {
    background: rgba(20,20,40,0.95);
    backdrop-filter: blur(40px);
    border: 1px solid var(--vk-border);
    border-radius: 24px;
    padding: 30px;
    width: 90%;
    max-width: 450px;
}
.modal-title { font-size: 22px; font-weight: 700; margin-bottom: 20px; text-align: center; }
.input {
    width: 100%;
    padding: 12px 15px;
    background: var(--vk-glass);
    border: 1px solid var(--vk-border);
    border-radius: 12px;
    color: white;
    margin-bottom: 12px;
    outline: none;
    font-family: 'Tajawal', sans-serif;
}
.input:focus { border-color: var(--vk-blue); }
.toast {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(20,20,40,0.9);
    backdrop-filter: blur(20px);
    border: 1px solid var(--vk-border);
    padding: 12px 25px;
    border-radius: 30px;
    font-size: 14px;
    opacity: 0;
    transition: all 0.3s;
    pointer-events: none;
    z-index: 9999;
}
.toast.show { opacity: 1; }
.auth-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle at 30% 20%, var(--aurora-1), transparent 70%),
                radial-gradient(circle at 70% 80%, var(--aurora-2), transparent 70%);
}
.auth-card {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(40px);
    border: 1px solid var(--vk-border);
    border-radius: 28px;
    padding: 40px;
    width: 90%;
    max-width: 420px;
}
.auth-logo {
    font-size: 36px;
    font-weight: 900;
    background: linear-gradient(135deg, #4a76a8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 30px;
}
@media (max-width: 768px) {
    .sidebar { width: 70px; padding: 15px 5px; }
    .sidebar-logo { font-size: 20px; }
    .sidebar-nav a span { display: none; }
    .sidebar-nav a { justify-content: center; padding: 12px; }
    .main-content { margin-right: 70px; }
}
'''
    
    # ========== 3. LOGIN ==========
    login_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VK - تسجيل الدخول</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body class="auth-container">
    <div class="auth-card">
        <div class="auth-logo">VK</div>
        <h2 style="text-align:center;margin-bottom:20px;color:#94a3b8;">تسجيل الدخول</h2>
        <input type="email" id="email" class="input" placeholder="البريد الإلكتروني">
        <input type="password" id="password" class="input" placeholder="كلمة المرور">
        <button onclick="login()" class="btn btn-primary" style="width:100%;margin-top:10px;">
            <i class="fas fa-sign-in-alt ml-2"></i> دخول
        </button>
        <p style="text-align:center;margin-top:20px;color:#64748b;">
            ليس لديك حساب؟ <a href="register.html" style="color:#4a76a8;">اشترك الآن</a>
        </p>
    </div>
    <script src="firebase.js"></script>
    <script>
        function login() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            auth.signInWithEmailAndPassword(email, password)
                .then(() => { window.location.href = 'index.html'; })
                .catch(err => { alert('خطأ: ' + err.message); });
        }
    </script>
</body>
</html>'''
    
    # ========== 4. REGISTER ==========
    register_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VK - اشتراك جديد</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body class="auth-container">
    <div class="auth-card">
        <div class="auth-logo">VK</div>
        <h2 style="text-align:center;margin-bottom:20px;color:#94a3b8;">اشتراك جديد</h2>
        <input type="text" id="name" class="input" placeholder="الاسم الكامل">
        <input type="email" id="email" class="input" placeholder="البريد الإلكتروني">
        <input type="password" id="password" class="input" placeholder="كلمة المرور">
        <input type="file" id="photo" class="input" accept="image/*" style="padding:8px;">
        <button onclick="register()" class="btn btn-primary" style="width:100%;margin-top:10px;">
            <i class="fas fa-user-plus ml-2"></i> اشتراك
        </button>
        <p style="text-align:center;margin-top:20px;color:#64748b;">
            لديك حساب؟ <a href="login.html" style="color:#4a76a8;">تسجيل الدخول</a>
        </p>
    </div>
    <script src="firebase.js"></script>
    <script>
        async function register() {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const photoFile = document.getElementById('photo').files[0];
            if (!name || !email || !password) { alert('الرجاء ملء جميع الحقول'); return; }
            try {
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const user = userCredential.user;
                let photoURL = '';
                if (photoFile) {
                    const formData = new FormData();
                    formData.append('file', photoFile);
                    formData.append('upload_preset', cloudinaryConfig.uploadPreset);
                    const res = await fetch(`https://api.cloudinary.com/v1_1/${cloudinaryConfig.cloudName}/image/upload`, { method: 'POST', body: formData });
                    const data = await res.json();
                    photoURL = data.secure_url;
                }
                await db.ref('users/' + user.uid).set({
                    name: name, email: email, photo: photoURL,
                    role: email === ADMIN_EMAIL ? 'admin' : 'user',
                    created_at: new Date().toISOString()
                });
                window.location.href = 'index.html';
            } catch (err) { alert('خطأ: ' + err.message); }
        }
    </script>
</body>
</html>'''
    
    # ========== 5. INDEX ==========
    index_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VK - الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <aside class="sidebar">
        <div class="sidebar-logo">VK</div>
        <ul class="sidebar-nav">
            <li><a href="index.html" class="active"><i class="fas fa-home"></i> <span>الرئيسية</span></a></li>
            <li><a href="profile.html"><i class="fas fa-user"></i> <span>ملفي الشخصي</span></a></li>
            <li><a href="friends.html"><i class="fas fa-users"></i> <span>الأصدقاء</span></a></li>
            <li><a href="messages.html"><i class="fas fa-envelope"></i> <span>الرسائل</span></a></li>
            <li><a href="#" id="admin-link" style="display:none;"><i class="fas fa-crown"></i> <span>لوحة الأدمن</span></a></li>
            <li><a href="#" onclick="logout()"><i class="fas fa-sign-out-alt"></i> <span>خروج</span></a></li>
        </ul>
    </aside>
    <main class="main-content">
        <header class="header">
            <input type="text" class="header-search" placeholder="🔍 بحث...">
            <div class="header-user">
                <span id="header-name" style="color:white;"></span>
                <img id="header-avatar" class="header-avatar" src="" alt="avatar" onclick="window.location.href='profile.html'">
            </div>
        </header>
        <div class="card">
            <textarea id="post-text" class="input" placeholder="ماذا يدور في بالك؟" rows="2"></textarea>
            <input type="file" id="post-image" class="input" accept="image/*" style="padding:8px;margin-top:10px;">
            <button onclick="createPost()" class="btn btn-primary" style="margin-top:10px;"><i class="fas fa-paper-plane ml-2"></i> نشر</button>
        </div>
        <div id="posts-container"></div>
    </main>
    <div id="toast" class="toast"></div>
    <script src="firebase.js"></script>
    <script src="app.js"></script>
</body>
</html>'''
    
    # ========== 6. APP.JS ==========
    app_js = '''// app.js - VK Clone Main Logic
auth.onAuthStateChanged(async (user) => {
    if (!user) { window.location.href = 'login.html'; return; }
    currentUser = user;
    const snapshot = await db.ref('users/' + user.uid).once('value');
    const userData = snapshot.val();
    if (userData) {
        document.getElementById('header-name').textContent = userData.name;
        document.getElementById('header-avatar').src = userData.photo || 'https://via.placeholder.com/40';
        if (userData.role === 'admin') {
            const link = document.getElementById('admin-link');
            link.style.display = 'block';
            link.href = 'admin.html';
        }
    }
    loadPosts();
});

async function loadPosts() {
    const snapshot = await db.ref('posts').orderByChild('created_at').limitToLast(50).once('value');
    const posts = snapshot.val();
    const container = document.getElementById('posts-container');
    container.innerHTML = '';
    if (!posts) { container.innerHTML = '<div class="card" style="text-align:center;color:#64748b;">لا توجد منشورات بعد</div>'; return; }
    const postsArray = Object.entries(posts).reverse();
    for (const [postId, post] of postsArray) {
        const userSnapshot = await db.ref('users/' + post.user_id).once('value');
        const userData = userSnapshot.val() || {};
        const div = document.createElement('div');
        div.className = 'card';
        div.innerHTML = `
            <div class="card-header">
                <img src="${userData.photo || 'https://via.placeholder.com/45'}" class="card-avatar">
                <div><div class="card-name">${userData.name || 'مستخدم'}</div><div class="card-time">${new Date(post.created_at).toLocaleString('ar-IQ')}</div></div>
            </div>
            <div class="post-text">${post.text}</div>
            ${post.image ? `<img src="${post.image}" class="post-image">` : ''}
            <div class="post-actions">
                <button onclick="likePost('${postId}')"><i class="far fa-heart"></i> إعجاب (${post.likes ? Object.keys(post.likes).length : 0})</button>
                <button onclick="showComments('${postId}')"><i class="far fa-comment"></i> تعليق</button>
            </div>
            <div id="comments-${postId}" style="margin-top:10px;"></div>`;
        container.appendChild(div);
    }
}

async function createPost() {
    const text = document.getElementById('post-text').value;
    const imageFile = document.getElementById('post-image').files[0];
    if (!text && !imageFile) { showToast('الرجاء كتابة نص أو اختيار صورة'); return; }
    let imageURL = '';
    if (imageFile) {
        const fd = new FormData(); fd.append('file', imageFile); fd.append('upload_preset', cloudinaryConfig.uploadPreset);
        const res = await fetch(`https://api.cloudinary.com/v1_1/${cloudinaryConfig.cloudName}/image/upload`, { method: 'POST', body: fd });
        imageURL = (await res.json()).secure_url;
    }
    await db.ref('posts').push({ user_id: currentUser.uid, text, image: imageURL, likes: {}, created_at: new Date().toISOString() });
    document.getElementById('post-text').value = '';
    document.getElementById('post-image').value = '';
    showToast('✅ تم النشر!');
    loadPosts();
}

async function likePost(postId) {
    const ref = db.ref(`posts/${postId}/likes/${currentUser.uid}`);
    (await ref.once('value')).val() ? await ref.remove() : await ref.set(true);
    loadPosts();
}

async function showComments(postId) {
    const div = document.getElementById('comments-' + postId);
    const snap = await db.ref(`posts/${postId}/comments`).once('value');
    const comments = snap.val();
    let html = '<div style="border-top:1px solid var(--vk-border);padding-top:10px;">';
    html += `<input id="cin-${postId}" class="input" placeholder="اكتب تعليق..." style="margin-bottom:5px;">`;
    html += `<button onclick="addComment('${postId}')" class="btn btn-glass" style="font-size:12px;">إرسال</button>`;
    if (comments) {
        for (const [cid, c] of Object.entries(comments).reverse()) {
            const us = await db.ref('users/' + c.user_id).once('value');
            const u = us.val() || {};
            html += `<div style="display:flex;gap:8px;align-items:center;margin-top:8px;padding:8px;background:var(--vk-glass);border-radius:10px;">
                <img src="${u.photo || 'https://via.placeholder.com/30'}" style="width:30px;height:30px;border-radius:50%;">
                <div><span style="font-weight:700;font-size:12px;color:white;">${u.name||''}</span><span style="font-size:11px;color:#94a3b8;display:block;">${c.text}</span></div></div>`;
        }
    }
    html += '</div>'; div.innerHTML = html;
}

async function addComment(postId) {
    const input = document.getElementById('cin-' + postId);
    if (!input.value) return;
    await db.ref(`posts/${postId}/comments`).push({ user_id: currentUser.uid, text: input.value, created_at: new Date().toISOString() });
    input.value = ''; showComments(postId);
}

function logout() { auth.signOut().then(() => window.location.href = 'login.html'); }
function showToast(msg) { const t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show'); setTimeout(() => t.classList.remove('show'), 2500); }
'''
    
    # ========== 7. PROFILE ==========
    profile_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>VK - الملف الشخصي</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"><link rel="stylesheet" href="style.css">
</head>
<body>
    <aside class="sidebar"><div class="sidebar-logo">VK</div><ul class="sidebar-nav">
        <li><a href="index.html"><i class="fas fa-home"></i><span>الرئيسية</span></a></li>
        <li><a href="profile.html" class="active"><i class="fas fa-user"></i><span>ملفي الشخصي</span></a></li>
        <li><a href="friends.html"><i class="fas fa-users"></i><span>الأصدقاء</span></a></li>
        <li><a href="messages.html"><i class="fas fa-envelope"></i><span>الرسائل</span></a></li>
        <li><a href="#" onclick="logout()"><i class="fas fa-sign-out-alt"></i><span>خروج</span></a></li>
    </ul></aside>
    <main class="main-content">
        <div class="card" style="text-align:center;">
            <img id="profile-photo" src="" style="width:150px;height:150px;border-radius:50%;object-fit:cover;border:4px solid var(--vk-blue);margin:20px auto;display:block;">
            <h1 id="profile-name" style="color:white;font-size:28px;"></h1><p id="profile-email" style="color:#94a3b8;"></p>
            <p id="profile-role" style="color:#fbbf24;font-size:14px;"></p><p id="profile-date" style="color:#64748b;font-size:12px;"></p>
            <button onclick="editProfile()" class="btn btn-primary" style="margin-top:20px;"><i class="fas fa-edit ml-2"></i>تعديل الملف الشخصي</button>
        </div>
        <h3 style="color:white;margin:20px 0;">📝 منشوراتي</h3><div id="my-posts"></div>
    </main>
    <div id="edit-modal" class="modal"><div class="modal-content">
        <h3 class="modal-title">تعديل الملف الشخصي</h3>
        <input type="text" id="edit-name" class="input" placeholder="الاسم"><input type="file" id="edit-photo" class="input" accept="image/*">
        <button onclick="saveProfile()" class="btn btn-primary" style="width:100%;">حفظ</button>
        <button onclick="closeModal()" class="btn btn-glass" style="width:100%;margin-top:10px;">إلغاء</button>
    </div></div>
    <script src="firebase.js"></script>
    <script>
        let currentUser;
        auth.onAuthStateChanged(async (user) => { if (!user) { window.location.href = 'login.html'; return; } currentUser = user; await loadProfile(); await loadMyPosts(); });
        async function loadProfile() { const s = await db.ref('users/' + currentUser.uid).once('value'); const d = s.val(); if (d) { document.getElementById('profile-photo').src = d.photo || 'https://via.placeholder.com/150'; document.getElementById('profile-name').textContent = d.name; document.getElementById('profile-email').textContent = d.email; document.getElementById('profile-role').textContent = d.role === 'admin' ? '👑 أدمن' : '👤 عضو'; document.getElementById('profile-date').textContent = 'عضو منذ: ' + new Date(d.created_at).toLocaleDateString('ar-IQ'); } }
        async function loadMyPosts() { const s = await db.ref('posts').orderByChild('user_id').equalTo(currentUser.uid).once('value'); const p = s.val(); const c = document.getElementById('my-posts'); c.innerHTML = ''; if (!p) { c.innerHTML = '<p style="color:#64748b;">لا توجد منشورات</p>'; return; } for (const [id, post] of Object.entries(p).reverse()) { c.innerHTML += `<div class="card"><div class="post-text">${post.text}</div>${post.image ? '<img src="'+post.image+'" class="post-image">' : ''}<div class="post-actions"><button onclick="deletePost(\'${id}\')"><i class="fas fa-trash"></i> حذف</button></div></div>`; } }
        async function deletePost(id) { if (confirm('حذف المنشور؟')) { await db.ref('posts/' + id).remove(); loadMyPosts(); } }
        function editProfile() { document.getElementById('edit-modal').classList.add('active'); }
        async function saveProfile() { const n = document.getElementById('edit-name').value; const f = document.getElementById('edit-photo').files[0]; const u = {}; if (n) u.name = n; if (f) { const fd = new FormData(); fd.append('file', f); fd.append('upload_preset', cloudinaryConfig.uploadPreset); const r = await fetch(`https://api.cloudinary.com/v1_1/${cloudinaryConfig.cloudName}/image/upload`, { method: 'POST', body: fd }); u.photo = (await r.json()).secure_url; } await db.ref('users/' + currentUser.uid).update(u); closeModal(); loadProfile(); }
        function closeModal() { document.getElementById('edit-modal').classList.remove('active'); }
        function logout() { auth.signOut().then(() => window.location.href = 'login.html'); }
    </script>
</body>
</html>'''
    
    # ========== 8. FRIENDS ==========
    friends_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>VK - الأصدقاء</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"><link rel="stylesheet" href="style.css">
</head>
<body>
    <aside class="sidebar"><div class="sidebar-logo">VK</div><ul class="sidebar-nav">
        <li><a href="index.html"><i class="fas fa-home"></i><span>الرئيسية</span></a></li>
        <li><a href="profile.html"><i class="fas fa-user"></i><span>ملفي الشخصي</span></a></li>
        <li><a href="friends.html" class="active"><i class="fas fa-users"></i><span>الأصدقاء</span></a></li>
        <li><a href="messages.html"><i class="fas fa-envelope"></i><span>الرسائل</span></a></li>
        <li><a href="#" onclick="logout()"><i class="fas fa-sign-out-alt"></i><span>خروج</span></a></li>
    </ul></aside>
    <main class="main-content">
        <header class="header"><input type="text" class="header-search" id="search-user" placeholder="🔍 بحث عن عضو..."></header>
        <div class="card"><h3 style="color:white;margin-bottom:20px;">👥 كل الأعضاء</h3><div id="all-users"></div></div>
        <div class="card"><h3 style="color:white;margin-bottom:20px;">💚 أصدقائي</h3><div id="my-friends"></div></div>
    </main>
    <script src="firebase.js"></script>
    <script>
        let currentUser;
        auth.onAuthStateChanged(async (user) => { if (!user) { window.location.href = 'login.html'; return; } currentUser = user; loadAllUsers(); loadMyFriends(); });
        async function loadAllUsers() { const s = await db.ref('users').once('value'); const u = s.val(); const c = document.getElementById('all-users'); c.innerHTML = ''; for (const [uid, d] of Object.entries(u)) { if (uid === currentUser.uid) continue; c.innerHTML += `<div style="display:flex;align-items:center;justify-content:space-between;padding:12px;background:var(--vk-glass);border-radius:12px;margin-bottom:8px;"><div style="display:flex;align-items:center;gap:10px;"><img src="${d.photo||'https://via.placeholder.com/40'}" style="width:40px;height:40px;border-radius:50%;"><span style="color:white;">${d.name}</span></div><button onclick="addFriend(\'${uid}\')" class="btn btn-primary" style="font-size:12px;padding:5px 15px;"><i class="fas fa-user-plus"></i>إضافة</button></div>`; } }
        async function addFriend(fid) { await db.ref('friends/' + currentUser.uid + '/' + fid).set(true); await db.ref('friends/' + fid + '/' + currentUser.uid).set(true); loadMyFriends(); }
        async function loadMyFriends() { const s = await db.ref('friends/' + currentUser.uid).once('value'); const f = s.val(); const c = document.getElementById('my-friends'); c.innerHTML = ''; if (!f) { c.innerHTML = '<p style="color:#64748b;">لا أصدقاء بعد</p>'; return; } for (const [fid, _] of Object.entries(f)) { const us = await db.ref('users/' + fid).once('value'); const u = us.val(); if (u) { c.innerHTML += `<div style="display:flex;align-items:center;justify-content:space-between;padding:12px;background:var(--vk-glass);border-radius:12px;margin-bottom:8px;"><div style="display:flex;align-items:center;gap:10px;"><img src="${u.photo||'https://via.placeholder.com/40'}" style="width:40px;height:40px;border-radius:50%;"><span style="color:white;">${u.name}</span></div><button onclick="removeFriend(\'${fid}\')" class="btn btn-glass" style="font-size:12px;"><i class="fas fa-user-times"></i>حذف</button></div>`; } } }
        async function removeFriend(fid) { await db.ref('friends/' + currentUser.uid + '/' + fid).remove(); await db.ref('friends/' + fid + '/' + currentUser.uid).remove(); loadMyFriends(); }
        function logout() { auth.signOut().then(() => window.location.href = 'login.html'); }
    </script>
</body>
</html>'''
    
    # ========== 9. MESSAGES ==========
    messages_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>VK - الرسائل</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"><link rel="stylesheet" href="style.css">
</head>
<body>
    <aside class="sidebar"><div class="sidebar-logo">VK</div><ul class="sidebar-nav">
        <li><a href="index.html"><i class="fas fa-home"></i><span>الرئيسية</span></a></li>
        <li><a href="profile.html"><i class="fas fa-user"></i><span>ملفي الشخصي</span></a></li>
        <li><a href="friends.html"><i class="fas fa-users"></i><span>الأصدقاء</span></a></li>
        <li><a href="messages.html" class="active"><i class="fas fa-envelope"></i><span>الرسائل</span></a></li>
        <li><a href="#" onclick="logout()"><i class="fas fa-sign-out-alt"></i><span>خروج</span></a></li>
    </ul></aside>
    <main class="main-content">
        <div style="display:flex;gap:20px;height:80vh;">
            <div class="card" style="width:300px;overflow-y:auto;"><h3 style="color:white;margin-bottom:15px;">💬 المحادثات</h3><div id="friends-list"></div></div>
            <div class="card" style="flex:1;display:flex;flex-direction:column;">
                <h3 style="color:white;margin-bottom:15px;" id="chat-title">اختر محادثة</h3>
                <div id="messages-area" style="flex:1;overflow-y:auto;margin-bottom:15px;"></div>
                <div style="display:flex;gap:10px;"><input type="text" id="message-input" class="input" placeholder="اكتب رسالة..." style="flex:1;"><button onclick="sendMessage()" class="btn btn-primary"><i class="fas fa-paper-plane"></i></button></div>
            </div>
        </div>
    </main>
    <script src="firebase.js"></script>
    <script>
        let currentUser, currentChat;
        auth.onAuthStateChanged(async (user) => { if (!user) { window.location.href = 'login.html'; return; } currentUser = user; loadFriends(); });
        async function loadFriends() { const s = await db.ref('friends/' + currentUser.uid).once('value'); const f = s.val(); const c = document.getElementById('friends-list'); c.innerHTML = ''; if (!f) return; for (const [fid, _] of Object.entries(f)) { const us = await db.ref('users/' + fid).once('value'); const u = us.val(); if (u) { c.innerHTML += `<div onclick="openChat(\'${fid}\',\'${u.name}\')" style="padding:12px;background:var(--vk-glass);border-radius:12px;margin-bottom:8px;cursor:pointer;display:flex;align-items:center;gap:10px;"><img src="${u.photo||'https://via.placeholder.com/40'}" style="width:40px;height:40px;border-radius:50%;"><span style="color:white;">${u.name}</span></div>`; } } }
        function openChat(fid, name) { currentChat = fid; document.getElementById('chat-title').textContent = '💬 ' + name; loadMessages(); }
        async function loadMessages() { if (!currentChat) return; const cid = [currentUser.uid, currentChat].sort().join('_'); const s = await db.ref('messages/' + cid).orderByChild('time').limitToLast(100).once('value'); const m = s.val(); const c = document.getElementById('messages-area'); c.innerHTML = ''; if (!m) return; for (const [mid, msg] of Object.entries(m)) { const me = msg.sender === currentUser.uid; c.innerHTML += `<div style="text-align:${me?'left':'right'};margin-bottom:10px;"><span style="display:inline-block;padding:10px 15px;border-radius:18px;font-size:14px;${me?'background:var(--vk-blue);color:white;':'background:var(--vk-glass);color:var(--vk-text);'}">${msg.text}</span><div style="font-size:10px;color:#64748b;">${new Date(msg.time).toLocaleTimeString('ar-IQ')}</div></div>`; } c.scrollTop = c.scrollHeight; }
        async function sendMessage() { if (!currentChat) return alert('اختر محادثة'); const t = document.getElementById('message-input').value; if (!t) return; const cid = [currentUser.uid, currentChat].sort().join('_'); await db.ref('messages/' + cid).push({ sender: currentUser.uid, text: t, time: new Date().toISOString() }); document.getElementById('message-input').value = ''; loadMessages(); }
        function logout() { auth.signOut().then(() => window.location.href = 'login.html'); }
    </script>
</body>
</html>'''
    
    # ========== 10. ADMIN ==========
    admin_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>VK - لوحة الأدمن</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database-compat.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"><link rel="stylesheet" href="style.css">
</head>
<body>
    <aside class="sidebar"><div class="sidebar-logo">VK</div><ul class="sidebar-nav">
        <li><a href="index.html"><i class="fas fa-home"></i><span>الرئيسية</span></a></li>
        <li><a href="profile.html"><i class="fas fa-user"></i><span>ملفي الشخصي</span></a></li>
        <li><a href="admin.html" class="active"><i class="fas fa-crown"></i><span>لوحة الأدمن</span></a></li>
        <li><a href="#" onclick="logout()"><i class="fas fa-sign-out-alt"></i><span>خروج</span></a></li>
    </ul></aside>
    <main class="main-content">
        <header class="header"><h2 style="color:white;">👑 لوحة تحكم الأدمن</h2></header>
        <div class="card"><h3 style="color:white;margin-bottom:20px;">👥 إدارة الأعضاء</h3><div id="users-list"></div></div>
    </main>
    <script src="firebase.js"></script>
    <script>
        auth.onAuthStateChanged(async (user) => { if (!user) { window.location.href = 'login.html'; return; } const s = await db.ref('users/' + user.uid).once('value'); const d = s.val(); if (!d || d.role !== 'admin') { alert('غير مصرح!'); window.location.href = 'index.html'; return; } loadUsers(); });
        async function loadUsers() { const s = await db.ref('users').once('value'); const u = s.val(); const c = document.getElementById('users-list'); c.innerHTML = ''; for (const [uid, d] of Object.entries(u)) { c.innerHTML += `<div style="display:flex;align-items:center;justify-content:space-between;padding:15px;background:var(--vk-glass);border-radius:12px;margin-bottom:10px;"><div style="display:flex;align-items:center;gap:10px;"><img src="${d.photo||'https://via.placeholder.com/40'}" style="width:40px;height:40px;border-radius:50%;"><div><span style="color:white;font-weight:700;">${d.name}</span><span style="font-size:11px;color:#64748b;display:block;">${d.email}</span></div></div><div><span style="color:#fbbf24;font-size:12px;">${d.role}</span><button onclick="deleteUser(\'${uid}\')" class="btn btn-glass" style="font-size:11px;padding:5px 10px;margin-right:10px;"><i class="fas fa-trash"></i>حذف</button></div></div>`; } }
        async function deleteUser(uid) { if (confirm('حذف العضو؟')) { await db.ref('users/' + uid).remove(); loadUsers(); } }
        function logout() { auth.signOut().then(() => window.location.href = 'login.html'); }
    </script>
</body>
</html>'''

    # ========== SAVE ==========
    files = {
        "firebase.js": firebase_js,
        "style.css": css,
        "login.html": login_html,
        "register.html": register_html,
        "index.html": index_html,
        "app.js": app_js,
        "profile.html": profile_html,
        "friends.html": friends_html,
        "messages.html": messages_html,
        "admin.html": admin_html,
    }
    
    for filename, content in files.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ {filename}")
    
    print(f"\n🎉 موقع VK تم بناؤه بنجاح! ({datetime.now().strftime('%Y-%m-%d %H:%M')})")

if __name__ == "__main__":
    generate_vk_site()
