import streamlit as st
import random
import string

st.title("Şifre Oluşturucu")

if st.button("Şifre Üret"):
    karakterler = string.ascii_letters + string.digits
    sifre = "".join(random.sample(karakterler, 10))
    st.code(sifre)
