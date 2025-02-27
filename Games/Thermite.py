import pygame, sys
from pygame.locals import *
import random
import time 

maxmistakes = 3
dimension = 10
hblocks = dimension * 2 
nblocks = dimension * dimension
itime = 1
bordersize = 10
chance = 1

width = 200 - 12 * dimension
height = 200 - 12 * dimension
screenwidth = width * dimension
screenheight = height * dimension


BLUE  = (150, 150, 255)
RED   = (255, 100, 100)
GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


gameover = False
state = [0] * nblocks
cstate = [1] * hblocks + [0] * (nblocks - hblocks)
random.shuffle(cstate)
cmistakes = 0
ccorrect = 0

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
pygame.init()
DISPLAYSURF = pygame.display.set_mode((width * dimension,height * dimension))
DISPLAYSURF.fill(BLUE)
pygame.display.set_caption("Puzzle")

def creategraph():
    graph = {}
    for x in range(nblocks):
        left = x - 1
        right = x + 1
        top = x - dimension
        bottom = x + dimension
        nodes = []
        if (left + 1) % dimension != 0:
            nodes.append(left)
        if (right) % dimension != 0:    
            nodes.append(right)
        if (top - 1) % dimension != 0 :
            if top >= 0:
                nodes.append(top)
        if (bottom + 1) % dimension != 0:
            if bottom < (dimension * dimension):
                nodes.append(bottom)
        graph[x] = nodes
    return graph

def bfs(graph):
    queue = []
    visited = [False] * nblocks
    queue.append(random.choice([i for i in range(nblocks - 1)]))
    print(len(visited))
    while len(queue) > 0:
        vertex = queue.pop(0)
        print(vertex)
        visited[vertex] = True
        neighbours = graph[vertex]
        if random.random() < chance:
            cstate[vertex] = 1
        for neighbour in neighbours:
            if visited[neighbour] == False:
                visited[vertex] = True
                queue.append(neighbour)
                
def drawpuzzle(state):
    for i in range(len(state)):
        if state[i] == 0:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, BLUE, (topleft,bottomleft, width, height))
        if state[i] == 1:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, WHITE, (topleft,bottomleft, width, height))
        if state[i] == 2:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, RED, (topleft,bottomleft, width, height))
    for x in range(dimension + 1):
        pygame.draw.line(DISPLAYSURF, BLACK,(x * width,0),(x * width,screenheight),bordersize)
        pygame.draw.line(DISPLAYSURF, BLACK,(0,x * height),(screenwidth,x * height),bordersize)

def drawfinal(state):
    for i in range(len(state)):
        if cstate[i] == 0:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, BLUE, (topleft,bottomleft, width, height))
        if cstate[i] == 1:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, GREEN, (topleft,bottomleft, width, height))
        if cstate[i] == 2:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, WHITE, (topleft,bottomleft, width, height))
        if cstate[i] == 3:
            topleft = (i % dimension) * width 
            bottomleft = int(i / dimension) * height
            pygame.draw.rect(DISPLAYSURF, RED, (topleft,bottomleft, width, height))
            
    for x in range(dimension + 1):
        pygame.draw.line(DISPLAYSURF, BLACK,(x * width,0),(x * width,screenheight),bordersize)
        pygame.draw.line(DISPLAYSURF, BLACK,(0,x * height),(screenwidth,x * height),bordersize)

def update(pos = (0,0)):
    global cmistakes, ccorrect, gameover, cstate
    
    if cmistakes >= maxmistakes:
        gameover = True
    if ccorrect >= hblocks:
        gameover = True
    if(pos != (0,0)):
        x = int(pos[0] /  width)
        y = int(pos[1] /  width)
        if cstate[x + y * dimension] == 1:
            state[x + y * dimension] = 1
            cstate[x + y * dimension] = 2
            ccorrect += 1
        elif(cstate[x + y * dimension] == 0):
            state[x + y * dimension] = 2
            cstate[x + y * dimension] = 3
            cmistakes += 1
    pos = (0,0)
    if gameover == True:
        drawfinal(cstate)
    else:
        drawpuzzle(state)
    pygame.display.update()

def intializepuzzle():
    global cmistakes, ccorrect, gameover, cstate, state
    gameover = False
    state = [0] * nblocks
    cstate = [1] * hblocks + [0] * (nblocks - hblocks)
    random.shuffle(cstate)
    cmistakes = 0
    ccorrect = 0
    drawpuzzle(cstate)
    pygame.display.update()
    time.sleep(itime)
    gameover = False
def main():
    global gameover
    
    intializepuzzle()
    update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if gameover == False:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    update(pos)
            if event.type == pygame.KEYUP:
                intializepuzzle()
                update()
        update()
        FramePerSec.tick(FPS)

# Initialize program
main()
