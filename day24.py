class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):#works only in non decreasing linked list
        if not head:
            return head
        current = head
        while current.next:
            if current.data is current.next.data:
                current.next = current.next.next
            else: current = current.next
        return head

    def delete_duplicates(self, head):# works in any kind of linked list
        current = head
        while current:
            runner = current
            while runner.next:
                if current.data is runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.delete_duplicates(head)
mylist.display(head)
