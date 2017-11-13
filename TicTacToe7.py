import pygame, Main
from pygame import *
# declare our global variables for the game
XO   = "X"   # track whose turn it is; X goes first
grid = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ], \
         [ "createO", "RESET", "createX" ]]

winner = None

# declare our support functions


class BinaryGame(object):
    def __init__(self):
        pass
    
    def initBoard(self, ttt):
        # initialize the board and return it as a variable
        # ---------------------------------------------------------------
        # ttt : a properly initialized pyGame display variable

        # set up the background surface
        background = pygame.Surface (ttt.get_size())
        background = background.convert()
        background.fill ((0, 0, 0))

        # draw the grid lines
        # vertical lines...
        pygame.draw.line (background, (178, 34, 34), (100, 0), (100, 300), 2)
        pygame.draw.line (background, (178, 34, 34), (200, 0), (200, 300), 2)

        # horizontal lines...
        pygame.draw.line (background, (178, 34, 34), (0, 100), (300, 100), 2)
        pygame.draw.line (background, (178, 34, 34), (0, 200), (300, 200), 2)

        # Game move choice boxes...
        pygame.draw.rect(background, (110, 0, 0), (0, 300, 100, 400))
        pygame.draw.rect(background, (0, 0, 0), (100, 300, 200, 400))
        pygame.draw.rect(background, (110, 0, 0), (200, 300, 300, 400))
        pygame.draw.circle(background, (0, 0, 0), (50, 350), 32, 3)
        pygame.draw.line(background, (0, 0, 0), (250, 325), (250, 375), 4)

        # return the board
        return background

    def drawStatus (self, board):
        # draw the status (i.e., player turn, etc) at the bottom of the board
        # ---------------------------------------------------------------
        # board : the initialized game board surface where the status will
        #         be drawn

        # gain access to global variables
        global XO, winner

    def showBoard (self, ttt, board):
        # redraw the game board on the display
        # ---------------------------------------------------------------
        # ttt   : the initialized pyGame display
        # board : the game board surface

        self.drawStatus(board)
        ttt.blit (board, (0, 0))
        pygame.display.flip()
        
    def boardPos (self, mouseX, mouseY):
        # given a set of coordinates from the mouse, determine which board space
        # (row, column) the user clicked in.
        # ---------------------------------------------------------------
        # mouseX : the X coordinate the user clicked
        # mouseY : the Y coordinate the user clicked

        # determine the row the user clicked
        if (mouseY < 100):
            row = 0
        elif (mouseY < 200):
            row = 1
        elif (mouseY < 300):
            row = 2
        else:
            row = 3

        # determine the column the user clicked
        if (mouseX < 100):
            col = 0
        elif (mouseX < 200):
            col = 1
        else:
            col = 2

        # return the tuple containg the row & column
        return (row, col)

    def drawMove (self, board, boardRow, boardCol, Piece):
        # draw an X or O (Piece) on the board in boardRow, boardCol
        # ---------------------------------------------------------------
        # board     : the game board surface
        # boardRow,
        # boardCol  : the Row & Col in which to draw the piece (0 based)
        # Piece     : 1 or O
        
        # determine the center of the square
        centerX = ((boardCol) * 100) + 50
        centerY = ((boardRow) * 100) + 50

        # draw the appropriate piece
        if (Piece == 'O'):
            pygame.draw.circle (board, (210, 105, 30), (centerX, centerY), 32, 2)
        else:
            pygame.draw.line (board, (210, 105, 30), (centerX, centerY - 25), \
                             (centerX, centerY + 25), 2)

            
             

        # mark the space as used
        grid[boardRow][boardCol] = Piece
        
    def clickBoard(self, board):
        # determine where the user clicked and if the space is not already
        # occupied, draw the appropriate piece there (1 or O)
        # ---------------------------------------------------------------
        # board : the game board surface
        
        global grid, XO, ttt, boardMain
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        (row, col) = self.boardPos (mouseX, mouseY)

        if (grid[row][col] == "createO"):
            XO = "O"
            return
        if (grid[row][col] == "createX"):
            XO = "X"
            return
        if (grid[row][col] == "RESET"):
            grid = [ [ None, None, None ], \
                     [ None, None, None ], \
                     [ None, None, None ], \
                     [ "createO", "RESET", "createX" ]]
            boardMain = self.initBoard(ttt)
            return

        # make sure no one's used this space
        if ((grid[row][col] == "X") or (grid[row][col] == "O")):
            # this space is in use
            return

        # draw an X or O
        self.drawMove(board, row, col, XO)


    def gameWon(self, board):
        # determine if anyone has won the game
        # ---------------------------------------------------------------
        # board : the game board surface
        global grid, winner
        if grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "X" and\
           grid[1][0] == "O" and grid[1][1] == "X" and grid[1][2] == "X" and\
           grid[2][0] == "O" and grid[2][1] == "X" and grid[2][2] == "O":
            F1 = Main.RealMain()
            F1.FINISH()


    def play(self):
        # --------------------------------------------------------------------
        # initialize pygame and our window
        pygame.init()
        global ttt, boardMain
        ttt = pygame.display.set_mode ((300, 400))
        pygame.display.set_caption ('Tic-Tac-Toe')

        # create the game board
        boardMain = self.initBoard(ttt)

        # main event loop
        running = 1

        XO = "X"
        while (running == 1):
            for event in pygame.event.get():
                if event.type is QUIT:
                    running = 0
                    pygame.quit()
                    break
                elif event.type is MOUSEBUTTONDOWN:
                    # the user clicked; place an X or O
                    self.clickBoard(boardMain)

                # check for a winner
                self.gameWon(boardMain)

                # update the display
                self.showBoard(ttt, boardMain)
