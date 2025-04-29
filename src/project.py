import random
import pygame
from pygame import mixer

class jumpingObject():
    def __init__(self, screenSize = (0,0), pos = (0,0), width = 800, height = 5):
        self.screenSize = screenSize
        self.pos = pos
        self.width = width
        self.height = height
        self.surface = pygame.Surface(size=(width, height))
        self.hitBox = pygame.Rect((0, 0), (width, height))
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)
        pygame.draw.rect(surface=self.surface, color=(255, 0, 0), rect=self.hitBox)
    
    def returnHitBox(self):
        return self.hitBox
    
    def update(self, surface):
        self.draw(surface)

class Player():
    def __init__(self, pos = (0,0), isFalling = True, keyPressed = ""):
        self.isFalling = isFalling
        self.keyPressed = keyPressed
        self.gravityVal = 0
        self.pos = pos
        self.surface = pygame.Surface(size=(10, 10))
        self.hitBox = pygame.Rect((0, 0), (10, 10))
        pygame.draw.rect(surface = self.surface, color=(255, 0, 0), rect=self.hitBox)

    def setFalling(self, val):
        self.isFalling = val

    def getPos(self):
        return self.pos
    
    def checkTouching (self, val):
        self.isTouching = val
        if self.isTouching:
            self.setFalling(False)
        else:
            self.setFalling(True)
    
    def returnHitBox(self):
        return self.hitBox
    
    def returnPosition(self):
        return self.pos
    
    def adjustYPosition(self):
        x, y = self.pos
        y += self.gravityVal
        self.pos = (x, y)
        self.hitBox = pygame.Rect((x, y), (10, 10))
    
    def adjustHorizontalPosition(self, keyPressed):
        x, y = self.pos
        if keyPressed == "left":
            x -= 1
            self.pos = (x, y)
            self.hitBox = pygame.Rect((x, y), (10, 10))
        if keyPressed == "right":
            x += 1
            self.pos = (x, y)
            self.hitBox = pygame.Rect((x, y), (10, 10))
    

    
    def draw(self, surface):
        pygame.draw.rect(surface = self.surface, color=(255, 0, 0), rect=self.hitBox)
        surface.blit(self.surface, self.pos)

    def update(self, surface, keyPressed):
        if self.isFalling:
            if self.gravityVal < 2:
                self.gravityVal += .005
        elif not self.isFalling:
            self.gravityVal = -3
            self.setFalling(True)
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
    player = Player((400, 200), True, "")
    testObject = jumpingObject(resolution, (0, 500), 800, 5)
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
            if player.returnHitBox().colliderect(testObject.returnHitBox()):
                player.setFalling(False)
        screen.fill((0, 0, 0))
        player.update(screen, keyPressed)
        testObject.update(screen)

        pygame.display.flip()









if __name__ == "__main__":
    main()