from model.settings_related.settings import Settings

class Upgrade_settings(Settings):
    def __init__(self):
        super().__init__(["cooldown", "cooldown_reload", "damage", "power", "rafale", "imprecision", "munitions", "speed", "life", "auto_reload"])
        self.upgrade_prices = [2, 1, 5, 2, 5, 2, 1, 1, 7, 3]

    def choiced_price(self):
        return self.upgrade_prices[self.choiced_index]
