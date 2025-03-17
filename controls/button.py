import pygame

class Button:
    def __init__(self, text, font, color, position, func=None):
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.rendered_text.get_rect(topleft=self.position)
        self.func = func

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.rendered_text, self.rect.topleft)

    def is_over(self, point):
        return self.rect.collidepoint(point)
    
    def mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.is_over(mouse_pos)
    
    def click(self, *args):
        if self.func:
            self.func(*args)