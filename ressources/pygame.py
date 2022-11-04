import pygame, sys
from pygame import *

def main():
    pygame.init()
    FPS = 30
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 400))
    cat = pygame.image.load('cat.png')
    rect = cat.get_rect(x=300, y=100)  # Create rectangle the same size as 'cat.png'.

    while True:
        if rect.collidepoint(pygame.mouse.get_pos()):
            print("The mouse cursor is hovering over the cat")

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(cat, rect)  # Use your rect to position the cat.
        pygame.display.flip()
        fpsClock.tick(FPS)
main()