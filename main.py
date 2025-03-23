import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, FONT_SIZE, BUTTON_COLOR, BUTTON_TEXT_COLOR
from ui.menu import create_button, draw_button, handle_buttons_event

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, FONT_SIZE)

in_main_menu = True

def start_game():
    global in_main_menu
    print("Starting game!")
    in_main_menu = False

def quit_game():
    pygame.quit()
    sys.exit()

buttons = [
    create_button(200, 150, 200, 50, "Start", start_game, FONT, BUTTON_COLOR, BUTTON_TEXT_COLOR),
    create_button(200, 220, 200, 50, "Quit", quit_game, FONT, BUTTON_COLOR, BUTTON_TEXT_COLOR)
]
#Main Loop
while True:
    screen.fill((30, 30, 30)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if in_main_menu:
            handle_buttons_event(event, buttons)

    if in_main_menu:
        for button in buttons:
            draw_button(screen, button)
    else:
    #Game Logic
        screen.fill((0, 0, 0))  

    pygame.display.update()
    clock.tick(FPS)
