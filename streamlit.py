import streamlit as st

def affine_encrypt(p, a, b):
    cip = ''
    for char in p:
        if char.isalpha():
            base = 97 if char.islower() else 65
            c = chr(((a * (ord(char) - base) + b) % 26) + base)
            cip += c
        else:
            cip += char
    return cip

st.title("Affine Cipher Encryption")

plaintext = st.text_input("Masukkan plaintext:")
a = st.number_input("Masukkan kunci a (bilangan bulat, harus coprime dengan 26)", min_value=1, step=1)
b = st.number_input("Masukkan kunci b (bilangan bulat)", min_value=0, step=1)

if st.button("Enkripsi"):
    # Validasi apakah a coprime dengan 26
    from math import gcd
    if gcd(int(a), 26) != 1:
        st.error("Kunci a harus coprime dengan 26!")
    else:
        ciphertext = affine_encrypt(plaintext, int(a), int(b))
        st.success(f"Ciphertext: {ciphertext}")
