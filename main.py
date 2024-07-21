import pygame
import sys
import os

# me when the initialize
pygame.init()
pygame.mixer.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

# test