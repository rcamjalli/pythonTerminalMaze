from mazeGame import Game
from maze import MyPair
import curses
import time

# get the curses screen window
screen = curses.initscr()
# enable text color 
curses.start_color()
# turn off input echoing
curses.noecho()
# respond to keys immediately (don't wait for enter)
curses.cbreak()
#hides the cursor
curses.curs_set(0)
# map arrow keys to special values
screen.keypad(True)
#set colors
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED) #player
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE) #maze background
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE) #maze walls
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN) #end of the maze

def drawGame(game):
    for y in range(len(myGame.obstacles)):
        for x in range(0,len(myGame.obstacles[y]) * len(game.drawChar),len(game.drawChar)):
            currentPos = MyPair(x/len(game.drawChar),y)
            screen.addstr(y,x,game.drawChar,curses.color_pair(game.posType(currentPos)))
        
def refreshPos(game,pos):
    screen.addstr(pos.y,pos.x*2,game.drawChar,curses.color_pair(game.posType(pos)))

try:
    myGame = Game()
    drawGame(myGame)
    screen.addstr(len(myGame.obstacles),0,"Press q to end",curses.A_BOLD)
    myGame.win = False
    while not myGame.win:
        char = screen.getch()
        move = False 
        startPos = MyPair(myGame.pos.x,myGame.pos.y)
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            move = myGame.moveRight()
        elif char == curses.KEY_LEFT:
            move = myGame.moveLeft()
        elif char == curses.KEY_UP:
            move = myGame.moveUp()
        elif char == curses.KEY_DOWN:
            move = myGame.moveDown()
        if move:
            #refreshPos(myGame,startPos)
            refreshPos(myGame,myGame.pos)
            if myGame.pos.x == (myGame.size.x) - 1 and myGame.pos.y == (myGame.size.y) - 1: 
                time.sleep(0.5)  
                myGame.win = True          
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()