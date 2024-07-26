def solve(A, B):
    # check bottom edge case
    if B < A[0]:
        return 0
    # check top edge case
    if B >= A[-1]:
        return len(A)

    # lower bound
    lb = 0
    # upper bound
    ub = len(A) - 1
    index = int((ub + lb) / 2)

    while lb < ub:
        # if the element at the index is less than or equal to B
        if A[index] <= B:
            # set lower bound to right of index
            lb = index + 1
        else:
            # set upper bound to index
            # using index - 1 will cause rounding error
            # int() will always round towards zero
            ub = index
        index = int((ub + lb) / 2)

    return index