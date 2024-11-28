class Binds:
    def __init__(self, canvas):
        self.canvas = canvas
        self.game_binds_dico = {}
        self.menu_binds_dico = {}
        self.active_binds = set()
        self.view.canvas.bind("<KeyPress>", self.active_bind)
        self.view.canvas.bind("<KeyRelease>", self.desactive_bind)
        self.view.canvas.focus_set()

    def active_bind(self, event):
        self.active_binds.add(self.get_binded_command(event.keysym))

    def desactive_bind(self, event):
        self.active_binds.discard(self.get_binded_command(event.keysym))
    
    def add_bind(self, command, key):
        if not key in self.binds_dico:
            self.binds_dico[key] = command
    
    def change_bind(self, command, key):
        if command in self.binds_dico:
            self.binds_dico[command] = key
    
    def reset_bind(self, command):
        if command in self.binds_dico:
            self.binds_dico[command] = None

    def remove_bind(self, command):
        if command in self.binds_dico:
            del self.binds_dico[command]
    
    def get_binded_command(self, key):
        for command, bind in self.binds_dico.items():
            if bind == key:
                return command
        return None
    
    def preset_binds(self):
        p1 = self.players.define_player(1)
        p2 = self.players.define_player(2)
        self.game_binds_dico = {
            self.p1.move(-1, 0): "Left",
            self.p1.move(1, 0): "Right",
            self.p1.shoot(): "space",
        }

    def reset_active_binds(self):
        self.active_binds = set()
    
    def reset_binds(self):
        self.binds_dico = {}
        self.active_binds = set()
        