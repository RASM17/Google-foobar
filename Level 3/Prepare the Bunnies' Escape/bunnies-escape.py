# Calculate all a board with all paths
def calculatePathsBoard(x, y, map):
    height = len(map)
    width = len(map[0])
    pathsBoard = [[None for i in range(width)] for i in range(height)]
    pathsBoard[x][y] =1
    directions = [[1,0],[-1,0],[0,-1],[0,1]]
    currentPoint = [(x, y)]
    while( currentPoint):
        x, y = currentPoint.pop(0)
        for dire in directions:
            nX, nY = x + dire[0], y+dire[1]
            if ( 0 <= nX < height and 0 <= nY < width):
                    if pathsBoard[nX][nY] is None:
                        pathsBoard[nX][nY] = pathsBoard[x][y] + 1
                        if (map[nX][nY] == 1):
                            continue #1 chance to destroy a wall
                        currentPoint.append((nX,nY))
    #printMap(paths) 
    return pathsBoard
    
#Print the map to visualize
def printMap(map):
    for i in range(len(map)):
        print(map[i])
    
def solution(map):
    #printMap(map)
    height = len(map)
    width = len(map[0])

    pathsBoardfromStart = calculatePathsBoard(0,0, map)
    pathsBoardfromEnd = calculatePathsBoard(height-1,width-1, map)
    result = 2*height*width
    for i in range(height):
        for j in range(width):
            if(pathsBoardfromStart[i][j] and pathsBoardfromEnd[i][j]):
                result = min(pathsBoardfromStart[i][j] + pathsBoardfromEnd[i][j] -1, result)
    return result

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))