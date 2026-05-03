// firebase.js - إعدادات Firebase + Cloudinary
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
