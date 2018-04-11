#from multiprocessing import Queue
#from collections import deque
import generateMaze as gm
from mpi4py import MPI
import queue
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
        
            newNode = Node(j,i)
            if((j,i)==start):
                newNode.startEnd='y'
            if((j,i)==end):
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
def bfsSearch(mazeInitial, startNode,endValue):
    print("in breaht first hsearch")
    q = queue.LifoQueue()
    startNode.visited = 'v'
    startNode.dist = 0
    q.put_nowait(startNode)
    while (not q.empty()):
        v = q.get_nowait()

        if(endValue[0] == v.x  and endValue[1] ==v.y):
            print(v.x, v.y, v.parent)
            break
        if(v.parent != None):

            print(v.x, v.y, (v.parent.x, v.parent.y))
        else: 
            print(v.x, v.y, v.parent)
        if(v.x+1 < len(mazeInitial[0])):
            node = mazeInitial[v.y][v.x+1]
            print(node.visited)
            if node.visited!= 'v' and node.open =='y':
                node.visited = 'v'
                node.parent = v
                q.put_nowait(node)

            mazeInitial[v.y][v.x+1] =node
        if(v.x-1 > 0):
            node = mazeInitial[v.y][v.x-1] 
            if node.visited!= 'v' and node.open =='y':
                node.visited = 'v'
                node.parent = v
                q.put_nowait(node)

            mazeInitial[v.y][v.x-1] =node


        if(v.y+1 < len(mazeInitial)):
            node = mazeInitial[v.y+1][v.x] 
            if (node.visited != 'v' and node.open =='y'):
                node.visited = 'v'
                node.parent = v
                q.put_nowait(node)

            mazeInitial[v.y+1][v.x] =node

        if(v.y-1 > 0):
            node = mazeInitial[v.y-1][v.x] 
            if node.visited!= 'v' and node.open =='y':
                node.visited = 'v'
                node.parent = v
                q.put_nowait(node)

            mazeInitial[v.y-1][v.x] =node

maze = gm.maze1

start = gm.intial[0]
end = gm.intial[1]
outMaze = makeMazeNodes(maze, start,end)
printMaze(outMaze)
startNode = outMaze[start[1]][start[0]]
print((start[0],start[1]), (end[0],end[1]))
bfsSearch(outMaze, startNode,end)



"""
comm = MPI.COMM_WORLD
rank =comm.Get_rank()
size = comm.Get_size()
print("hello world process", rank, size)
"""
