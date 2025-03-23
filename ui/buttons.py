import pygame

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect=pygame.Rect(x,y,width,height)
        self.color = (150,150,150)
        self.text = text
        self.font = pygame.font.SysFont(None, 36)
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,self.rect)
        text_surface = self.fond.render(self.text, true, (0,0,0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)