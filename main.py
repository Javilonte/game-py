import pygame
import sys
from ui.menu import MainMenu
WIDTH, HEIGHT = 600, 400
SPRITE_WIDTH, SPRITE_HEIGHT = 50, 50 

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.x += self.speed
        if left:
            self.pos.x -= self.speed
        if down:
            self.pos.y += self.speed
        if up:
            self.pos.y -= self.speed

        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.bottom > HEIGHT:
            self.pos.top = 0
        if self.pos.left < 0:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.bottom = HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_image = pygame.image.load('assets/images/player.png').convert_alpha()
entity_image = pygame.image.load('assets/images/player.png').convert_alpha()
background = pygame.image.load('assets/images/background.png').convert()

player_obj = GameObject(player_image, 10, 5)
entities = []
for x in range(10):
    entity = GameObject(entity_image, x*40, 2)
    entities.append(entity)

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_menu = MainMenu()
    screen.blit(main_menu.background, (0,0))
#Not sure how to directly use the butons
    create_buttons = MainMenu.create_buttons()
    screen.blit(create_buttons(text_rect))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_obj.move(up=True)
    if keys[pygame.K_DOWN]:
        player_obj.move(down=True)
    if keys[pygame.K_LEFT]:
        player_obj.move(left=True)
    if keys[pygame.K_RIGHT]:
        player_obj.move(right=True)
    
    screen.blit(player_obj.image, player_obj.pos)

    for e in entities:

        e.move(down=True)
        screen.blit(e.image, e.pos)

    pygame.display.update()
    clock.tick(60)
