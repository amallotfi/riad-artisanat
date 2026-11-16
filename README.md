# 🕌 Riad Artisanat — Plateforme E-commerce

Application web interactive développée avec **Python** et **Streamlit**, dédiée à la mise en valeur et à la vente de produits de l'artisanat marocain.

> *Note : Ce projet est un prototype démonstratif réalisé à des fins d'apprentissage et de portfolio (les produits, prix et commandes affichés sont fictifs).*

## ✨ Fonctionnalités principales
- **Catalogue dynamique :** Chargement et structuration des produits depuis une base de données Excel via `Pandas`.
- **Filtres multicritères :** Recherche instantanée par ville (Fès, Marrakech, Essaouira, Ouarzazate) et par catégorie (Poterie, Tapis, Cuir, Bois, Cuivre).
- **Interface uniformisée :** Grille de produits harmonisée et redimensionnement automatique des images avec `Pillow (PIL)`.
- **Panier interactif (`Mon Couffin`) :** Ajout d'articles, calcul automatique du montant total via `st.session_state` et formulaire de validation de commande.

## 🛠️ Technologies utilisées
- **Python 3**
- **Streamlit** (Interface utilisateur & gestion d'état)
- **Pandas & OpenPyXL** (Manipulation des données Excel)
- **Pillow (PIL)** (Traitement et redimensionnement des images)

## 🚀 Lancer le projet en local
1. Cloner le dépôt :
   `git clone https://github.com/amallotfi/riad-artisanat.git`
2. Installer les dépendances :
   `pip install -r requirements.txt`
3. Démarrer l'application :
   `streamlit run app.py`
