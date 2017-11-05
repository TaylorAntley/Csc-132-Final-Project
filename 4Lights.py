

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
YELLOW = (138, 7, 7)
GREY = (105, 105, 105)
WHITE = (255, 255, 255)
RED = (64, 35, 39)
GREEN = (25,39,13)
WIDTH = 79
HEIGHT = 79
MARGIN = 6 

grid = []


for row in range(7):
    grid.append([])
    for column in range(7):
        grid[row].append(0)  
 

pygame.init()
WINDOW_SIZE = [515, 515]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Lights")

 
clock = pygame.time.Clock()



# -------- Main Program Loop -----------


game = False
    
while not game:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            game = True
        elif event.type == pygame.MOUSEBUTTONDOWN:                 
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if grid[1][1] == 1 and grid[4][4] == 1 and grid[4][3] == 1 and grid[4][2] == 1 and grid[4][1] == 1 and grid[1][2] == 1 and grid[1][3] == 1 and grid[1][4] == 1 and grid[2][1] == 1 and grid[2][2] == 1 and grid[2][3] == 1:
                pygame.quit()
            if grid[row][column] == 0:
                grid[row][column] = 1
            else:grid[row][column] = 0
            if grid[row+1][column] == 1:
                grid[row+1][column] = 0
            else:grid[row+1][column] = 1
            if grid[row][column+1] == 1:
                grid[row][column+1] = 0
            else:grid[row][column+1] = 1
            if grid[row-1][column] == 1:
                grid[row-1][column] = 0
            else:grid[row-1][column] = 1
            if grid[row][column-1] == 1:
                grid[row][column-1] = 0
            else: grid[row][column-1] = 1         
                
    screen.fill(BLACK)
    for row in range(6):
        for column in range(6):
            color = WHITE
            grid[0][0] = 2
            grid[1][0] = 3
            grid[2][0] = 2
            grid[3][0] = 3
            grid[4][0] = 2
            grid[5][0] = 3
            grid[5][5] = 2
            grid[0][5] = 3
            grid[0][4] = 2
            grid[0][3] = 3
            grid[0][2] = 2
            grid[0][1] = 3
            grid[5][1] = 2
            grid[5][2] = 3
            grid[5][3] = 2
            grid[5][4] = 3
            grid[5][5] = 2
            grid[1][5] = 2
            grid[2][5] = 3
            grid[3][5] = 2
            grid[4][5] = 3
            

            if grid[row][column] == 0:
                color = GREY
            elif grid[row][column] == 1:
                color = YELLOW
            elif grid[row][column] == 2:
                color = GREEN
            else:
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    clock.tick(60)
    pygame.display.flip()  
pygame.quit()
