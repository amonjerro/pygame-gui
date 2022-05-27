import pygame

class Button:
    def __init__(self, text, font_size, f, rect=None):
        self.rect = rect
        self.text = text
        self.font_size = font_size
        self.f = f
    def execute_action(self):
        self.f()
    def render(self, surface):
        font = pygame.font.SysFont('Arial', self.font_size)
        if self.rect:
            pygame.draw.rect(surface,(130,130,130), self.rect)
            text_surface = font.render(self.text, False, (255,255,255))
            surface.blit(text_surface, (self.rect.x, self.rect.y))
    def check_mouse_collision(self, mouse_pos):
        if self.rect:
            return self.rect.collidepoint(mouse_pos)
        else:
            return False