
class Settings:
    def __init__(self, length):
        self.length = length
        self.choiced_index = 0

    def get_choiced_index(self):
        return self.choiced_index

    def next_option(self):
        print(self.choiced_index)
        if self.choiced_index < self.length - 1:
            self.choiced_index += 1

    def prev_option(self):
        print(self.choiced_index)
        if self.choiced_index > 0:
            self.choiced_index -= 1
    
    def reset_option(self):
        self.choiced_index = 0
    