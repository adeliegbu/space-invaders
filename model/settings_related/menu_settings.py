from model.settings_related.settings import Settings

class Menu_settings(Settings):
    def __init__(self):
        super().__init__(options=["Nouvelle Partie", "Règles", "Options", "Quitter"])
        