from multiprocessing import Queue
import generateMaze as gm
from mpi4py import MPI

class Node():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.paths = {} #example {'path1': {'source': (start), 'sink':(end), nodes1:(x1,y1), "dist":10}}
        self.dist = 100000000
        self.visited = 'nV'
        self.startEnd = 'n'
        self.open = 'n'
        self.parent = None
        self.source = (0,0)
    def setSource(self, start):
        if((self.x == start[0] )or (self.y==start[1])):
            self.startEnd = 'y'
        self.source = start

    def setParent(self, parent):
        self.parent = parent
    def changeOpen(self,new):
        self.open = new
    def addPath(self, path, dist):
        self.paths[path] = {'dist': dist,"source":self.source, "sink": self.sink}
    
    def addNode(self, path,node,nodeName, upDist):
        self.paths[path]['dist'] = upDist
        self.paths[path][nodeName] = (node.x,node.y)
     
        
def makeMazeNodes(mazeIn,start, end):
    mazeOut = []
    for i in range(len(mazeIn)):
        row = []
        for j in range(len(mazeIn[0])):
        
            newNode = Node(i,j)
            if((i,j)==start):
                newNode.startEnd='y'
            if((i,j)==end):
                newNode.startEnd='y'
            x = mazeIn[i][j] == 'True'
            if(x):
                newNode.open='n'
            else:
                newNode.open='y'
            row.append(newNode)
        mazeOut.append(row)
    return mazeOut

def printMaze(mazeIn):
     for i in range(len(mazeIn)):
        x = ""
        for j in range(len(mazeIn[0])):
            x += "  :   " +mazeIn[i][j].open 
        print(x)
def bfsSearch(mazeInitial, startNode):
    print("in breaht first hsearch")
    q = Queue()
    q.put(startNode)
    startNode.visited = 'v'
    startNode.dist = 0
    while ( q.empty()):
        v = q.get()
        print(v.x, v.y)
        if(v.y+1 < len(mazeInitial[0])):
            top = mazeInitial[v.x][v.y+1] 
        else:
            top =Node(0,0)
        if(v.y -1 >0):
            bottom = mazeInitial[v.x][v.y-1]
        else:

            bottom =Node(0,0)
        if(v.x+1 < len(mazeInitial)):
            right= mazeInitial[v.x+1][v.y]
        else:
            right = Node(0,0)
        if(v.x-1 > 0):
            left = mazeInitial[v.x-1][v.y] 
        else:
            left = Node(0,0)
        for neighbour in [top,bottom,left,right]:
            if neighbour.visited!= 'v' or neighbour.open =='y':
                neighbour.visited = 'v'
                neighbour.parent = v
                q.put(neighbour)

maze = gm.maze1

start = gm.intial[0]
end = gm.intial[1]
outMaze = makeMazeNodes(maze, start,end)
printMaze(outMaze)
startNode = outMaze[start[1]][start[0]]
bfsSearch(outMaze, startNode)




"""
comm = MPI.COMM_WORLD
rank =comm.Get_rank()
size = comm.Get_size()
print("hello world process", rank, size)
"""
