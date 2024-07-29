from UniquePathsGrid import *

solution = Solution()

def test_recursion():
    assert solution.uniquePathsWithObstacles1 ([[0,0,0],
                                                [0,1,0],
                                                [0,0,0]]) == 2
    assert solution.uniquePathsWithObstacles1 ([[1, 0]]) == 0
    assert solution.uniquePathsWithObstacles1 ([[0, 1]]) == 0
    assert solution.uniquePathsWithObstacles1 ([[0, 0],
                                                [0, 0],
                                                [0, 0],
                                                [1, 0],
                                                [0, 0]]) == 3
    assert solution.uniquePathsWithObstacles1 ([[0, 0, 0, 0, 0, 1, 0, 0, 0]]) == 0

def test_bottom_up():
    assert solution.uniquePathsWithObstacles2 ([[0,0,0],
                                                [0,1,0],
                                                [0,0,0]]) == 2
    assert solution.uniquePathsWithObstacles2 ([[1, 0]]) == 0
    assert solution.uniquePathsWithObstacles2 ([[0, 1]]) == 0
    assert solution.uniquePathsWithObstacles2 ([[0, 0],
                                                [0, 0],
                                                [0, 0],
                                                [1, 0],
                                                [0, 0]]) == 3
    assert solution.uniquePathsWithObstacles2 ([[0, 0, 0, 0, 0, 1, 0, 0, 0]]) == 0

test_bottom_up()