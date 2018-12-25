from maze import MyPair
from random import shuffle
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

curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) #maze background
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE) #maze walls

drawChar = "  "

def posColor(pos, maze):
    if maze[pos.y][pos.x]:
        return 2
    else:
        return 1

def drawMaze(maze):
    for y in range(len(maze)):
        for x in range(0,len(maze[y]) * len(drawChar),len(drawChar)):
            currentPos = MyPair(x/len(drawChar),y)
            screen.addstr(y,x,drawChar,curses.color_pair(posColor(currentPos,maze)))
    screen.refresh()
    time.sleep(0.03)

def drawBaseMaze(size):
    maze = []
    for y in range(size.y*2+1):
        array = []
        for x in range(size.x*2+1):
            if y > 0 and y < (size.x*2) and y % 2 == 1:
                if x % 2 == 0:
                    array.append(True)
                else:
                    array.append(False)
            else:
                array.append(True)
        maze.append(array)
        drawMaze(maze) 
    return maze

def validNeighbour(pos, mazeSize):
    return pos.x >= 0 and pos.x < mazeSize.x and pos.y >= 0 and pos.y < mazeSize.y

def createMaze(size):
    maze = drawBaseMaze(size)
    visited = [[False for i in range(size.x)] for j in range(size.y)]
    def walk(pos):
        visited[pos.y][pos.x] = True
        if pos.x != size.x - 1 or pos.y != size.y - 1:  
            neighbours = [MyPair(pos.x+1,pos.y),MyPair(pos.x-1,pos.y),MyPair(pos.x,pos.y+1),MyPair(pos.x,pos.y-1)] 
            shuffle(neighbours)
            for neighbour in neighbours:
                if validNeighbour(neighbour,size) and not visited[neighbour.y][neighbour.x]:
                    if neighbour.x > pos.x:
                        maze[pos.y*2+1][pos.x*2+2] = False
                    elif neighbour.x < pos.x:
                        maze[pos.y*2+1][pos.x*2] = False
                    elif neighbour.y > pos.y:
                        maze[pos.y*2+2][pos.x*2+1] = False
                    elif neighbour.y < pos.y:
                        maze[pos.y*2][pos.x*2+1] = False
                    drawMaze(maze)
                    walk(neighbour)
    walk(MyPair(0,0))
    return maze
def maze(size):
    return createMaze(MyPair(size.x/2,size.y/2))
try:
    size = MyPair(60,45)
    maze(size)
    screen.addstr(size.y+1,0,"Press r to restart",curses.A_BOLD)
    screen.addstr(size.y+2,0,"Press q to end",curses.A_BOLD)
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == ord('r'):
            maze(size)
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()