"use of algrothim from https://en.wikipedia.org/wiki/Maze_generation_algorithm"""

import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import sys
import random


def maze(width=81, height=51, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                   Z[y_, x_] = 1
                   Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                   x, y = x_, y_
    #Z = Z.tolist()
    return Z


def display(mazeX):
    pyplot.figure(figsize=(10, 5))
    pyplot.imshow(mazeX, cmap=pyplot.cm.binary, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()

def convertToArray(mazeX):
    mazeMatrix = mazeX.tolist()
    return mazeMatrix

def startPoint(maze):
    randX = random.randint(1,len(maze[0])-2)
    randY = random.randint(1,len(maze)-2)
    while(maze[randY][randX] == 1 ):
        randX = random.randint(1,len(maze[0])-2)
        randY = random.randint(1,len(maze)-2)
    return (randX,randY)

def endPoint(maze,startPoint):
    randX = random.randint(1,len(maze[0])-2)
    randY = random.randint(1,len(maze)-2)
    while((maze[randY][randX] ==1) or (startPoint ==(randX,randY))):
        randX = random.randint(1,len(maze[0])-2)
        randY = random.randint(1,len(maze)-2)

    return (randX,randY)
def mazeChange(maze,col, row):
    maze2= [] 
    for i in range(0, len(maze)):
        mazeX = []
        for j in  range(0, len(maze[0])):
                mazeX.append(str(maze[i][j]))
        maze2.append(mazeX)
    return maze2

def startEnd(maze,cols,rows):
    x = mazeChange(maze, cols, rows) 
    start = startPoint( x)
    end = endPoint( x, start)
    #x[start[1]][start[0]] = "S"
    #x[end[1]][end[0]] = "E"
    return (start,end)

def gen(rows, cols):

    #rows = int(sys.argv[1])
    #cols = int(sys.argv[2])
    x = maze(rows, cols)
    maze1 = mazeChange(x,cols,rows)
    intial = startEnd(maze1,cols,rows)
    return (maze1, intial)

