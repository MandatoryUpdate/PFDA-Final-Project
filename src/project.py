import random
import pygame
from pygame import mixer

GAME_MENU = 0
GAME = 1
DEATH_SCREEN = 2


class jumpingObject():
    def __init__(self, screenSize = (0,0), pos = (0,0), width = 800, height = 5):
        self.screenSize = screenSize
        self.pos = pos
        self.width = width
        self.height = height
        self.surface = pygame.Surface(size=(width, height))
        self.hitBox = pygame.Rect(self.pos, (width, height))
        pygame.draw.rect(surface=self.surface, color=(255, 0, 0), rect=self.hitBox)


    def draw(self, surface):
        surface.blit(self.surface, self.pos)
    
    def giveYPosition(self):
        return self.pos[1]
    
    def returnHitBox(self):
        return self.hitBox

    def update(self, surface):
        self.draw(surface)

class groupOfObjects():
    def __init__(self, screenSize = (0,0)):
        self.screenSize = screenSize
        self.platforms = []
        self.canMake = True

    def update (self, checkRemove, surface):
        if self.canMake and not self.platforms:
            i = self.screenSize[1] - 50
            while i > 62:
                randomValue = random.randrange(0, int(self.screenSize[0]/2))
                platform = jumpingObject(self.screenSize, (randomValue, i), 100, 10)
                self.platforms.insert(0, platform)
                
                platform2 = jumpingObject(self.screenSize, (random.randrange(randomValue, self.screenSize[0]-randomValue), i - 100), 100, 10)
                self.platforms.insert(0, platform2)
                i = i - 150   
            self.canMake = False
        elif self.canMake:
            i = self.platforms[0].pos[1] - 50
            while i > 62:
                randomValue = random.randrange(0, int(self.screenSize[0]/2))
                platform = jumpingObject(self.screenSize, (randomValue, i), 100, 10)
                print(platform.pos)
                print(platform.hitBox)
                self.platforms.insert(0, platform)
                platform2 = jumpingObject(self.screenSize, (random.randrange(randomValue, self.screenSize[0]-randomValue), i - 100), 100, 10)
                self.platforms.insert(0, platform2)
                print (platform2.pos)
                print (platform2.hitBox)
                i = i - 150
            self.canMake = False
        

        self.draw(surface)

    def moveDown(self, distanceMovedDownY):
        if self.platforms:
            for platform in self.platforms:
                x, y = platform.pos
                y += 600
                platform.pos = (x, y)
                platform.hitBox = pygame.Rect((0, 0), (10, 10))
                if platform.pos[1] > self.screenSize[1]:
                    del platform

        self.canMake = True
    
    def draw(self, surface):
        for platform in self.platforms:
            platform.draw(surface)
    

class Player():
    def __init__(self, pos = (0,0), isFalling = True, keyPressed = "", screenSize = (0, 0), width = 10, height = 10):
        self.isFalling = isFalling
        self.keyPressed = keyPressed
        self.gravityVal = 1
        self.screenSize = screenSize
        self.dead = False
        self.pos = pos
        self.width = width
        self.height = height
        self.scale = 1
        self.surface = pygame.Surface(size=(width, height))
        self.hitBox = pygame.Rect((0, 0), (width, height), border_radius=5)
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
        self.hitBox = pygame.Rect((x, y), (10, 10))

    def moveDown(self):
        x, y = self.pos
        y += 600
        self.pos = (x, y)
        self.hitBox = pygame.Rect((x, y), (10, 10))



    
    def adjustHorizontalPosition(self, keyPressed):
        x2, y2 = self.screenSize
        x, y = self.pos
        
        if keyPressed == "left":
                x -= 10
        elif keyPressed == "right":
                x += 10
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
            if self.gravityVal <= 16:
                self.gravityVal += 4
        if not self.isFalling:
            self.keyPressed = "notMoving"
            self.gravityVal = -50
            self.setFalling(True)
        self.adjustYPosition()
        self.adjustHorizontalPosition(keyPressed)
        self.draw(surface)
        if self.pos[1] > self.screenSize[1]:
            del self

        





