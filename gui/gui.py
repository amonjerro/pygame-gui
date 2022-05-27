import pygame
from gui.button import Button

class GUI:
    def __init__(self):
        self.buttons = []
    def get_mouse_button_collision(self, mouse_pos):
        return [button for button in self.buttons if button.check_mouse_collision(mouse_pos)]
    def add_button(self, button):
        self.buttons.append(button)
    def render_gui(self, screen):
        map(lambda x: x.render(screen, x.font_size), self.buttons)

def test_function():
    print('Test')

class TestGui(GUI):
    def build(self):
        r = pygame.Rect(120,120,200,200)
        self.add_button(Button('Test', 30, test_function, r))
        