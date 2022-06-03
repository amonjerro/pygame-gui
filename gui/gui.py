import pygame
from gui.button import Button

PHI = 1.62

class GUI:
    def __init__(self):
        self.buttons = []
    def get_mouse_button_collision(self, mouse_pos):
        return [button for button in self.buttons if button.check_mouse_collision(mouse_pos)]
    def add_button(self, button):
        self.buttons.append(button)
    def render_gui(self, screen):
        for button in self.buttons:
            button.render(screen)

def test_function():
    print('Test')

class TestGui(GUI):
    def build(self):
        button_height = 100
        button_width = int(button_height*PHI)
        r = pygame.Rect(120,120,button_width, button_height)
        self.add_button(Button('Test', 30, test_function, r))
        