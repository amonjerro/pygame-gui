import pygame
import sys
from pygame.locals import *

from config import config
from gui import TestGui

def initialization():
    pygame.init()
    pygame.font.init()
    config_object = config.Config()
    return config_object

if __name__=='__main__':
    conf_obj = initialization()
    screen = pygame.display.set_mode(conf_obj.video['resolution'])
    gui = TestGui()
    gui.build()
    while True:
        gui.render_gui(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()