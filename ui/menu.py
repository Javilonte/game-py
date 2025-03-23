import pygame 
from ui.buttons import Button

class MainMenu:
    
    def __init__(self):
        self.background = pygame.image.load('assets/images/menu_background.png').convert()

    def create_buttons(self):
        start_button = Button(200, 150, 200, 50, "Start Game", self.start_game)
        quit_button = Button(200, 220, 200, 50, "Quit", self.quit_game)
        self.buttons.append(start_button)
        self.buttons.append(quit_button)