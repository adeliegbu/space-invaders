from model.settings_related.settings import Settings

class Options_settings(Settings):
    def __init__(self):
        super().__init__([["Solo", "coop", "duel"],["easy", "competitive", "nightmare"],["assault", "rafale", "machine_gun", "tank", "sniper"],["skin1, skin2, skin3, skin4, skin5","skin6"],])
        self.choiced_sub_index = 0
        self.choiced_sub_index_list = [0] * self.length

    def get_choiced_sub_index(self):
        return self.choiced_sub_index
    
    def get_choiced_sub_option(self):
        return self.options[self.choiced_index][self.choiced_sub_index]
    
    def get_choiced_options(self):
        for i in range(self.length):
            yield self.options[i][self.choiced_sub_index_list[i]]
    
    def set_choiced_sub_index(self):
        self.choiced_sub_index[self.choiced_index] = self.choiced_sub_index

    def next_sub_option(self):
        if self.choiced_sub_index < len(self.options[self.choiced_index]) - 1:
            self.choiced_sub_index += 1

    def prev_sub_option(self):
        if self.choiced_sub_index > 0:
            self.choiced_sub_index -= 1
    
    def reset_sub_option(self):
        self.choiced_sub_index = 0
    
    def reset_sub_options(self):
        for i in range(self.length):
            self.choiced_sub_index_list[i] = 0