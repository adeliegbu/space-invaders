from model.settings_related.settings import Settings

class Upgrade_settings(Settings):
    def __init__(self):
        super().__init__(length=9)
        self.upgrade_choices = ["cooldown", "cooldown_reload", "damage", "power", "rafale", "imprecision", "munitions", "speed", "life", "auto_reload"]
        self.choosing = False

    def get_choiced_upgrade(self):
        self.choosing = False
        return self.upgrade_choices[self.choiced_index]
