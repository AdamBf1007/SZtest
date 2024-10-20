import gradio as gr

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

# Fonction pour obtenir le texte correspondant à l'élément sélectionné
def get_text(selected_item):
    if selected_item is None or selected_item == "Aucun résultat trouvé.":
        return "Aucun élément sélectionné."
    
    for item in data:
        if item['Texte'] == selected_item:
            return f"**Frame :** {item['Frame']} | **Texte :** {item['Texte']}"
    return "Aucun élément sélectionné."

# Fonction pour filtrer les options basées sur la recherche
def filter_options(search_text):
    search_text = search_text.strip().lower()  # Normaliser la chaîne
    filtered_data = [item['Texte'] for item in data if search_text in item['Texte'].lower()]
    return filtered_data if filtered_data else ["Aucun résultat trouvé."]

# Interface principale
with gr.Blocks() as iface:
    gr.Markdown("# Recherche de Textes")
    
    # Champ de recherche
    search_text = gr.Textbox(label="Rechercher un texte", placeholder="Entrez du texte ici...")
    
    # Liste déroulante qui se mettra à jour avec les résultats de la recherche
    dropdown = gr.Dropdown(label="Sélectionnez un texte", choices=[], interactive=True)
    
    # Afficher le résultat
    result = gr.Markdown("")

    # Mettre à jour le dropdown lorsque le texte de recherche change
    search_text.change(fn=filter_options, inputs=search_text, outputs=dropdown)

    # Afficher le texte correspondant lorsque le dropdown change
    dropdown.change(fn=get_text, inputs=dropdown, outputs=result)

# Lancer l'interface
iface.launch()
