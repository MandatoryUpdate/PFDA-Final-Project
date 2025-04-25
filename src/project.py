import random
import pygame
from pygame import mixer


class Player():
    def __init__(self, pos = (0,0), isFalling = True, keyPressed = "", isTouching = False):
        self.isFalling = isFalling
        self.keyPressed = keyPressed
        self.isTouching = isTouching
        self.gravityVal = 0
        self.pos = pos
        self.surface = pygame.Surface(size=(10, 10))
        pygame.draw.rect(surface = self.surface, color=(255, 255, 255), rect=(0,0, 10, 10))

    def setFalling(self, val):
        self.isFalling = val
    
    def setTouching (self, val):
        self.isTouching = val
    
    def adjustYPosition(self):
        x, y = self.pos
        y += self.gravityVal
        self.pos = (x, y)
    
    def adjustHorizontalPosition(self, keyPressed):
        x, y = self.pos
        if keyPressed == "left":
            x -= 1
            self.pos = (x, y)
        if keyPressed == "right":
            x += 1
            self.pos = (x, y)
            
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

    def update(self, surface, keyPressed):
        if self.isFalling:
            if self.gravityVal < 2:
                self.gravityVal += .005
        self.adjustYPosition()
        self.adjustHorizontalPosition(keyPressed)
        self.draw(surface)
        

        





def main():
    pygame.init()
    pygame.display.set_caption("Final Project")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True
    player = Player((400, 150), True, "", False)
    fullscreen = False
    resolution2 = resolution
    keyPressed = ""

    while running:
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                keyPressed = "left"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                keyPressed = "right"

        screen.fill((0, 0, 0))
        player.update(screen, keyPressed)
        pygame.display.flip()









if __name__ == "__main__":
    main()