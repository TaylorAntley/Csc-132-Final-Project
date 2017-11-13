# Initialize with imports and global to stop the game
import pygame, time, random, Main
global gameExit

# initialize all the neccessary variables, will run within main as soon as the
#  code is run
display_width = 600
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')

class Racecar(object):
    # Initialize with renaming the screen etc., pretty things
    def __init__(self):
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption('Dodge the squares')

    # Just counts up the things dodged
    def things_dodged(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, black)
        gameDisplay.blit(text,(0,0))
    # general draw function, not too special
    def things(self, thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    # car creation 
    def car(self, x,y):
        gameDisplay.blit(carImg,(x,y))
    # Simple text creation function, lots of modularization
    def text_objects(self, text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    # if you die you run this function and it creates a text whicjh says
    #  "you died", then it waits 2 seconds, then enters the loop to let you continue
    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        self.game_loop()
        
        
    # Just says you crashed, then enters another function
    def crash(self):
        self.message_display('You Died!')
    # The actual game loop, enters a while loop and doesn't leave until you dodge
    #  7 things, has some initializers here too, then you get into it and there
    #  is velocity which is changed within the loop and defines whether you win
    #  or lose the game
    def game_loop(self):
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width = 100
        thing_height = 100

        thingCount = 1

        dodged = 0

        global gameExit
        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change
            gameDisplay.fill(black)

            self.things(thing_startx, thing_starty, thing_width, thing_height, block_color)


            
            thing_starty += thing_speed
            self.car(x,y)
            self.things_dodged(dodged)

            if x > display_width - car_width or x < 0:
                self.crash()

            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0,display_width)
                dodged += 1
                if dodged >= 7:
                    global gameExit
                    gameExit = True
                    q2 = Main.RealMain()
                    q2.game2Quit()
                    #################### How we quit this game
                    
                thing_speed += 1
                thing_width += (dodged * 1.2)

            if y < thing_starty+thing_height:
                if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                    self.crash()
            
            pygame.display.update()
            clock.tick(60)

