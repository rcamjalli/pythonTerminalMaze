import maze
from maze import MyPair

class Game:
    pos = MyPair(1,1)
    size = MyPair(30,30)
    obstacles = maze.maze(size)
    win = False
    drawChar = "  "
    def moveLeft(self):
        nextPos = MyPair(self.pos.x-1,self.pos.y)
        if self.posType(nextPos) == 3 or self.posType(nextPos) == 4:
            self.pos.x -= 1
            return True
        else:
            return False
    def moveRight(self):
        nextPos = MyPair(self.pos.x+1,self.pos.y)
        if self.posType(nextPos) == 3 or self.posType(nextPos) == 4:
            self.pos.x += 1 
            return True
        else:
            return False

    def moveUp(self):
        nextPos = MyPair(self.pos.x,self.pos.y-1)
        if self.posType(nextPos) == 3 or self.posType(nextPos) == 4:
            self.pos.y -= 1
            return True
        else:
            return False
    def moveDown(self):
        nextPos = MyPair(self.pos.x,self.pos.y+1)
        if self.posType(nextPos) == 3 or self.posType(nextPos) == 4:
            self.pos.y += 1
            return True
        else:
            return False
    def posType(self, pos):
        if self.pos == pos:
            return 1
        elif self.obstacles[pos.y][pos.x]:
            return 2
        elif pos.x == (self.size.x)- 1 and pos.y == (self.size.y) - 1:
            return 4
        else: 
            return 3