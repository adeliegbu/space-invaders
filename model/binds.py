class Binds:
    def __init__(self, canvas):
        self.canvas = canvas
        self.game_binds_dico = {}
        self.menu_binds_dico = {}
        self.active_binds = set()
        self.canvas.bind("<KeyPress>", self.active_bind)
        self.canvas.bind("<KeyRelease>", self.desactive_bind)
        self.canvas.focus_set()

    def active_bind(self, event):
        self.active_binds.add(self.get_binded_command(event.keysym))

    def desactive_bind(self, event):
        self.active_binds.discard(self.get_binded_command(event.keysym))
    
    def add_bind(self, command, key):
        if not key in self.game_binds_dico:
            self.game_binds_dico[key] = command
    
    def change_bind(self, command, key):
        if command in self.game_binds_dico:
            self.game_binds_dico[command] = key
    
    def reset_bind(self, command):
        if command in self.game_binds_dico:
            self.game_binds_dico[command] = None

    def remove_bind(self, command):
        if command in self.game_binds_dico:
            del self.game_binds_dico[command]
    
    def get_binded_command(self, key):
        for command, bind in self.game_binds_dico.items():
            if bind == key:
                return command
        return None

    def reset_active_binds(self):
        self.active_binds = set()
    
    def reset_binds(self):
        self.game_binds_dico = {}
        self.active_binds = set()
        