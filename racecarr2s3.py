import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)


perry_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge the squares')
clock = pygame.time.Clock()

perryImg = pygame.image.load('perry.png')
#racecarImg = pygame.image.load('racecar.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, (34, 139, 34), [thingx, thingy, thingw, thingh])

def perry(x,y):
    gameDisplay.blit(perryImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def Game_Over():
    message_display('Game Over.')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 6
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

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
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)


        
        thing_starty += thing_speed
        perry(x,y)
        things_dodged(dodged)

        if x > display_width - perry_width or x < 0:
            Game_Over()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + perry_width > thing_startx and x + perry_width < thing_startx+thing_width:
                print('x crossover')
                Game_Over()
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
