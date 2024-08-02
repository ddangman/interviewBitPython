class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        # convert to list
        A = list(A)
        B = list(B)
        lenA = len(A)
        lenB = len(B)
        # build lenA+1 x lenB+1 matrix
        dp = [[0]*(lenB+1) for i in range(lenA+1)]

        # initialize top row [0, 1, 2, 3, ...]
        for a in range(lenA+1):
            dp[a][0] = a
        # initialize left column [0, 1, 2, 3, ...]
        for b in range(lenB+1):
            dp[0][b] = b
        
        # convert A to B
        for a in range(lenA):
            for b in range(lenB):
                # sub-problems
                
                # replace last char A if not equal
                replace = dp[a][b] + (0 if A[a] == B[b] else 1) 
                # delete last char A
                delete = dp[a][b+1] + 1
                # add last char
                insert = dp[a+1][b] + 1
                
                dp[a+1][b+1] = min(replace,delete,insert)

        return dp[lenA][lenB]
    
    
# Driver Code
if __name__ == "__main__":
    s = Solution()

    A = "abad"
    B = "abac"
    # 1: replace 'd' with 'c'
    print(s.minDistance(A, B))

    A = "Anshuman"
    B = "Antihuman"
    # 1: replace 's' with 't', 
    # 2: insert 'i'
    print(s.minDistance(A, B))