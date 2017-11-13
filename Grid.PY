import pygame, sys, Main

global CX, CY, game_counter



class Level(object):
    # initializes it and defines each instance's level array as an instance variable
    def __init__(self, lvl):
        self.lvl = lvl

    # creates the level and prints it to the screen
    def createLevel(self):
        for i in range(len(self.lvl)):
            for j in range(len(self.lvl[i])):
                # define x and y for readability and then convert to real numbers
                x = j
                y = i
                x_real = BLOCK_SIZE * x
                y_real = BLOCK_SIZE * y
                # go through each part of the created lvl and print it on the screen
                if self.lvl[y][x] == 0:
                    screen.blit(grass, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                    pygame.display.update()
                elif self.lvl[y][x] == 1:
                    screen.blit(wall1, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                elif self.lvl[y][x] == 2:
                    screen.blit(door, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                elif self.lvl[y][x] == 3:
                    screen.blit(blank, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                elif self.lvl[y][x] == 5:
                    screen.blit(fakeWall, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                elif self.lvl[y][x] == 6:
                    screen.blit(fakeFloor, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                elif self.lvl[y][x] == 7:
                    screen.blit(lava, (x_real - CX, y_real - CY), area = None, special_flags = 0)
                   
    # draws it on the screen every time it is needed
    def draw(self, x_real, y_real):
        screen.blit(levelPaint, (x_real - CX, y_real - CY), area = None, special_flags = 0)
        pygame.display.update
        
    # checks if there is a collision a block over and then sends it to move
    def collisionCheck(self, key, x, y):
        if key[pygame.K_UP] and (self.lvl[(y + CY) / BLOCK_SIZE - 1][(x + CX) / BLOCK_SIZE] == 1 or self.lvl[(y + CY) / BLOCK_SIZE - 1][(x + CX) / BLOCK_SIZE] == 6):
            return 1
        elif key[pygame.K_DOWN] and (self.lvl[(y + CY) / BLOCK_SIZE + 1][(x + CX) / BLOCK_SIZE] == 1 or self.lvl[(y + CY) / BLOCK_SIZE + 1][(x + CX) / BLOCK_SIZE] == 6):
            return 1
        elif key[pygame.K_LEFT]\
             and (self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE - 1] == 1\
             or self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE - 1] == 2\
             or self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE - 1] == 6):
            return 1
        # checks to see if it is a door and play mini games
        elif key[pygame.K_RIGHT] and self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE + 1] == 2:
            global game_counter
            game_counter += 1
            game = Game(game_counter)
            game.play()
            self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE + 1] = 0
            pygame.display.update
            return 0
        # False walls, not implemented but there
        elif key[pygame.K_RIGHT] and self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE + 1] == 5:
            self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE + 1] = 0
            pygame.display.update
            return 0

        elif key[pygame.K_RIGHT] and (self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE + 1] == 1 or self.lvl[(y + CY) / BLOCK_SIZE][(x + CX) / BLOCK_SIZE + 1] == 6):
            return 1
        else:
            return 0
            


            
      

class Character(object):
    # place at arbitrary place, can pick sprite, we always choose ANKY
    def __init__(self, x = 280, y = 280, name = "Mario"):
        self.x = x
        self.y = y
        if name == "Mario":
            self.image = pygame.image.load("Mario2.png")
        if name == "ANKY":
            self.image = pygame.image.load("ANKY.png")

    # Checks to see if a key is pressed, if so then it runs the code necessary
    def keysPressed(self):
        global CX, CY
        key = pygame.key.get_pressed()
        collisionBool = L1.collisionCheck(key, self.x, self.y)
        
        if key[pygame.K_UP] and collisionBool == 0:
            CY = CY - BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            T1.draw(levelPaint)
            pygame.display.update()

        if key[pygame.K_DOWN] and collisionBool == 0:
            CY = CY + BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            T1.draw(levelPaint)
            pygame.display.update()

        if key[pygame.K_LEFT] and collisionBool == 0:
            CX = CX - BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            T1.draw(levelPaint)
            pygame.display.update()

        if key[pygame.K_RIGHT] and collisionBool == 0:
            CX = CX + BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            T1.draw(levelPaint)
            pygame.display.update()
            
        collisionBool = 0

    # Draws the character to the screen, done after the field is printed        
    def draw(self, surface):
        screen.blit(self.image, ((self.x), (self.y)), area = None, special_flags = 0)

# a copy of the character class which is used to place a textbox which tells the
#  player what to do based off the picture chosen
class TextBox(object):
    def __init__(self, x = 200, y = 470, text = "Intro"):
        if text == "Intro":
            self.image = pygame.image.load("Intro.png")
        elif text == "Lights":
            self.image = pygame.image.load("Lights.png")
        elif text == "Run":    
            self.image = pygame.image.load("Run.png")
    # If a key is pressed and the collision is False, then we can move in that
    #  direction and this function both checks those conditions and runs it
    def keysPressed(self):
        global CX, CY

        key = pygame.key.get_pressed()
        collisionBool = L1.collisionCheck(key, self.x, self.y)
        
        if key[pygame.K_UP] and collisionBool == 0:
            CY = CY - BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            pygame.display.update()

        if key[pygame.K_DOWN] and collisionBool == 0:            
            CY = CY + BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            pygame.display.update()

        if key[pygame.K_LEFT] and collisionBool == 0:
            CX = CX - BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            pygame.display.update()

        if key[pygame.K_RIGHT] and collisionBool == 0:
            CX = CX + BLOCK_SIZE
            L1.createLevel()
            C1.draw(levelPaint)
            pygame.display.update()
            
        collisionBool = 0
    # Draws the Text box to the screen
    def draw(self, surface):
        screen.blit(self.image, (30, 400), area = None, special_flags = 0)

