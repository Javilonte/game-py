import pygame

def create_button(x, y, width, height, text, callback, font, color, text_color):
    return {
        'rect': pygame.Rect(x, y, width, height),
        'color': color,
        'text': text,
        'callback': callback,
        'font': font,
        'text_color': text_color
    }

def draw_button(surface, button):
    pygame.draw.rect(surface, button['color'], button['rect'])
    text_surface = button['font'].render(button['text'], True, button['text_color'])
    text_rect = text_surface.get_rect(center=button['rect'].center)
    surface.blit(text_surface, text_rect)

def handle_buttons_event(event, buttons):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            if button['rect'].collidepoint(mouse_pos):
                button['callback']()
