from __future__ import print_function
import generateMaze2 as gm
from mpi4py import MPI
#import queue
import sys
#import pymp
        

def printMaze(mazeIn,start,end,current):
     for i in range(len(mazeIn)):
        x = ""
        for j in range(len(mazeIn[0])):
           
            if(start[0] == j and start[1] ==i):
                x += "  :   " +" S"
            elif(end[0] == j and end[1] ==i):
                x += "  :   " +" E"
            elif(current[0] ==j and current[1] ==i):
                x += "  :   " +" C"

            elif(mazeIn[i][j] == 'True'):
                x += "  :   " +" N"

            else:
                
                x += "  :   " +" Y"
        print(x)

def printMatrix(matrix):
    for i in range(len(matrix)):
        x = ""
        for j in range(len(matrix[0])):
            x+= " :   " + str(matrix[i][j] )
        print(x)
def bfsSearch(mazeInit, startNode,endValue):

    q = []
    rows = len(mazeInit) 
    cols = len(mazeInit[0]) 
    v = Matrix = [['Nv' for x in range(cols)] for y in range(rows)] 
    dist = Matrix = [[0 for x in range(cols)] for y in range(rows)] 
    p = Matrix = [[(-1,-1) for x in range(cols)] for y in range(rows)] 
    neighbours = [(1,0) , (-1,0), (0,1), (0,-1)]
    
    q.append(startNode)
    v[startNode[1]][startNode[0]] = 'v'
    p[startNode[1]][startNode[0]] = startNode
    while (len(q)!=0):
        current = q.pop(0)
        #print(current) 
        for n in neighbours:
            boundX = current[0]+n[0]
            boundY = current[1]+n[1]
            #print(n, (boundX, boundY), current)
            if((boundX <0 ) or (boundX> len(mazeInit[0])) or (boundY <0 ) or (boundY> len(mazeInit))):
                #print("out of bounds")
                pass
            elif (boundX == endValue[0] and boundY ==  endValue[1]):
                v[boundY][boundX] = 'v'
                p[boundY][boundX] = (current[0],current[1])
                dist[boundY][boundX] = dist[current[1]][current[0]]+1 
                break
            elif( mazeInit[boundY][boundX] =='True'):
                #print("can't run into wall")
                pass
            elif v[boundY][boundX]!= 'v':
                v[boundY][boundX] = 'v'
                p[boundY][boundX] = (current[0],current[1])
                dist[boundY][boundX] = dist[current[1]][current[0]]+1 
                q.append((boundX, boundY))
                #print(q)
                        
                #printMaze(maze,start,end,(boundX,boundY))
                #print(boundX, boundY)
            else:
                #print("cant revisit noded")
                pass

    print(p[endValue[1]][endValue[0]], dist[endValue[1]][endValue[0]])
    #printMatrix(p)
    #printMatrix(dist)
    """                
    #print(v.x, v.y, v.parent,v.dist)
    """
def createGrid(dims,periods,reord):
    comm = MPI.COMM_WORLD.Create_cart(dims, periods, reord)
    return comm


def rank0(maze,comm, rank):
    
    pass

def subRanks(maze, comm, rank):
    pass


rows = int(sys.argv[1])
cols = int(sys.argv[2])

(maze,inital) = gm.gen(int(sys.argv[1]),int(sys.argv[2]))

start = inital[0]
end = inital[1]
#startNode = maze[start[1]][start[0]]
print((start[0],start[1]), (end[0],end[1]))
printMaze(maze,start,end,(-1,-1))
print()
bfsSearch(maze, start,end)



