class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        # LIS minimum is 1 for each element
        # so we initialize the dp array with 1
        dp = [1] * len(A)

        # 0 to j is the subproblem
        for j in range(1, len(A)):
            # i must be less than j since i is a subsequence of j
            for i in range(0, j):
                # check if the ith element is less than the jth element
                # since we are looking for increasing subsequence
                if A[i] < A[j]:
                    # keep track of the maximum LIS
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
    
    def return_lis(self, A):
        dp = [1] * len(A)
        # initialized as invalid index so we can check if the element is not part of the LIS
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
                    