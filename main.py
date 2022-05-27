import pygame
import sys
from pygame.locals import *

from config import config

def initialization():
    pygame.init()
    pygame.font.init()
    config_object = config.Config()
    return config_object

if __name__=='__main__':
    conf_obj = initialization()
    screen = pygame.display.set_mode(conf_obj.video['resolution'])

    while True:
        for event in pygame.event.get():
            print(pygame.mouse.get_pos())
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()