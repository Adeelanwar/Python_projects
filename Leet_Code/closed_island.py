def closedIsland(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print(len(grid))
        print(len(grid[0]))
        search_space = {}
        islands = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    search_space[(i, j)] = True
        while (len(search_space) > 0):
            touched_edge = False
            (i, j) = search_space.popitem()[0]
            stack = [(i, j)]
            while (len(stack)>0):
                elt = stack.pop(-1)
                neighbours = []
                
                if elt[0] > 0: neighbours.append((elt[0] - 1, elt[1]))
                if elt[0] < len(grid) - 1: neighbours.append((elt[0] + 1, elt[1]))
                if elt[1] > 0: left = neighbours.append((elt[0], elt[1] - 1))
                if elt[1] < len(grid[0]) - 1: left = neighbours.append((elt[0], elt[1] + 1))
                for neighbour in neighbours:
                    if neighbour[0] == 0 or neighbour[0] == len(grid) - 1 or neighbour[1] == 0 or neighbour[1] == len(grid[0]) - 1:
                        if grid[neighbour[0]][neighbour[1]] == 0:
                            touched_edge = True
                    if neighbour in search_space:
                        stack.append(neighbour)
                        search_space.pop(neighbour)
            if touched_edge == False:
                islands += 1
            else:
                touched_edge = True
        return islands

print(closedIsland([[0,0,1,1,0,1,0,0,1,0],
                    [1,1,0,1,1,0,1,1,1,0],
                    [1,0,1,1,1,0,0,1,1,0],
                    [0,1,1,0,0,0,0,1,0,1],
                    [0,0,0,0,0,0,1,1,1,0],
                    [0,1,0,1,0,1,0,1,1,1],
                    [1,0,1,0,1,1,0,0,0,1],
                    [1,1,1,1,1,1,0,0,0,0],
                    [1,1,1,0,0,1,0,1,0,1],
                    [1,1,1,0,1,1,0,1,1,0]]))