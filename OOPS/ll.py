# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
size_of_ll = 0

class LL:
    # 1. Add value x before first element => 0

    def add_element_at_beginning(self,value):
        global size_of_ll
        global head
        temp = ListNode(value)
        temp.next = head
        head = temp
        size_of_ll += 1


    # 2. Add value x at last              => 1

    def add_element_at_end(self,value):
        global size_of_ll
        global head
        count = 0
        newNode = ListNode(value)
        temp = head
        while (count <= size_of_ll):
            temp = temp.next
            count += 1
        temp = newNode
        size_of_ll += 1


    # 3. Add a value before indexed node  => 2
    # - if index is = to length append at last *imp*
    # - if index is greater or minus ignore it

    def add_element_before_index_ignore_if_gretaer(self,positon, value):
        global size_of_ll
        global head
        count = 0
        temp = ListNode(value)

        if positon > size_of_ll:
            return

        if positon == size_of_ll:
            add_element_at_end(value)
            return

        prev = head

        while positon >= 0 and positon - 1 < count:
            prev = prev.next
            count += 1
        temp.next = prev.next
        prev.next = temp

        size_of_ll += 1


# 4. Delete the index node if valid **imp** =>3
def delete_index_node(self,positon):
    global size_of_ll
    global head
    count = 0
    temp = head
    while (count < positon - 1):
        temp = temp.next
        count += 1
    temp.next = temp.next.next


def print_ll():
    global head
    tmp = head
    ans = []
    while tmp is not None:
        ans.append(str(tmp.val))
        tmp = tmp.next
    print("->".join(ans))


# Index is 0 Based

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(A):
        arr_size = len(A)

        for i in range(arr_size):
            if A[i][0] == 0:
                add_element_at_beginning(A[i][1])
                add_element_at_beginning(A[i][2])

            if A[i][0] == 1:
                add_element_at_end(A[i][1])
                add_element_at_end(A[i][2])
            if A[i][0] == 2:
                add_element_before_index_ignore_if_gretaer(A[i][1], A[i][2])
            if A[i][0] == 3:
                delete_index_node(A[i][1])
                delete_index_node(A[i][2])

        print_ll()

A = [   [0, 1, -1],
            [1, 2, -1],
            [2, 3, 1]   ]

Solution.solve(A)



