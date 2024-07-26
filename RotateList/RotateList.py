# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def rotateRight(A, B):
    count = 1
    current = A
    while current.next != None:
        count += 1
        current = current.next

    # snake the tail to the head
    current.next = A

    # calculate distance to the new tail
    mod = B % count
    count = count - mod
    # iterate to the new tail
    while count > 0:
        count -= 1
        current = current.next
    
    # mark the new head
    head = current.next

    # cut tail
    current.next = None

    return head


### code for testing ###
# modulo test case
input = [ 91, 34, 18, 83, 38, 82, 21, 69 ]
A = ListNode(input[0])
current = A
for i in range(1, len(input)):
    ln = ListNode(input[i])
    current.next = ln
    current = ln

head = rotateRight(A, 89)
# 69 -> 91 -> 34 -> 18 -> 83 -> 38 -> 82 -> 21 -> NULL
print(head.val)

# sample test case
input = [1, 2, 3, 4, 5]
# create linked list
A = ListNode(input[0])
current = A
for i in range(1, len(input)):
    ln = ListNode(input[i])
    current.next = ln
    current = ln

head = rotateRight(A, 2)
# 4->5->1->2->3->NULL
print(head.val)