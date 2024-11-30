class Binds:
    def __init__(self, canvas):
        self.canvas = canvas
        self.game_binds_dico = {}
        self.menu_binds_dico = {}
        self.active_maintainable_binds = set()
        self.active_non_maintainable_binds = set()
        self.canvas.bind("<KeyPress>", self.active_bind)
        self.canvas.bind("<KeyRelease>", self.desactive_bind)
        self.canvas.focus_set()

        # Les commandes sont des tuples (command, maintainable=booléen)
    
    def add_bind(self, command, key):
        if not command in self.game_binds_dico:
            self.game_binds_dico[command] = key
    
    def change_bind(self, command, key):
        if command in self.game_binds_dico:
            self.game_binds_dico[command] = key
    
    def reset_bind(self, command):
        if (command) in self.game_binds_dico:
            self.game_binds_dico[(command)] = None

    def remove_bind(self, command):
        if command in self.game_binds_dico:
            del self.game_binds_dico[command]
    
    def get_binded_command(self, key):
        for command, bind in self.game_binds_dico.items():
            if bind == key:
                return command
        return None

    def active_bind(self, event):
        command = self.get_binded_command(event.keysym)
        if command != None:
            if command[1]:
                self.active_maintainable_binds.add(command)
            if not command[1]:
                self.active_non_maintainable_binds.add(command)

    def desactive_bind(self, event):
        command = self.get_binded_command(event.keysym)
        if command in self.active_maintainable_binds:
            self.active_maintainable_binds.discard(command)
        if command in self.active_non_maintainable_binds:
            self.active_non_maintainable_binds.discard(command)
    
    def execute_active_binds(self):
        for command in self.active_maintainable_binds:
            command[0]()
        non_maintainable_binds = []
        for command in self.active_non_maintainable_binds:
            non_maintainable_binds.append(command)
        self.active_non_maintainable_binds = set()
        for command in non_maintainable_binds:
            command[0]()

    def reset_active_binds(self):
        self.active_binds = set()
    
    def reset_binds(self):
        self.game_binds_dico = {}
        self.active_binds = set()
        