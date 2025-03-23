import pygame


def draw_level1(screen):
    background = pygame.image.load('assets/images/background.png').convert()
    screen.blit(background,(0,0))