from model.settings_related.settings import Settings

class Options_settings(Settings):
    def __init__(self):
        super().__init__([["solo", "coop"],["easy", "ranked", "defi"],["assault", "rafale", "mitraille", "tank", "sniper"],["green", "red", "blue", "yellow", "pink","grey"],["left", "right", "reload", "shoot"]])
        self.categorises = ["mode", "level", "class", "skin", "binds"]
        self.choiced_sub_index_list = [0] * self.length
    
    def get_choiced_sub_option(self, index):
        return self.options[index][self.choiced_sub_index_list[index]]

    def get_choiced_sub_index(self, index):
        return self.choiced_sub_index_list[index]
    
    def get_choiced_options(self):
        for i in range(self.length):
            yield self.options[i][self.choiced_sub_index_list[i]]

    def next_sub_option(self):
        if self.choiced_sub_index_list[self.choiced_index] < len(self.options[self.choiced_index]) - 1:
            self.choiced_sub_index_list[self.choiced_index] += 1

    def prev_sub_option(self):
        if self.choiced_sub_index_list[self.choiced_index] > 0:
            self.choiced_sub_index_list[self.choiced_index] -= 1
    
    def reset_sub_options(self):
        self.choiced_sub_index_list = [0] * self.length