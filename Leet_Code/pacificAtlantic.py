from unittest.mock import seal


def pacificAtlantic(heights):
        search_space = {}
        x = len(heights) - 1
        y = len(heights[0]) - 1
        search_space = []
        for i in range(x):
            search_space.append([x, i])
            search_space.append([0, i])
        for j in range(y):
            search_space.append([y, j])
            search_space.append([0, j])
        islands = [[0, y], [x, 0]]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if heights[i][j] == '1':
                    search_space[(i, j)] = True
        
        while (len(search_space) > 0):
            (i, j) = search_space.pop(0)
            stack = [(i, j)]
            visited = [(i, j)]
            while (len(stack)>0):
                elt = stack.pop(-1)
                visited.append((i, j))
                neighbours = []
                if elt[0] > 0: neighbours.append((elt[0] - 1, elt[1]))
                if elt[0] < len(heights) - 1: neighbours.append((elt[0] + 1, elt[1]))
                if elt[1] > 0: neighbours.append((elt[0], elt[1] - 1))
                if elt[1] < len(heights[0]) - 1: neighbours.append((elt[0], elt[1] + 1))
                for neighbour in neighbours:
                    if neighbour not in visited:
                        if heights[elt[0]][elt[1]] <= heights[neighbour[0]][neighbour[1]]:
                            stack.append(neighbour)
                        
                            islands.append(neighbour)

        return islands

print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))