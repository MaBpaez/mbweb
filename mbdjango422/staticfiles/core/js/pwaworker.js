// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
  '/offline',
  '/static/core/css/main.css'
];

// Cache on install
self.addEventListener("install", event => {
  this.skipWaiting();
  event.waitUntil(
    caches.open(staticCacheName)
      .then(cache => {
        return cache.addAll(filesToCache);
      })
  )
});

// Clear cache on activate
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(cacheName => (cacheName.startsWith("django-pwa-")))
          .filter(cacheName => (cacheName !== staticCacheName))
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});

// Serve from Cache
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
      .catch(() => {
        return caches.match('offline');
      })
  )
});

// Código para las notificaciones push (Firebase)
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC6qUSKTAHGeFupX7j3JA8ZVwP_Ym-91us",
  authDomain: "noti-mbsocialweb.firebaseapp.com",
  projectId: "noti-mbsocialweb",
  storageBucket: "noti-mbsocialweb.appspot.com",
  messagingSenderId: "571081267257",
  appId: "1:571081267257:web:f6d41af001fa6a8b0495e8"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
// Initialize Firebase Cloud Messaging and get a reference to the service
let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
  let title = payload.notification.title;
  let options = {
    body: payload.notification.body,
    icon: payload.notification.image,
    click_action: payload.data.contents
  };
  self.registration.showNotification(title, options);
});