def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    search_space = {}
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                search_space[(i, j)] = True
    print(search_space)
    while (len(search_space) > 0):
        area = 1
        (i, j) = search_space.popitem()[0]
        
        stack = [(i, j)]
        while (len(stack)>0):
            elt = stack.pop(-1)
            neighbours = []
            if elt[0] > 0: neighbours.append((elt[0] - 1, elt[1]))
            if elt[0] < len(grid) - 1: neighbours.append((elt[0] + 1, elt[1]))
            if elt[1] > 0: left = neighbours.append((elt[0], elt[1] - 1))
            if elt[1] < len(grid[0]) - 1: left = neighbours.append((elt[0], elt[1] + 1))
            print('here')
            for neighbour in neighbours:
                if neighbour in search_space:
                    stack.append(neighbour)
                    search_space.pop(neighbour)
                    area += 1
        max_area = max(area, max_area)

    return max_area

print(maxAreaOfIsland(
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
))