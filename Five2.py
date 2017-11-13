import pygame, Main
global game1, screen
# Define some colors
BLACK = (0, 0, 0)
YELLOW = (138, 7, 7)
GREY = (105, 105, 105)
WHITE = (255, 255, 255)
RED = (64, 35, 39)
GREEN = (25,39,13)
#Sets the width and height of the grid squares, and the margin. 
WIDTH = 64
HEIGHT = 64
MARGIN = 8
game1 = False
WINDOW_SIZE = [515, 515]
screen = pygame.display.set_mode(WINDOW_SIZE)
class x3Light(object):
    def __init__(self):
        WINDOW_SIZE = [515, 515]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Willowcreek Sanitorium Door 1")
        screen.fill(BLACK)
        #Creates an empty grid and then populates it. 
        self.grid = []
        for row in range(8):
            self.grid.append([])
            for column in range(8):
                self.grid[row].append(0)
                
        pygame.display.update()
        #Colors the boarder. 
        self.grid[0][0] = 2
        self.grid[1][0] = 3
        self.grid[2][0] = 2
        self.grid[3][0] = 3
        self.grid[4][0] = 2
        self.grid[5][0] = 3
        self.grid[6][0] = 2
        
        self.grid[0][6] = 2
        self.grid[0][5] = 2
        self.grid[0][5] = 3
        self.grid[0][4] = 2
        self.grid[0][3] = 3
        self.grid[0][2] = 2
        self.grid[0][1] = 3
        
        self.grid[6][1] = 3
        self.grid[6][2] = 2
        self.grid[6][3] = 3
        self.grid[6][4] = 2
        self.grid[6][5] = 3
        
        self.grid[1][6] = 3
        self.grid[2][6] = 2
        self.grid[3][6] = 3
        self.grid[4][6] = 2
        self.grid[5][6] = 3
        self.grid[6][6] = 2
           
        self.checkValues()
    def play(self):
        global game1
        game1 = True
        while game1:
            self.checkButton()

    def quitt(self):
        global m1
        q1 = Main.RealMain()
        q1.game1Quit()
        global game1
        game1 = False

    def checkButton(self):
        for event in pygame.event.get():
            #Quits the game if the user hits X. 
            if event.type == pygame.QUIT:
                pygame.quit()
            #Reads for clicks and for mouse position. 
            elif event.type == pygame.MOUSEBUTTONDOWN:                 
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                #Does not allow the outter edges to change when clicked. 
                if self.grid[row][column] == 2:
                    self.grid[row][column] = 2
                if self.grid[row][column] == 3:
                    self.grid[row][column] = 3
                #Sets the victory conditions, turns the screen black and runs the quit function. 
                if self.grid[1][1] == 1 and self.grid[2][5] == 1 \
                   and self.grid[1][2] == 1 and self.grid[1][3] == 1 \
                   and self.grid[3][1] == 1 and self.grid[1][4] == 1 \
                   and self.grid[3][2] == 1 and self.grid[1][5] == 1 \
                   and self.grid[3][3] == 1 and self.grid[3][4] == 1 \
                   and self.grid[2][1] == 1 and self.grid[3][5] == 1 \
                   and self.grid[2][2] == 1 and self.grid[2][3] == 1 \
                   and self.grid[4][1] == 1 and self.grid[4][3] == 1 \
                   and self.grid[4][4] == 1 and self.grid[4][5] == 1 \
                   and self.grid[5][1] == 1 and self.grid[5][2] == 1 \
                   and self.grid[5][3] == 1 and self.grid[5][4] == 1 \
                   and self.grid[5][5] == 1 and self.grid[2][4] == 1 \
                   and self.grid[4][2] == 1:
                    self.grid[0][0] = 4
                    self.grid[1][0] = 4
                    self.grid[2][0] = 4
                    self.grid[3][0] = 4
                    self.grid[4][0] = 4
                    self.grid[5][0] = 4
                    self.grid[5][0] = 4
                    self.grid[6][0] = 4  
                    self.grid[0][1] = 4
                    self.grid[0][2] = 4
                    self.grid[0][3] = 4
                    self.grid[0][4] = 4
                    self.grid[0][5] = 4
                    self.grid[0][5] = 4
                    self.grid[0][6] = 4
                    self.grid[6][1] = 4
                    self.grid[6][2] = 4
                    self.grid[6][3] = 4
                    self.grid[6][4] = 4
                    self.grid[6][5] = 4
                    self.grid[6][6] = 4
                    self.grid[5][1] = 4
                    self.grid[5][2] = 4
                    self.grid[5][3] = 4
                    self.grid[5][4] = 4
                    self.grid[5][5] = 4
                    self.grid[5][6] = 4
                    self.grid[4][1] = 4
                    self.grid[4][2] = 4
                    self.grid[3][1] = 4
                    self.grid[3][2] = 4
                    self.grid[3][3] = 4
                    self.grid[3][4] = 4
                    self.grid[3][5] = 4
                    self.grid[3][6] = 4
                    self.grid[2][1] = 4
                    self.grid[2][2] = 4
                    self.grid[2][3] = 4
                    self.grid[2][4] = 4
                    self.grid[2][5] = 4
                    self.grid[2][6] = 4
                    self.grid[1][1] = 4
                    self.grid[1][2] = 4
                    self.grid[1][3] = 4
                    self.grid[1][4] = 4
                    self.grid[1][5] = 4
                    self.grid[1][6] = 4

                    self.quitt()
                #Makes the grid light or go dark in the t formation. 
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                elif self.grid[row][column] == 1:
                    self.grid[row][column] = 0
                if self.grid[row+1][column] == 1:
                    self.grid[row+1][column] = 0
                elif self.grid[row+1][column] == 0:
                    self.grid[row+1][column] = 1
                if self.grid[row][column+1] == 1:
                    self.grid[row][column+1] = 0
                elif self.grid[row][column+1] == 0:
                    self.grid[row][column+1] = 1
                if self.grid[row-1][column] == 1:
                    self.grid[row-1][column] = 0
                elif self.grid[row-1][column] == 0:
                    self.grid[row-1][column] = 1
                if self.grid[row][column-1] == 1:
                    self.grid[row][column-1] = 0
                elif self.grid[row][column-1] == 0:
                    self.grid[row][column-1] = 1

                self.checkValues()
    #Draws the grid, and colors the peices based on values assigned above and throughout the puzzle. 
    def checkValues(self):
        for row in range(7):
            for column in range(7):

                if self.grid[row][column] == 0:
                    color = GREY
                elif self.grid[row][column] == 1:
                    color = YELLOW
                elif self.grid[row][column] == 2:
                    color = GREEN
                elif self.grid[row][column] == 4:
                    color = BLACK
                else:
                    color = RED
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) \
                                                 * column + MARGIN,(MARGIN \
                                                                    + HEIGHT) \
                                                 * row + MARGIN, WIDTH, HEIGHT])
                pygame.display.update()
