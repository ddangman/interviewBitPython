def majorityElement(tuple):
    # track result for return
    result = tuple[0]
    # track count of result
    count = 1
    # track key value pairs
    dict = {}
    # iterate through tuple to count elements
    for t in tuple:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
        # check if current element count is greater than current result count
        if dict[t] > count:
            result = t
            count = dict[t]
    return result