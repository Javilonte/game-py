import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, FONT_SIZE, BUTTON_COLOR, BUTTON_TEXT_COLOR
from ui.menu import create_button, draw_button, handle_buttons_event
from core.game import draw_level1
from game_states import MENU, LEVEL1, GAME_OVER

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, FONT_SIZE)

current_state = MENU

def start_game():
    global current_state
    print("Starting game!")
    current_state = LEVEL1

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
        if current_state == MENU:
            handle_buttons_event(event, buttons)

    if current_state == MENU:
        for button in buttons:
            draw_button(screen, button)
    elif current_state == LEVEL1:
        draw_level1(screen)

    pygame.display.update()
    clock.tick(FPS)
