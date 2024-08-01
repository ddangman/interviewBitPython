'''
https://www.youtube.com/watch?v=aPQY__2H3tE 
1) Visualize the problem. Can the problem be represented by a directed acyclic graph?
2) Find an appropriate subproblem. Think size 1. Entire problem is also a subproblem.
3) Find relationships among subproblems. From entire problem, what subproblem needs to be solved?
4) Generalize the relationship.
5) Implement by solving subproblems in order.
'''

class Box:
    def __init__(self, d, w, h):
        self.d = d
        self.w = w
        self.h = h

def canStack(top, bottom):
    return top.w < bottom.w and top.d < bottom.d

def tallestStack(boxes):
    # subproblems must be solved in order
    # sort the boxes by their base depth
    # alternatively, we could sort by base width
    boxes.sort(key=lambda _: _.d)

    # create a dictionary to store the current max height of each box
    # ie solve the partial path of the directed acyclic graph for each box
    # initially, the max height of each box is the height of the single box
    dp = {box: box.h for box in boxes}

    # iterate through the sorted boxes from smallest to largest base depth
    for j in range(1, len(boxes)):
        box_j = boxes[j]
        # find all the boxes that can fit on top of the current box
        # from left to right, list is directed acyclic graph
        # being sorted, leftmost box can stack on 2nd leftmost box, ... , rightmost box is on bottom
        fitsOnTop = [boxes[i] for i in range(j) if canStack(boxes[i], box_j)]
        # update the max height of the current box by selecting the max subset of boxes that can fit on top
        # if there are no boxes that can fit on top, ie. fitsOnTop is empty, then max() will return 0
        dp[box_j] = box_j.h + max([dp[fit] for fit in fitsOnTop], default=0)

    return max(dp.values())


# Driver Code
if __name__ == "__main__":
    boxes = [Box(1, 5, 4), Box(1, 2, 2), Box(2, 3, 2),
            Box(2, 4, 1), Box(3, 6, 2), Box(4, 5, 3)]

    print("The maximum possible height of stack is",
           tallestStack(boxes))