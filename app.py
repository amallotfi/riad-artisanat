import pandas as pd 
import streamlit as st
from PIL import Image, ImageOps

# Page configuration 
st.set_page_config(
    page_title="Product Data",
    page_icon="🕌",
    layout="wide"
)
# Data & State
df = pd.read_excel("products.xlsx") 
df["City"] = df["City"].astype(str).str.strip()
df["Category"] = df["Category"].astype(str).str.strip()
if  "🧺 Mon Couffin " not in st.session_state:
    st.session_state["🧺 Mon Couffin "] = []
# Sidebar 
page = st.sidebar.radio("Aller vers :", [" ✨ Nos Créations ", "🧺 Mon Couffin "])
if page == " ✨ Nos Créations ":
    st.sidebar.subheader("🔍 Filtres")
    ville = st.sidebar.selectbox("Ville :", ["Toutes", "Fes", "Marrakech", "Ouarzazate","Essaouira"])
    categorie = st.sidebar.selectbox("Catégorie :", ["Toutes", "Poterie", "Tapis", "Cuir", "Bois", "Cuivre"]) 

    
# Main page
st.title("🏺 Riad Artisanat ")
if page == " ✨ Nos Créations ":
    # 1. تطبيق الفلاتر
    df_filtered = df
    if ville != "Toutes":
        df_filtered = df_filtered[df_filtered["City"] == ville]
    if categorie != "Toutes":
        df_filtered = df_filtered[df_filtered["Category"] == categorie]

    # 2. تقسيم الشاشة لـ 3 أعمدة وعرض الصور
    cols = st.columns(3)
    for i, row in df_filtered.reset_index().iterrows():
        with cols[i % 3]:
            with st.container(height=470):
                img = ImageOps.fit(Image.open(row["Image_URL"]), (400, 400))
                st.image(img, use_container_width=True)
                st.subheader(row["Title"])
                st.caption(f"📍 {row['City']} | {row['Category']}")
                st.write(f"💰 **{row['Price']} MAD**")
            
            # زر الإضافة للقفة
            if st.button("Ajouter 🧺", key=row["ID"]):
                st.session_state["🧺 Mon Couffin "].append(row.to_dict())
                st.toast(f"{row['Title']} ajouté au couffin !")
elif page == "🧺 Mon Couffin ":
    st.header("🧺 Votre Couffin")
    
    if len(st.session_state["🧺 Mon Couffin "]) == 0:
        st.info("Votre couffin est vide pour le moment. Explorez nos créations !")
    else:
        total = 0
        for item in st.session_state["🧺 Mon Couffin "]:
            st.write(f"• **{item['Title']}** ({item['City']}) — `{item['Price']} MAD`")
            total += item["Price"]
            
        st.divider()
        st.subheader(f"💰 Total à payer : {total} MAD")
        
        if st.button("Vider le couffin 🗑️"):
            st.session_state["🧺 Mon Couffin "] = []
            st.rerun()
        st.divider()
        st.subheader("📦 Finaliser votre commande")
        with st.form("commande_form"):
            nom = st.text_input("Nom complet")
            tel = st.text_input("Numéro de téléphone")
            adresse = st.text_input("Adresse de livraison")
            
            submit = st.form_submit_button("Confirmer la commande ✅")
            
            if submit:
                if nom and tel and adresse:
                    st.success(f"Merci {nom} ! Votre commande de {total} MAD a été enregistrée. Nous vous contacterons au {tel}.")
                    st.balloons()
                    st.session_state["🧺 Mon Couffin "] = []
                else:
                    st.warning("Veuillez remplir tous les champs avant de confirmer.")    
      
