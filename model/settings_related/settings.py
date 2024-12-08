
class Settings:
    def __init__(self, options):
        self.options = options
        self.length = len(options)
        self.choiced_index = 0
        self.choosing = False

    def get_choiced_index(self):
        return self.choiced_index
    
    def get_choiced_option(self):
        return self.options[self.choiced_index]

    def next_option(self):
        print(self.choiced_index)
        if self.choiced_index < self.length - 1:
            self.choiced_index += 1

    def prev_option(self):
        if self.choiced_index > 0:
            self.choiced_index -= 1
    
    def reset_option(self):
        self.choiced_index = 0
    
    def chose_option(self):
        self.choosing = False
    
    def chose_none(self):
        self.choosing = None
    