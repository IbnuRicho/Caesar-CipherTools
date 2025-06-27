from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from collections import Counter

app = Flask(__name__)

# Load model dan vectorizer
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Fungsi untuk enkripsi
def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            result += shift_char.upper() if char.isupper() else shift_char
        else:
            result += char
    return result

# Fungsi untuk dekripsi
def caesar_decrypt(ciphertext):
    results = []
    for shift in range(1, 26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                shift_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97)
                decrypted += shift_char.upper() if char.isupper() else shift_char
            else:
                decrypted += char
        results.append((decrypted, shift))
    return results

# Endpoint untuk menghitung frekuensi karakter
@app.route('/frequency', methods=['POST'])
def frequency():
    text = request.json.get('text', '').lower()
    frequency = Counter(c for c in text if c.isalpha())
    return jsonify(frequency)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'encrypt' in request.form:
            plaintext = request.form['plaintext']
            shift = int(request.form['shift'])
            ciphertext = caesar_encrypt(plaintext, shift)
            return render_template('index.html', ciphertext=ciphertext)

        elif 'decrypt' in request.form:
            ciphertext = request.form['ciphertext']
            vectorized_input = vectorizer.transform([ciphertext])
            predicted_shift = model.predict(vectorized_input)[0]
            decrypted_results = caesar_decrypt(ciphertext)
            predicted_plaintext = decrypted_results[predicted_shift - 1][0]
            return render_template(
                'index.html', 
                predicted_plaintext=predicted_plaintext, 
                predicted_shift=predicted_shift
            )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
