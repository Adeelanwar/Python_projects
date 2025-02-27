from cgi import print_arguments


def shortestPathBinaryMatrix(grid):
        width = len(grid[0])
        height = len(grid)
        goal = (height - 1, width - 1)
        if grid[0][0] == 1 or grid[goal[0]][goal[1]]:
            return -1
        searchspace = set()
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    searchspace.add((i, j))
        queue = [(0, 0)]
        searchspace.remove((0, 0))
        distance = 1
        

        haveneighbours = True
        while(len(queue) > 0):
            elt = queue.pop(0)
            
            if elt == goal:
                return distance
            if haveneighbours == True:    
                distance += 1
            haveneighbours = False
            i = elt[0]
            j = elt[1]
            neighbours = {(i - 1, j - 1), (i, j - 1), (i, j - 1),(i - 1, j), (i + 1, j),
                         (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)}
            if goal in neighbours:
                return distance
            for neighbour in neighbours:
                if neighbour in searchspace:
                    haveneighbours = True
                    queue.append(neighbour)
                    searchspace.remove(neighbour)
            print(elt, haveneighbours)
        return -1
print(shortestPathBinaryMatrix([[0,1],[1,0]]))
print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(shortestPathBinaryMatrix([[0,0,0],[1,0,0],[1,1,0]]))