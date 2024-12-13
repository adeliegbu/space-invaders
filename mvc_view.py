# -*- coding: utf-8 -*-
"""
Filename: mvc_view.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module contains the view component of the MVC architecture for the application.
             It handles the display of various elements on the canvas, including upgrade stages, 
             choosing cards, menus, and options.
TODO:
- Add missing skins for players
- Add error handling for file operations
- Optimize the display functions for better performance
- Add more detailed comments and docstrings
"""

import tkinter as tk
from PIL import Image, ImageTk
import json

from visuel.rules import rules_text
from mvc_model import Weapons

class View:
    def __init__(self, controller):
        """
        Initialize the View class.
        
        Parameters:
        controller (Controller): The controller instance that this view interacts with.
        """
        self.controller = controller

        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x0, self.y0 = self.screen_width // 2, self.screen_height // 2

        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, highlightthickness=0, cursor="none")
        self.canvas.pack(fill="both", expand=True)

        self.bg_game_image = ImageTk.PhotoImage(Image.open("visuel/background_invader.jpg").resize((self.screen_width, self.screen_height), Image.LANCZOS))
        self.bg_menu_image = ImageTk.PhotoImage(Image.open("visuel/bg_menu.jpg").resize((self.screen_width, self.screen_height), Image.LANCZOS))

        self.bg_game_id = self.canvas.create_image(0, 0, image=self.bg_game_image, anchor="nw")
        self.bg_menu_id = self.canvas.create_image(0, 0, image=self.bg_menu_image, anchor="nw")

        self.logo_image = ImageTk.PhotoImage(Image.open("visuel/space_logo.png").resize((self.screen_width // 3, self.screen_height // 6), Image.LANCZOS))

        # Load images for aliens, players, and projectiles
        self.alien_skins = {}
        self.player_skins = {}
        self.projectile_skins = {}

        self.alien_skins["basic"] = ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien__basic.png").resize((self.screen_height // 13, self.screen_height // 13), Image.LANCZOS))
        self.alien_skins["doctor"] = ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien__doctor.png").resize((self.screen_height // 19, self.screen_height // 22), Image.LANCZOS))
        self.alien_skins["bonus"] = ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien__bonus.png").resize((self.screen_height // 11, self.screen_height // 18), Image.LANCZOS))
        self.alien_skins["projectile"] = ImageTk.PhotoImage(Image.open("visuel/fire_ball.png").resize((30, 50), Image.LANCZOS))

        for type in ["assault", "rafale", "mitraillette", "sniper", "tank"]:
            self.alien_skins[type] = [ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien_{type}_{level}.png").resize((self.screen_height // 20, self.screen_height // 22), Image.LANCZOS)) for level in range (1, 6)]
            self.player_skins[type] = [ImageTk.PhotoImage(Image.open(f"visuel/player_skins/player_{type}_{color}.png").resize((self.screen_height // 15, self.screen_height // 15), Image.LANCZOS)) for color in ["green", "blue", "red", "yellow", "pink"]]
        
        for color in ["green", "blue", "red", "yellow", "pink"]:
            self.projectile_skins[color] = ImageTk.PhotoImage(Image.open(f"visuel/projectile_skins/projectile_{color}.png").rotate(90).resize((250, 250), Image.LANCZOS))
        
        self.weapons_stats = {}
        for weapon in ["assault", "rafale", "mitraillette", "sniper", "tank"]:
            temporary = Weapons(None, (weapon, "player"), None, None)
            self.weapons_stats[weapon] = temporary.stats

        self.heart_full_image = ImageTk.PhotoImage(Image.open("visuel/full_life.png").resize((30, 30), Image.LANCZOS))
        self.heart_semi_image = ImageTk.PhotoImage(Image.open("visuel/semi_life.png").resize((30, 30), Image.LANCZOS))
        self.heart_dead_image = ImageTk.PhotoImage(Image.open("visuel/no_life.png").resize((30, 30), Image.LANCZOS))

        self.button_active_image = ImageTk.PhotoImage(Image.open("visuel/button_active.png").resize((int(self.screen_width // 4.5), self.screen_height // 13), Image.LANCZOS))
        self.button_inactive_image = ImageTk.PhotoImage(Image.open("visuel/button_inactive.png").resize((int(self.screen_width // 4.5), self.screen_height // 13), Image.LANCZOS))
        self.options_solo_bubble_image = ImageTk.PhotoImage(Image.open("visuel/options_bubble.png").resize((self.screen_width // 5 * 2, self.screen_height // 2), Image.LANCZOS))
        self.options_coop_bubble_image = ImageTk.PhotoImage(Image.open("visuel/options_bubble.png").resize((self.screen_width // 5, self.screen_height // 2), Image.LANCZOS))

        self.lil_button_active_image = ImageTk.PhotoImage(Image.open("visuel/button_active.png").resize((self.screen_width // 6, self.screen_height // 25), Image.LANCZOS))
        self.lil_button_inactive_image = ImageTk.PhotoImage(Image.open("visuel/button_inactive.png").resize((self.screen_width // 6, self.screen_height // 25), Image.LANCZOS))

        self.arrow_left_image = ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-arrow_left.png").resize((self.screen_height // 40, self.screen_height // 40), Image.LANCZOS))
        self.arrow_right_image = ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-arrow_right.png").resize((self.screen_height // 40, self.screen_height // 40), Image.LANCZOS))

        self.wall_image = ImageTk.PhotoImage(Image.open("visuel/n_wall.webp").resize((20, 20), Image.LANCZOS))

        # Load font images
        self.font_images = {}
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+"
        for char in characters:
            self.font_images[char] = [ImageTk.PhotoImage(Image.open(f"visuel/font/police_space_invaders-{char}.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]
        self.font_images[":"] = [ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-doublepoint.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]
        self.font_images["<"] = [ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-arrow_left.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]
        self.font_images[">"] = [ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-arrow_right.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]
        self.font_images["."] = [ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-_.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]
        self.font_images["_"] = [ImageTk.PhotoImage(Image.open("visuel/font/police_space_invaders-_.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]

        self.upgrade_images = {}
        upgrades = ["cooldown", "cooldown_reload", "damage", "power", "rafale", "imprecision", "munitions", "speed", "life", "auto_reload"]
        upgrade_prices = [2, 1, 4, 2, 5, 2, 3, 1, 7, 3]
        upgrade_texts = ["-30 cooldown", "-50 cd recharge", "+1 degats", "+2 puissance", "+1 rafale", "+3 precision", "+3 munitions", "+1 vitesse", "+1 vie", "recharge auto"]
        i = 0
        for upgrade in upgrades:
            self.upgrade_images[upgrade] = [ImageTk.PhotoImage(Image.open(f"visuel/upgrade_cards/up_{upgrade}.png").resize((125, 200), Image.LANCZOS)), upgrade_prices[i], upgrade_texts[i]]
            i += 1

        self.lives_munitions_images_list = [None] * 6
        self.image_score = []
        self.image_stage = []
        self.image_upgrade_points = []
        self.image_upgrade_cards = []
        self.cards_choosing_index = 0
        self.upgrade_text = []
        self.binds_overlay = []
        self.menu_overlay = []
        self.menu_choosing_index = 0
        self.options_choosing_index = [0, 0]

    def new_game(self):
        """
        Start a new game by resetting the overlay and updating the display.
        """
        self.overlay_reset()
        self.canvas.delete(self.logo_id)
        self.binds_overlay = self.display_font_text("menu:Echap", alignment="right", size=1, pad_x=2, pad_y=10, x=self.screen_width - 20, y= 20)

        self.controller.new_game()
        self.update(should_update_lives=True, should_update_score=True, should_update_stage=True, should_update_skill_points=False)

    def rules(self):
        """
        Display the game rules on the canvas.
        """
        self.display_font_text(rules_text, alignment="left", size=0, pad_x=0, pad_y=10, x=0, y=self.y0 // 2)

    def menu(self):
        """
        Display the main menu on the canvas.
        """
        self.hide_image_list(self.lives_munitions_images_list)
        self.bg_menu_id = self.canvas.create_image(0, 0, image=self.bg_menu_image, anchor="nw")
        self.logo_id = self.canvas.create_image(self.x0, self.y0 // 2, image=self.logo_image, anchor="center")
        self.hide_image_list(self.binds_overlay)
        self.display_menu()

    def display_menu(self):
        """
        Display the main menu on the canvas.
        This includes the menu options and highlights the currently selected option.
        """
        self.menu_overlay = []
        self.menu_overlay.append([self.canvas.create_image(self.x0, self.screen_height // 8 * (4 + i), image=self.button_inactive_image, anchor="center") for i in range(4)])
        self.menu_overlay.append(self.display_font_text("New game\nRegles\nOptions\nQuitter", alignment="center", size=5, pad_x=2, pad_y=self.screen_height // 8 - self.screen_height // 25, x=self.x0, y=self.y0))
        self.canvas.itemconfig(self.menu_overlay[0][self.menu_choosing_index], image=self.button_active_image)

    def quit(self):
        """
        Quit the application.
        """
        self.root.quit()

    def show_options(self):
        """
        Display the options menu on the canvas.
        """
        self.hide_image_list(self.menu_overlay)
        self.canvas.delete(self.logo_id)
        self.display_options()

    def hide_image_list(self, image_list):
        """
        Hide a list of images on the canvas.
        
        Parameters:
        image_list (list): The list of image IDs to hide.
        """
        if isinstance(image_list, list):
            for i in range (len(image_list)):
                if isinstance(image_list[i], list):
                    self.hide_image_list(image_list[i])
                elif image_list[i] is not None:
                    self.canvas.delete(image_list[i])
    
    def overlay_reset(self):
        """
        Reset the overlay by deleting all items except the background.
        """
        for item in self.canvas.find_all():
            if item != self.bg_game_id:
                self.canvas.delete(item)

    def display_lives(self, lives, weapon, x, y, difficulty):
        """
        Display the player's lives on the canvas.
        
        Parameters:
        lives (int): The number of lives to display.
        x (int): The x-coordinate for the lives display.
        y (int): The y-coordinate for the lives display.
        difficulty (int): The difficulty level affecting the display.
        """
        self.hide_image_list(self.lives_munitions_images_list)
        j = 0
        for i in range(- difficulty // 2 + 1, difficulty // 2 + 1):
            j += 1
            if j <= lives:
                self.lives_munitions_images_list[j-1] = self.canvas.create_image(x + i * 20, y + 45, image=self.heart_full_image, anchor="center")
            elif j - 0.5 == lives:
                self.lives_munitions_images_list[j-1] = self.canvas.create_image(x + i * 20, y + 45, image=self.heart_semi_image, anchor="center")
            else:
                self.lives_munitions_images_list[j-1] = self.canvas.create_image(x + i * 20, y + 45, image=self.heart_dead_image, anchor="center")
        if not weapon.reloading:
            self.lives_munitions_images_list[-1] = self.canvas.create_rectangle(x + self.screen_height // 20, y + self.screen_height // 50, x + self.screen_height // 18, y + self.screen_height // 25 * (0.5 - weapon.get_munitions_left()), fill=self.controller.options_settings.get_choiced_sub_option(3))
        else:
            self.lives_munitions_images_list[-1] = self.canvas.create_rectangle(x + self.screen_height // 20, y + self.screen_height // 50, x + self.screen_height // 18, y + self.screen_height // 25 * (0.5 - weapon.cooldown_reload.get_progression()), fill=self.controller.options_settings.get_choiced_sub_option(3))
    
    def update(self, should_update_lives, should_update_score, should_update_stage, should_update_skill_points):
        """
        Update the display elements on the canvas.
        
        Parameters:
        should_update_lives (bool): Whether to update the lives display.
        should_update_score (bool): Whether to update the score display.
        should_update_stage (bool): Whether to update the stage display.
        should_update_skill_points (bool): Whether to update the skill points display.
        """
        if should_update_lives:
            for player in self.controller.players.objects_list:
                self.display_lives(player.life, player.weapon, player.x, player.y, difficulty=5 - 2 * self.controller.options_settings.get_choiced_sub_index(1))
        if should_update_score:
            if self.image_score:
                self.hide_image_list(self.image_score)
            self.image_score = self.display_font_text(f"Score:{self.controller.score}", alignment="left", size=2, pad_x=2, pad_y=0, x= 20, y=20)
        if should_update_stage:
            if self.image_stage:
                self.hide_image_list(self.image_stage)
            self.image_stage = self.display_font_text(f"Stage:{self.controller.stage_number}", alignment="center",size=2, pad_x=2, pad_y=0, x=self.x0, y=20)
        if should_update_skill_points:
            if self.image_upgrade_points:
                self.hide_image_list(self.image_upgrade_points)
            self.image_upgrade_points = self.display_font_text(f"sp:{self.controller.skill_points}", alignment="left", size=2, pad_x=2, pad_y=0, x=20, y=60)

    def display_font_text(self, text, alignment, size, pad_x, pad_y, x, y):
        """
        Display text on the canvas with specified font settings.
        
        Parameters:
        text (str): The text to display.
        alignment (str): The alignment of the text.
        size (int): The size of the text.
        pad_x (int): The padding on the x-axis.
        pad_y (int): The padding on the y-axis.
        x (int): The x-coordinate for the text.
        y (int): The y-coordinate for the text.
        
        Returns:
        list: A list of text IDs created on the canvas.
        """
        text_ids = [[]]
        i = 0
        for c in text:
            if c == " ":
                text_ids[i].append(None)
            elif c == "\n":
                text_ids.append([])
                i += 1   
            elif c in self.font_images or c.upper() in self.font_images:
                c = c.upper()
                text_ids[i].append(self.font_images[c][size])
            else:
                raise ValueError(f"Caractère {c} non reconnu")

        for i in range(len(text_ids)):
            line_width = (self.screen_height // (50 - 5 * size) + pad_x) * (len(text_ids[i]) - 1)
            if alignment == "center":
                offset_x = x - line_width // 2
            elif alignment == "right":
                offset_x = x - line_width
            else:  # default to left alignment
                offset_x = x
            for j in range(len(text_ids[i])):
                if text_ids[i][j] is not None:
                    text_ids[i][j] = self.canvas.create_image(offset_x + ((self.screen_height // (50 - 5 * size) + pad_x) * j), y + ((self.screen_height // (50 - 5 * size) + pad_y) * i), image=text_ids[i][j], anchor="center")

        return text_ids

    def display_upgrade_stage(self):
        """
        Display the upgrade stage on the canvas.
        This includes the upgrade cards and their prices.
        """
        i = 0
        for upgrade in self.upgrade_images.values():
            self.image_upgrade_cards.append(self.canvas.create_image(self.screen_width // 6 * (i % 5 + 1), self.screen_height // 9 * ((i // 5 * 3) + 4) + 50, image=upgrade[0], anchor="center"))
            self.image_upgrade_cards.append(self.display_font_text(f"prix:{upgrade[1]}sp\n{upgrade[2]}", alignment="center", size=0, pad_x=2, pad_y=10, x=self.screen_width // 6 * (i % 5 + 1), y=self.screen_height * (((i // 5 * 3) + 4) / 9) - 80))
            i += 1
        self.canvas.move(self.image_upgrade_cards[0], 0, 30)
        self.upgrade_text = self.display_font_text("Choisissez une amelioration\nLeft - Right\nEntree pour valider\nEchap pour passer au next stage", alignment="center", size=3, pad_x=2, pad_y=10, x=self.x0, y=self.y0 // 4)

    def display_choosing_card(self):
        """
        Display the currently chosen card by moving the selection indicator.
        """
        if self.cards_choosing_index != self.controller.upgrade_settings.get_choiced_index():
            self.canvas.move(self.image_upgrade_cards[self.cards_choosing_index * 2], 0, -30)
            self.cards_choosing_index = self.controller.upgrade_settings.get_choiced_index()
            self.canvas.move(self.image_upgrade_cards[self.cards_choosing_index * 2], 0, 30)

    def dynamic_menu(self):
        """
        Update the menu dynamically based on user input.
        This changes the highlighted menu option.
        """
        if self.menu_choosing_index != self.controller.menu_settings.get_choiced_index():
            self.canvas.itemconfig(self.menu_overlay[0][self.menu_choosing_index], image=self.button_inactive_image)
            self.menu_choosing_index = self.controller.menu_settings.get_choiced_index()
            self.canvas.itemconfig(self.menu_overlay[0][self.menu_choosing_index], image=self.button_active_image)

    def display_options(self):
        """
        Display the options menu on the canvas.
        This reads the key bindings from a JSON file and displays them.
        """
        with open("binds.json", "r") as file:
            data_binds = json.load(file)

        self.menu_overlay = [[] for _ in range(4)]

        self.menu_overlay[0].append(self.canvas.create_image(self.screen_width // 3 * 2, self.screen_height // 3 * 2, image=self.options_solo_bubble_image, anchor="center"))
        self.menu_overlay[0].append(self.display_font_text("to modify:enter then key", alignment="center", size=1, pad_x=1, pad_y=0, x=self.screen_width // 3 * 2, y=self.screen_height // 9 * 8))

        for i in range(5):
            if i < 2:
                self.menu_overlay[1].append(self.canvas.create_image(self.screen_width // 3, self.screen_height // 8 * (i + 2), image=self.button_inactive_image, anchor="center"))
            else:
                self.menu_overlay[1].append(self.canvas.create_image(self.screen_width // 4, self.screen_height // 8 * (i + 2), image=self.button_inactive_image, anchor="center"))

        for i in range(5):
            if i < 2:
                self.menu_overlay[2].append(self.canvas.create_image(self.screen_width // 3 * 2, self.screen_height // 8 * (i + 2), image=self.button_inactive_image, anchor="center"))
                self.menu_overlay[2].append(self.display_font_text(f"< {self.controller.options_settings.categorises[i]} >", alignment="center", size=5, pad_x=2, pad_y=0, x=self.screen_width // 3, y=self.screen_height // 8 * (i + 2)))
            else:
                self.menu_overlay[2].append(self.display_font_text(f"< {self.controller.options_settings.categorises[i]} >", alignment="center", size=5, pad_x=2, pad_y=0, x=self.screen_width // 4, y=self.screen_height // 8 * (i + 2)))

        self.menu_overlay[2].append([self.canvas.create_image(self.screen_width // 40 * (23 + i // 2 * 7), self.screen_height // 21 * (17 + i % 2), image=self.lil_button_inactive_image, anchor="center") for i in range(4)])
        self.menu_overlay[2].append([self.display_font_text(f"{self.controller.options_settings.options[4][i]}:{data_binds[0][self.controller.options_settings.options[4][i]]}", alignment="center", size=1, pad_x=1, pad_y=0, x=self.screen_width // 40 * (23 + i // 2 * 7), y=self.screen_height // 21 * (17 + i % 2)) for i in range(4)])

        for i in range(2):
            if i == 0:
                self.menu_overlay[-1].append(self.display_font_text("soon", alignment="center", size=5, pad_x=2, pad_y=0, x=self.screen_width // (3 + i // 2) * 2, y=self.screen_height // 8 * (i + 2)))
            else:
                self.menu_overlay[-1].append(self.display_font_text(self.controller.options_settings.get_choiced_sub_option(i), alignment="center", size=5, pad_x=2, pad_y=0, x=self.screen_width // (3 + i // 2) * 2, y=self.screen_height // 8 * (i + 2)))

        self.menu_overlay[-1].append([self.display_font_text(self.controller.options_settings.get_choiced_sub_option(2), alignment="center", size=2, pad_x=1, pad_y=0, x=self.screen_width // 15 * 11, y=self.screen_height // 15 * 7), self.display_font_text(self.weapons_stats[self.controller.options_settings.get_choiced_sub_option(2)], alignment="left", size=2, pad_x=1, pad_y=5, x=self.screen_width // 30 * 19, y=self.screen_height // 15 * 8), self.canvas.create_image(self.screen_width // 7 * 4, self.screen_height // 3 * 2, image=self.player_skins[self.controller.options_settings.get_choiced_sub_option(2)][self.controller.options_settings.get_choiced_sub_index(3)], anchor="center")])

        self.canvas.itemconfig(self.menu_overlay[1][0], image=self.button_active_image)

    def dynamic_options(self):
        """
        Update the options menu dynamically based on user input.
        This changes the highlighted option and updates the displayed key bindings.
        """
        index = self.controller.options_settings.get_choiced_index()
        sub_index = self.controller.options_settings.get_choiced_sub_index(index)

        if self.controller.options_settings.should_update_binds_view:
            self.hide_image_list(self.menu_overlay[2][-1])
            with open("binds.json", "r") as file:
                data_binds = json.load(file)
            self.menu_overlay[2][-1] = [self.display_font_text(f"{self.controller.options_settings.options[4][i]}:{data_binds[0][self.controller.options_settings.options[4][i]]}", alignment="center", size=1, pad_x=1, pad_y=0, x=self.screen_width // 40 * (23 + i // 2 * 7), y=self.screen_height // 21 * (17 + i % 2)) for i in range(4)]
            self.controller.options_settings.should_update_binds_view = False

        if self.options_choosing_index[0] != index:
            if index == 4:
                self.canvas.itemconfig(self.menu_overlay[2][-2][self.controller.options_settings.get_choiced_sub_index(4)], image=self.lil_button_active_image)
            else:
                self.canvas.itemconfig(self.menu_overlay[2][-2][self.controller.options_settings.get_choiced_sub_index(4)], image=self.lil_button_inactive_image)
            self.canvas.itemconfig(self.menu_overlay[1][self.options_choosing_index[0]], image=self.button_inactive_image)
            self.options_choosing_index[0] = index
            self.canvas.itemconfig(self.menu_overlay[1][self.options_choosing_index[0]], image=self.button_active_image)

        elif self.options_choosing_index[1] != sub_index:
            if index < 2:
                self.hide_image_list(self.menu_overlay[-1][index])
                self.menu_overlay[-1][index] = self.display_font_text(self.controller.options_settings.get_choiced_sub_option(index), alignment="center", size=5, pad_x=1, pad_y=30, x=self.screen_width // 3 * 2, y=self.screen_height // 8 * (index + 2))
            elif index == 2 or index == 3:
                self.hide_image_list(self.menu_overlay[-1][2])
                self.menu_overlay[-1][2] = [self.display_font_text(self.controller.options_settings.get_choiced_sub_option(2), alignment="center", size=2, pad_x=1, pad_y=0, x=self.screen_width // 15 * 11, y=self.screen_height // 15 * 7), self.display_font_text(self.weapons_stats[self.controller.options_settings.get_choiced_sub_option(2)], alignment="left", size=2, pad_x=1, pad_y=5, x=self.screen_width // 30 * 19, y=self.screen_height // 15 * 8), self.canvas.create_image(self.screen_width // 7 * 4, self.screen_height // 3 * 2, image=self.player_skins[self.controller.options_settings.get_choiced_sub_option(2)][self.controller.options_settings.get_choiced_sub_index(3)], anchor="center")]
            elif index == 4:
                if self.options_choosing_index[1] < 4:
                    self.canvas.itemconfig(self.menu_overlay[2][-2][self.options_choosing_index[1]], image=self.lil_button_inactive_image)
                    self.canvas.itemconfig(self.menu_overlay[2][-2][sub_index], image=self.lil_button_active_image)
            else:
                self.menu_overlay[-1][index] = self.display_font_text(self.controller.options_settings.get_choiced_sub_option(index), alignment="center", size=5, pad_x=2, pad_y=0, x=self.screen_width // 2, y=self.screen_height // 8 * (index + 2))

            self.options_choosing_index[1] = sub_index