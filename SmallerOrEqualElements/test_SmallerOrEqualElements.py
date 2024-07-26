from SmallerOrEqualElements import solve

def testSolve():
    assert solve([1, 3, 4, 4, 6], 4) == 4
    assert solve([1, 2, 5, 5], 3) == 2
    assert solve([4, 4, 12, 12, 15, 19, 23, 24, 34, 42], 48) == 10