def Game(resolution, screen):
    pygame.init()
    clock = pygame.time.Clock()
    displayScore = 0
    realScore = 0
    running = True
    player = Player((200, 200), True, "", resolution, 10, 10)
    platformGroup = groupOfObjects(resolution)
    fullscreen = False
    font = pygame.font.Font('freesansbold.ttf', 32)
    fontType = pygame.freetype.SysFont(None, 50)
    resolution2 = resolution
    keyPressed = ""
    while running:
        x, y = player.getPos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    keyPressed = "left"
                elif event.key == pygame.K_d:
                    keyPressed = "right"
                else:
                    keyPressed = "none"

            if player.dead:
                running = False
                return DEATH_SCREEN
        screen.fill("white")
        if player.pos[1] <= 0:
            player.moveDown()
            platformGroup.moveDown(600)
        for platform in platformGroup.platforms:   
            if(player.hitBox.colliderect(platform.hitBox)):
                if player.gravityVal >= 0:
                    player.setFalling(False)
       
        player.update(screen, keyPressed)
        platformGroup.update(False, screen)
        
        if player.pos[1] > resolution[1]:
            player.dead = True
       
        realScore -= player.gravityVal
        if displayScore < realScore:
            displayScore = round(realScore)
        renderedFont, rect = fontType.render(str(displayScore), (255, 0, 0))
        screen.blit(renderedFont, (30, 30))
        pygame.display.flip()
        clock.tick(30)

def DEATH_SCREEN(resolution, screen):
    pygame.init()
    running = True
    surface = pygame.Surface((600, 50))
    menuBox = pygame.Rect((50, 400), (120, 50))
    gameBox = pygame.Rect((200, 400), (120, 50))
    font = pygame.font.Font('freesansbold.ttf', 12)
    fontType = pygame.freetype.SysFont(None, 12)
    renderedFont1, rect = fontType.render("Return to Menu", (255, 0, 0))
    renderedFont2, rect = fontType.render("Play Again", (255, 0, 0))
    clock = pygame.time.Clock()
    while running:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuBox.collidepoint(mouse_position):
                    print("This works")
                    running = False
                    return GAME_MENU
                if gameBox.collidepoint(mouse_position):
                    running = False
                    return GAME
                
        screen.fill("black")
        pygame.draw.rect(surface, color=(1, 255, 255), rect=gameBox)
        pygame.draw.rect(surface, color=(1, 255, 255), rect=menuBox)
        screen.blit(surface, (50, 400))
        screen.blit(renderedFont1, (65, 418))
        screen.blit(renderedFont2, (215, 418))
        pygame.display.flip()

# 2 Menus -> Game_Menu, DEATH_SCREEN
def Game_Menu(resolution, screen):
    pygame.init()
    running = True
    surface = pygame.Surface((65, 50))
    menuBox = pygame.Rect((100, 200), (65, 50))
    pygame.draw.rect(surface, color=(255, 255, 255), rect=menuBox)
    font = pygame.font.Font('freesansbold.ttf', 32)
    fontType = pygame.freetype.SysFont(None, 12)
    renderedFont1, rect = fontType.render("Play Game", (255, 0, 0))
    clock = pygame.time.Clock()
    while running:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("This works")
                running = False
                return GAME
        screen.fill("red")
        screen.blit(surface, (100, 200))
        screen.blit(renderedFont1, (100, 220))

        clock.tick(30)
        pygame.display.flip()

def main():
    resolution = (400, 800)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    scene = GAME_MENU
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if scene == GAME_MENU:
            scene = None
            scene = Game_Menu(resolution, screen)
        elif scene == GAME:
            scene = None
            scene = Game(resolution, screen)
        elif scene == DEATH_SCREEN:
            scene = None
            scene = DEATH_SCREEN(resolution, screen)
            

if __name__ == "__main__":
    main()