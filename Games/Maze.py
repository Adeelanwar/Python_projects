import pygame, sys
from pygame.locals import *
import random
import time


BLUE  = (150, 150, 255)
RED   = (255, 100, 100)
GREEN = (100, 255, 100)
BLACK = (40, 40, 40)
WHITE = (215, 215, 215)

maze_length = 50
block_size = 8
maze = [[1 for i in range(maze_length)]
            for j in range(maze_length)]

#borders


#Generating maze using prism's method



# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '0'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '0'):
		s_cells += 1

	return s_cells


## Main code
# Init variables
wall = 1
cell = 0
unvisited = 1
height = maze_length
width = maze_length
maze = []


# Denote all cells as unvisited
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 2
maze[starting_height][starting_width - 1] = 2
maze[starting_height][starting_width + 1] = 2
maze[starting_height + 1][starting_width] = 2

while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 1 and maze[rand_wall[0]][rand_wall[1]+1] == 0):
			# Find the number of surrounding cells
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 0

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 0):
						maze[rand_wall[0]-1][rand_wall[1]] = 2
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# Bottom cell
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 0):
						maze[rand_wall[0]+1][rand_wall[1]] = 2
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != 0):
						maze[rand_wall[0]][rand_wall[1]-1] = 2
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 1 and maze[rand_wall[0]+1][rand_wall[1]] == 0):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 0

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 0):
						maze[rand_wall[0]-1][rand_wall[1]] = 2
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 0):
						maze[rand_wall[0]][rand_wall[1]-1] = 2
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# Rightmost cell
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 0):
						maze[rand_wall[0]][rand_wall[1]+1] = 2
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 1 and maze[rand_wall[0]-1][rand_wall[1]] == 0):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 0

				# Mark the new walls
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 0):
						maze[rand_wall[0]+1][rand_wall[1]] = 2
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 0):
						maze[rand_wall[0]][rand_wall[1]-1] = 2
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 0):
						maze[rand_wall[0]][rand_wall[1]+1] = 2
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# Check the right wall
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 1 and maze[rand_wall[0]][rand_wall[1]-1] == 0):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 0

				# Mark the new walls
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 0):
						maze[rand_wall[0]][rand_wall[1]+1] = 2
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 0):
						maze[rand_wall[0]+1][rand_wall[1]] = 2
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != 0):
						maze[rand_wall[0]-1][rand_wall[1]] = 2
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


# Mark the remaining unvisited cells as walls
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 1):
			maze[i][j] = 2

# Set entrance and exit
for i in range(0, width):
	if (maze[1][i] == 0):
		maze[0][i] = 0
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == 0):
		maze[height-1][i] = 0
		break

maze[0][1] = 1
maze[-1][-2] = 3
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
# Setting up color objects
pygame.init()
DISPLAYSURF = pygame.display.set_mode((block_size * maze_length,block_size * maze_length))
DISPLAYSURF.fill(BLUE)
pygame.display.set_caption("Puzzle")

def create_graph(maze):
    graph = {}
    for j in range(maze_length - 1):
        for i in range(1, maze_length - 1):
                if maze[i][j] != 2:
                        graph[i + j * maze_length] = []
                        if maze[i][j + 1] != 2:
                                graph[i + j * maze_length].append(i + (j + 1) * maze_length)
                        if maze[i + 1][j] != 2:
                                graph[i + j * maze_length].append(i + 1 + j * maze_length)
    return graph

graph = create_graph(maze)
graph[maze_length - 2 + (maze_length - 1) * maze_length] = []
print(graph)
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
#bfs(visited, graph, 1)

def drawmaze(maze):
    for i in range(maze_length):
        for j in range(maze_length):
            topleft = i * block_size
            bottomleft = j * block_size
            if maze[j][i] == 1:
                pygame.draw.rect(DISPLAYSURF, BLUE, (topleft,bottomleft, block_size, block_size))
            elif maze[j][i] == 2:
                pygame.draw.rect(DISPLAYSURF, BLACK, (topleft,bottomleft, block_size, block_size))
            elif maze[j][i] == 3:
                pygame.draw.rect(DISPLAYSURF, RED, (topleft,bottomleft, block_size, block_size))
            elif maze[j][i] == 0:
                pygame.draw.rect(DISPLAYSURF, WHITE, (topleft,bottomleft, block_size, block_size))
def update():
    pass
gameover =True
def main():
    global gameover
    
    drawmaze(maze)
    pygame.display.update()
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
                update()
        update()
        FramePerSec.tick(FPS)
main()

