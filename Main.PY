# Willowcreek Assylum
#By: Alexandra Michelle Duran, Taylor Antley, Owen Sutka


import pygame, Grid, Five2, racecarr, TicTacToe7
# This main class is used to define whihc games are used. It can be thought of
#  as either the link or hub for the games
class RealMain(object):
    def __init__(self):
        pass
    # play game 1
    def game1(self):
        g1 = Five2.x3Light()
        g1.play()
    # play game 2
    def game2(self):
        g2 = racecarr.Racecar()
        g2.game_loop()
    # play game 3
    def game3(self):
        g3 = TicTacToe7.BinaryGame()
        g3.play()
    # quit game 1 and go to grid
    def game1Quit(self):
        gm1 = Grid.GridMain()
        gm1.game1Return()
    # quit game 2 and go to grid
    def game2Quit(self):
        gm2 = Grid.GridMain()
        gm2.game2Return()
    # quit game 3 and go to grid which has the end screen function
    def FINISH(self):
        gm3 = Grid.GridMain()
        gm3.game3Return()

# what is run to start the game
def start():
    m1 = Grid.GridMain()
    m1.gridStart()
    m1.main()



# can only be run once from the main to initialize the game
if __name__ == '__main__':

    pygame.init()
    start()



