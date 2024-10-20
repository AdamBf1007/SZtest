import streamlit as st
import pandas as pd

# Charger les données depuis un fichier Excel
file_path = 'fichier_modifié.xlsx'
data = pd.read_excel(file_path)

# Vérifiez que les colonnes "Frame", "Text" et "Pourcentage" existent
if not all(col in data.columns for col in ['Frame', 'Text', 'Pourcentage']):
    st.error("Le fichier Excel doit contenir les colonnes 'Frame', 'Text' et 'Pourcentage'.")
else:
    # Titre de l'application
    st.title("Recherche de textes en CUSTOM BATTLE (SparkingZero)")

    # Champ de recherche
    search_text = st.text_input("Rechercher un texte")

    # Filtrer les options basées sur la recherche
    options = [row['Text'] for index, row in data.iterrows() if search_text.lower() in row['Text'].lower()]

    # Liste déroulante
    selected_item = st.selectbox("Sélectionnez un texte", options)

    # Afficher le texte correspondant à l'élément sélectionné
    if selected_item:
        selected_row = data[data['Text'] == selected_item]
        if not selected_row.empty:
            frame_value = selected_row['Frame'].values[0]
            percentage_value = selected_row['Pourcentage'].values[0]
             # Afficher le texte avec une taille de police plus grande
            st.markdown(f"""
            <p style='font-size:24px;'><strong style='color:green;'>Texte :</strong> {selected_item}</p>
            <p style='font-size:24px;'><strong style='color:green;'>Pourcentage (+/-) :</strong> {percentage_value}</p>
            """, unsafe_allow_html=True)
            st.markdown(f"\n\n")
            st.markdown(f"\n\n")
            st.markdown(f"\n\n")
            # Texte rouge en mode indication
            st.markdown("<span style='color:yellow; font-weight: bold;'>GUIDE D'UTILISATION :\n\n-Il ne faut utiliser aucun filtre\n\n-Il faut garder l'indication \"Tout\" en dessous du terme Légendes comme montré sur l'image ci-dessous.\n\n-Une fois que vous aurez recherché votre terme voulu, la liste contiendra toutes les occurrences de ce terme parmi les 5000+ légendes disponibles.\n\n-Le POURCENTAGE associé indique l'endroit jusqu'auquel il vous faudra scroller pour arriver à votre terme souhaité PAR RAPPORT A L'ECHELLE de la barre latérale de scroll.\n\n-En d'autres termes, si le pourcentage lié à votre texte indique 79%, cela veut dire qu'il faut scroller à peu près jusqu'aux trois quarts de la barre (en passant par en bas c'est plus facile donc).\n\nNB : Il y a encore certaines imprécisions mais ça devrait grandement vous aider à créer vos CUSTOM BATTLE sans passer 24h à chercher une phrase/un mot.</span>", unsafe_allow_html=True)
            st.markdown("<span style='color:red; font-weight: bold;'>NB : Il y a encore certaines imprécisions mais ça devrait grandement vous aider à créer vos CUSTOM BATTLE sans passer 24h à chercher une phrase/un mot.</span>", unsafe_allow_html=True)
            # Ajouter une image
            image_path = 'guide.png'  # Spécifiez le chemin de votre image
            st.image(image_path, caption="Image GUIDE", use_column_width=True)

    else:
        st.write("Aucun élément sélectionné.")
