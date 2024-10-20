import streamlit as st

# Exemple de liste à afficher
data = [
    {"Frame": 0, "Texte": "Cell contre Buu"},
    {"Frame": 0, "Texte": "Prends ça ! Kamehameha enragé !"},
    {"Frame": 0, "Texte": "Lève-toi, Son Goku !"},
    {"Frame": 0, "Texte": "Fais vite, Jalousie !"},
    {"Frame": 0, "Texte": "La véritable puissance de Freezer"},
    {"Frame": 180, "Texte": "Buu se déchaîne"},
    {"Frame": 180, "Texte": "La puissance latente de Saiyen"},
    {"Frame": 180, "Texte": "Protège jalousie de Freezer de Planète Namek !"},
    {"Frame": 180, "Texte": "Le fils de Son Goku"},
    {"Frame": 180, "Texte": "La détermination de Namek"},
    {"Frame": 210, "Texte": "La jalousie (ilin"}
]

# Titre de l'application
st.title("Recherche de Textes")

# Champ de recherche
search_text = st.text_input("Rechercher un texte")

# Filtrer les options basées sur la recherche
options = [item['Texte'] for item in data if search_text.lower() in item['Texte'].lower()]

# Liste déroulante
selected_item = st.selectbox("Sélectionnez un texte", options)

# Afficher le texte correspondant à l'élément sélectionné
if selected_item:
    for item in data:
        if item['Texte'] == selected_item:
            st.markdown(f"**Frame :** {item['Frame']} | **Texte :** {item['Texte']}")
            break
else:
    st.write("Aucun élément sélectionné.")
