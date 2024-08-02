class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if A[0] == 0: # trivial case
            if n == 1: # already at the end
                return 0
            else:
                return -1 # stuck at the beginning

        position = 0 # initialize
        count = 0    # initialize

        while(position < n-1):
            count += 1 # count the jump
            current_reach = position + A[position]
            next_position = 0 # initialize
            next_reach = 0    # initialize

            if current_reach >= n-1: # already at the end
                break

            # check all elements within current_reach for max(next_reach)
            for next in range(position+1, current_reach+1):
                if next + A[next] > next_reach: # greater reach found
                    next_reach = next + A[next]
                    next_position = next
            position = next_position

        return count