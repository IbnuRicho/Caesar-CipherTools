# 🔐 Cipher Tool with Machine Learning (Flask Web App)

Proyek ini merupakan aplikasi web berbasis **Flask** yang menyediakan fitur **enkripsi dan dekripsi** teks menggunakan **Caesar Cipher** dan **Random Substitution**, serta menampilkan **frekuensi huruf** dalam teks. Sistem ini dilengkapi dengan model **Machine Learning Naive Bayes** untuk **memprediksi nilai shift Caesar Cipher** secara otomatis saat proses dekripsi.

---

## 🚀 Fitur Utama

- ✅ Enkripsi teks dengan Caesar Cipher atau Random Substitution
- ✅ Dekripsi otomatis menggunakan model Naive Bayes untuk prediksi shift
- ✅ Visualisasi diagram frekuensi huruf (dibandingkan dengan frekuensi bahasa Inggris standar)
- ✅ GUI berbasis web menggunakan Flask
- ✅ Visual interaktif menggunakan Chart.js

---

## 🛠 Teknologi yang Digunakan

- Python
- Flask
- HTML/CSS (Jinja2 Template)
- Chart.js
- Scikit-learn (Naive Bayes Classifier)
- Pickle (untuk menyimpan model)
- NumPy & String Library

---

## 🧠 Tentang Model Machine Learning
Model machine learning yang digunakan adalah Naive Bayes Classifier, yang dilatih untuk mengenali pola distribusi huruf dalam ciphertext guna memprediksi nilai shift dari Caesar Cipher. Proses pelatihan menggunakan pendekatan supervised learning, dan fitur teks diekstraksi menggunakan TF-IDF Vectorizer.



## 📊 Visualisasi Frekuensi Huruf
Aplikasi ini menampilkan diagram batang frekuensi huruf menggunakan Chart.js, yang membandingkan frekuensi huruf pada input dengan frekuensi standar bahasa Inggris. Fitur ini membantu pengguna memahami distribusi huruf dan mendukung proses dekripsi secara visual.
