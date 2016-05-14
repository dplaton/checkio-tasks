#!/usr/bin/env python3
"""
http://www.checkio.org/mission/count-neighbours/
"""
NEIGHBOUR_COORDS = ((-1,-1),(-1, 0), (-1,1),
                    (0, -1),(0, 1),
                    (1, -1),(1, 0), (1, 1))

def count_neighbours(grid, row, col):
    cnt=0
    transposed = list(map(list,zip(*grid)))
    
    for c in NEIGHBOUR_COORDS:
        x,y = row + c[0], col + c[1]
        if x in range(len(transposed[0])) and y in range(len(grid[0])):
            cnt+=grid[x][y]
    
    return cnt
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

    assert count_neighbours(((1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),    
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),), 5, 4) == 2, "Something test"
