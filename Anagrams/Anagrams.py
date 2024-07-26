def anagrams1(A):
    # list containing the indices of the anagrams
    result = []

    # set used to store matched words to preven duplicates
    removed_j = set()

    # list comprehension to sort all chars of each word in A
    B = [''.join(sorted(word)) for word in A]

    # iterate through the list of sorted words
    for i in range(len(B)):
        # store indices that match word i
        match_i = [i+1] # add 1 to index to match 1-based index
        for j in range(i+1, len(B)):
            # check if word j is already matched
            if j in removed_j:
                continue
            if B[i] == B[j]:
                match_i.append(j+1) # add 1 to index to match 1-based index
                removed_j.add(j) # add j to set to prevent duplicates using for loop's index
        # append inner list to result list if unmatched
        if i not in removed_j:
            result.append(match_i)

    return result

def anagrams2(A):
    # list of prime numbers to assign to each letter
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131]

    # store hash as key and list of indices as value
    dict = {}

    # iterate through the list of words using index since .index() results in collisions
    for i in range(len(A)):
        # calculate hash of word
        hash = 1
        for char in A[i]:
            hash *= primes[ord(char)-ord('a')]
        # check if hash is already in dict
        if hash in dict:
            dict[hash].append(i+1) # add 1 to index to match 1-based index
        else:
            dict[hash] = [i+1]

    # list containing the indices of the anagrams
    result = []

    # Extracting all dictionary values
    # Using loop + keys()
    for key in dict.keys() :
        result.append(dict[key])

    return result