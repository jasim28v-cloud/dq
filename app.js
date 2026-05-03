// app.js - VK Clone Main Logic
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
