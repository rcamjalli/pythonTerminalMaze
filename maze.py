class MyPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return False
    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return not self.__eq__(other)

from random import shuffle

def validNeighbour(pos, mazeSize):
    return pos.x >= 0 and pos.x < mazeSize.x and pos.y >= 0 and pos.y < mazeSize.y

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
    return maze

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
                    walk(neighbour)
    walk(MyPair(0,0))
    return maze

def maze(size):
    return createMaze(MyPair(size.x/2,size.y/2))