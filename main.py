import pygame
import sys

# Constantes
WIDTH, HEIGHT = 600, 400
SPRITE_WIDTH, SPRITE_HEIGHT = 50, 50  # Ajusta según el tamaño real del sprite

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
        
        # Limites
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

# Carga de imágenes
player_image = pygame.image.load('player.png').convert_alpha()
entity_image = pygame.image.load('player.png').convert_alpha()
background = pygame.image.load('background.png').convert()

# Crear objetos
player_obj = GameObject(player_image, 10, 5)
entities = []
for x in range(10):
    entity = GameObject(entity_image, x*40, 2)
    entities.append(entity)

# Game Loop
while True:
    # Dibujar fondo
    screen.blit(background, (0, 0))

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_obj.move(up=True)
    if keys[pygame.K_DOWN]:
        player_obj.move(down=True)
    if keys[pygame.K_LEFT]:
        player_obj.move(left=True)
    if keys[pygame.K_RIGHT]:
        player_obj.move(right=True)
    
    # Dibujar jugador
    screen.blit(player_obj.image, player_obj.pos)

    # Mover y dibujar entidades (si quieres que se muevan)
    for e in entities:
        # Por ejemplo, hacer que se muevan hacia abajo siempre
        e.move(down=True)
        screen.blit(e.image, e.pos)

    # Actualizar pantalla
    pygame.display.update()
    clock.tick(60)
