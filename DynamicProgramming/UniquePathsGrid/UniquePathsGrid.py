class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles1(self, A):
        # check trivial case
        if A[0][0] == 1 or A[-1][-1] == 1:
            return 0
        global dict
        dict = {}
        result = recursion(A, 0, 0)
        dict = {}
        if result is None:
            return 0
        return result
    
    def uniquePathsWithObstacles2(self, A):
        # check trivial case
        if A[0][0] == 1 or A[-1][-1] == 1:
            return 0
        
        # create a 2D array to store the number of paths
        dp = [[0 for i in range(len(A[0])+1)] for j in range(len(A)+1)]
        for i in range(len(dp)):
            if i == 0: # out of bounds
                dp[i][0] = 0
            for j in range(len(dp[0])):
                if j == 0: # out of bounds
                    dp[0][j] = 0
                elif i == 1 and j == 1: # starting point is unblocked
                    dp[i][j] = 1
                elif A[i-1][j-1] == 1: # blocked path
                    dp[i][j] = 0
                else: # can arrive from left or above
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]




def count_paths(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a + b

def recursion(A, i, j):
    # if invalid move, return None
    if i >= len(A) or j >= len(A[0]) or A[i][j] == 1:
        return None
    # if at the end, return 1
    if i == len(A) - 1 and j == len(A[0]) - 1:
        return 1
    # if solution in dict, return it
    if (i, j) in dict:
        return dict[(i, j)]
    right = recursion(A, i, j + 1)
    down = recursion(A, i + 1, j)
    answer = count_paths(right, down)
    dict[(i, j)] = answer
    return answer