# Game class is just to organize which game is run. I made it two functions
#  because I wanted to pull parts out to test and this just stayed through the
#  end
class Game(object):
    def __init__(self, counter):
        self.game = 0
        if counter == 1:
            self.game = "3x3"
        elif counter == 2:
            self.game = "game2"
        elif counter == 3:
            self.game = "game3"
        elif counter == 4:
            self.game = "game4"
        else:
            print "error"
    # unnecessary function, but useful for organization for running games
    #  Calls on main to run the functions
    def play(self):
        if self.game == "3x3":
            print "GAME 1 STARTED"
            global game1
            game1 = True
            ga1 = Main.RealMain()
            ga1.game1()
            print "GAME 1 ENDED"
        elif self.game == "game2":
            print "GAME 2 STARTED"
            ga2 = Main.RealMain()
            ga2.game2()
            print "GAME 2 ENDED"
        elif self.game == "game3":
            print "GAME 3 STARTED"
            ga3 = Main.RealMain()
            ga3.game3()
            print "GAME 3 ENDED"
        elif self.game == "game4":
            L1.endScreen()
    
# initializes all the images needed for the game
grass = pygame.image.load("linoleum.png")
fakeFloor = pygame.image.load("Linoleum2.png")
wall1 = pygame.image.load("LinoleumWall1.png")
fakeWall = pygame.image.load("LinoleumWall2.png")
door = pygame.image.load("door.png")
blank = pygame.image.load("blank.png")
levelPaint = pygame.image.load("field.png")
#win = pygame.image.load("win.png")
# The maps we use. We keep them smaller so we don't kill the pi
lvl1 =  [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 2, 3],\
        [3, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 3],\
        [3, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 3],\
        [3, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 3],\
        [3, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],\
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]

lvl2 =  [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 3],\
        [3, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 2, 3],\
        [3, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 3],\
        [3, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 3],\
        [3, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 3],\
        [3, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],\
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]

lvl3 =  [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 3],\
        [3, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 2, 3],\
        [3, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3],\
        [3, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 3],\
        [3, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 3],\
        [3, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 3],\
        [3, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 3],\
        [3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3],\
        [3, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 3],\
        [3, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],\
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],\
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
# initialize some variables
global BLOCK_SIZE, game_counter, screen, CX, CY
BLOCK_SIZE = 40
CX = -200
CY = -200
game_counter = 0
size = width, height = 560, 560
black = 0, 0, 0


# basically just there to communicate with the Main file and figure out how the
#  ANKY will be treated at every turn. If you beat a game it gets a command and
#  creates a new instance of the map
class GridMain(object):
    def __init__(self):
        pass

    # This is where the game starts, creates a map for the game
    def gridStart(self):
        global game_counter, L1, C1, clock, T1, screen, CX, CY
        CX = -200
        CY = -200


        game_counter = 0
                
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Creating a Game')


        screen.fill(black)

        L1 = Level(lvl1)
        L1.createLevel()
        C1 = Character(280, 280, "ANKY")
        C1.draw(levelPaint)
        T1 = TextBox(40, 400, "Intro")
        T1.draw(levelPaint)
        pygame.display.update()
        clock = pygame.time.Clock()

    # This is just to check if a key is pressed because then an event could have
    #  been triggered
    def main(self):
        x = 1
        while x == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    x = 0

            C1.keysPressed()
            clock.tick(60)
    # Called by Main to fix it
    def game1Return(self):
        global game_counter, L1, C1, clock, T1, screen, CX, CY
        CX = -200
        CY = -200


        game_counter = 1
        
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Creating a Game')


        screen.fill(black)

        L1 = Level(lvl2)
        L1.createLevel()
        C1 = Character(280, 280, "ANKY")
        C1.draw(levelPaint)
        T1 = TextBox(40, 400, "Lights")
        T1.draw(levelPaint)
        pygame.display.update()
        clock = pygame.time.Clock()
               
    # called by Main to fix it
    def game2Return(self):
        global game_counter, L1, C1, clock, T1, screen, CX, CY
        CX = -200
        CY = -200

        game_counter = 2
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Willowcreek Sanitorium')


        screen.fill(black)

        L1 = Level(lvl3)
        L1.createLevel()
        C1 = Character(320, 280, "ANKY")
        C1.draw(levelPaint)
        T1 = TextBox(40, 400, "Run")
        T1.draw(levelPaint)
        pygame.display.update()
        clock = pygame.time.Clock()


    # called by Main to fix it
    def game3Return(self):
        screen.blit(win, (0, 0), area = None, special_flags = 0)
        pygame.quit()



# just made this a class so it didn't break my game when I wanted to test it
#  on my computer without the raspberry pi. Just initializes the GPIO
class run_GPIO():
    def __init__(self):
        import Rpi.GPIO as GPIO
        switches = [ 23, 18, 12, 16 ]
        leds = [ 4, 17, 22, 6 ]


    def setGPIO(self):
        gpio = [ 4, 6, 12, 16, 17, 18, 22, 23 ]
        for i in GPIO:
            GPIO.setup(i, GPIO.OUT)
            return gpio

