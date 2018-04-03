import generateMaze as gm
#import node 
import sys
import random 
def startPoint(maze):
    randX = random.randint(1,len(maze[0])-1)
    randY = random.randint(1,len(maze)-1)
    while(maze[randY][randX] =='True'):
        randX = random.randint(1,len(maze[0])-1)
        randY = random.randint(1,len(maze)-1)
    return (randX,randY)

def endPoint(maze,startPoint):
    randX = random.randint(1,len(maze[0])-1)
    randY = random.randint(1,len(maze)-1)
    while((maze[randY][randX] =='True') and (startPoint ==(randX,randY))):
        randX = random.randint(1,len(maze[0])-1)
        randY = random.randint(1,len(maze)-1)

    return (randX,randY)
def mazeChange(maze,col, row):
    maze2= [] 
    for i in range(0, len(maze)):
        mazeX = []
        for j in  range(0, len(maze[0])):
                mazeX.append(str(maze[i][j]))
        maze2.append(mazeX)
    return maze2


def main():
    rows = int(sys.argv[1])    
    cols = int(sys.argv[2])    
    mazeCreate = gm.maze(cols,rows)
    x = mazeChange(mazeCreate, cols, rows) 
    start = startPoint( x)
    end = endPoint( x, start)
    x[start[1]][start[0]] = "S"
    x[end[1]][end[0]] = "E"
    print(x)

main()
