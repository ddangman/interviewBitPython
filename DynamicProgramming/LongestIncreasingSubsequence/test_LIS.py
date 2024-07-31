from LIS import *

solution = Solution()

def test_bottom_up():
    assert solution.lis([1, 2, 1, 5]) == 3
    assert solution.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
    assert solution.lis([1]) == 1

def test_return_lis():
    assert solution.return_lis([1, 2, 1, 5]) == [0, 1, 3]
    assert solution.return_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == [0, 2, 6, 9, 11, 15]
    assert solution.return_lis([1]) == [0]