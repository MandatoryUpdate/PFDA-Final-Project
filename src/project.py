import random
import pygame
from pygame import mixer


class Player():
    def __init__(self, isFalling = True, keyPressed = "", isTouching =""):
        self.isFalling = isFalling
        self.keyPressed = keyPressed
        self.isTouching = isTouching


        def setFalling(self, val):
            self.isFalling = val





def main():
    pygame.init()
    pygame.display.set_caption("Final Project")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True
    fullscreen = False
    resolution2 = resolution

    while running:
        mouse_position = pygame.mouse.get_pos()
        #Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                resolution2 = (event.w, event.h)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                window_size = pygame.display.get_desktop_sizes()[0]
                resolution2 = window_size
                fullscreen = not fullscreen
                if fullscreen:
                    pygame.display.quit()
                    pygame.init()
                    screen = pygame.display.set_mode(resolution2)
                    pygame.display.toggle_fullscreen()
                else:
                    pygame.display.quit()
                    pygame.display.init()
                    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)









if __name__ == "__main__":
    main()