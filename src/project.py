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
        self.hitBox = pygame.Rect(self.pos, (width, height))
        pygame.draw.rect(surface=self.surface, color=(255, 0, 0), rect=self.hitBox)
        self.surface.fill("white")

    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)
    
    def returnHitBox(self):
        return self.hitBox

    def update(self, surface):
        self.draw(surface)

class Player():
    def __init__(self, pos = (0,0), isFalling = True, keyPressed = "", screenSize = (0, 0), width = 10, height = 10):
        self.isFalling = isFalling
        self.keyPressed = keyPressed
        self.gravityVal = 1
        self.screenSize = screenSize
        self.pos = pos
        self.width = width
        self.height = height
        self.scale = 1
        self.surface = pygame.Surface(size=(width, height))
        self.hitBox = pygame.Rect((0, 0), (width, height))
        pygame.draw.rect(surface = self.surface, color=(255, 0, 0), rect=self.hitBox)


    def setFalling(self, val):
        self.isFalling = val

    def returnHitBox(self):
        return self.hitBox

    def getPos(self):
        return self.pos
    
    def checkTouching (self, val):
        self.isTouching = val
        if self.isTouching:
            self.setFalling(False)
        else:
            self.setFalling(True)
    
    def returnPosition(self):
        return self.pos
    
    def adjustYPosition(self):
        x, y = self.pos
        y += self.gravityVal
        self.pos = (x, y)
        self.hitBox = pygame.Rect((x, y), (self.width, self.height))

    
    def adjustHorizontalPosition(self, keyPressed):
        x2, y2 = self.screenSize
        x, y = self.pos
        if not keyPressed == "notMoving":
            if keyPressed == "left":
                x -= .5
            elif keyPressed == "right":
                x += .5 
        
        if(x >= x2 - self.width):
            x = x2 - self.width
        elif(x < 0):
            x -= x-0
        self.pos = (x, y)
        self.hitBox = pygame.Rect((x, y), (10, 10))
    

    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

    def update(self, surface, keyPressed):
        if self.isFalling:
            if self.gravityVal <= 2:
                self.gravityVal += .005
        if not self.isFalling:
            self.gravityVal = -2
            self.setFalling(True)
        self.adjustYPosition()
        self.adjustHorizontalPosition(keyPressed)
        self.draw(surface)
        if self.pos[1] > self.screenSize[1]:
            pass

        





def main():
    pygame.init()
    pygame.display.set_caption("Final Project")
    clock = pygame.time.Clock()
    dt = 0
    displayScore = 0
    realScore = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    running = True
    player = Player((400, 200), True, "", resolution, 10, 10)
    testObject = jumpingObject(resolution, (0, 500), 800, 5)
    fullscreen = False
    font = pygame.font.Font('freesansbold.ttf', 32)

    resolution2 = resolution
    keyPressed = ""
    timeTillReset = 0
    while running:
        x, y = player.getPos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                resolution2 = (event.w, event.h)
                x, y = resolution
                player = Player((400, 400), True, "", resolution2)
                testObject = jumpingObject(resolution2, (0, 500), 800, 5)
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
                timeTillReset = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                keyPressed = "right"
                timeTillReset = 0
        screen.fill("black")
        timeTillReset += 1
        if not player.isFalling:
                keyPressed == "notMoving"
        player.update(screen, keyPressed)
        testObject.update(screen)
        if(player.returnHitBox().colliderect(testObject.returnHitBox())):
            player.setFalling(False)
        realScore -= player.gravityVal
        if displayScore < realScore:
            displayScore = round(realScore)
        print(displayScore)
        fontType = pygame.freetype.SysFont(None, 12)
        renderedFont, rect = fontType.render(str(displayScore), (255, 0, 0))
        screen.blit(renderedFont, (200, 200))
        pygame.display.flip()
        clock.tick(720)








if __name__ == "__main__":
    main()