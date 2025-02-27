def numEnclaves(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        search_space = {}
        islands = 0
        enclaves = []
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1:
                    search_space[(i, j)] = True
        while (len(search_space) > 0):
            enclave = []
            touched_edge = False
            (i, j) = search_space.popitem()[0]
            enclave.append((i, j))
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
                        if grid[neighbour[0]][neighbour[1]] == 1:
                            touched_edge = True
                            continue
                    if neighbour in search_space:
                        stack.append(neighbour)
                        enclave.append(neighbour)
                        search_space.pop(neighbour)
            if touched_edge == False:
                islands += 1
                enclaves += enclave
                
        return len(enclaves)

print(numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))