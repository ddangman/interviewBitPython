class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        # LIS minimum is 1 for each element
        dp = [1] * len(A)
        # For each element in A
        # check to see if ith tuple element is less than the current jth element
        for j in range(1, len(A)):
            for i in range(0, j):
                if A[i] < A[j]:
                    # keep track of the maximum LIS
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
    
    def return_lis(self, A):
        dp = [1] * len(A)
        prev = [-1] * len(A)
        max_index = 0
        for j in range(1, len(A)):
            for i in range(0, j):
                if A[i] < A[j] and dp[j] < dp[i] + 1:
                    prev[j] = i
                    dp[j] = dp[i] + 1
                    if dp[j] > dp[max_index]:
                        max_index = j
                    
        reversed_lis = [max_index]
        while prev[max_index] != -1:
            reversed_lis.append(prev[max_index])
            max_index = prev[max_index]
        return(reversed_lis[::-1])
                    