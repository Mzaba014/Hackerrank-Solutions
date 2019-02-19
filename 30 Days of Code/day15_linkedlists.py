'''
Title     : Linked List
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-linked-list/problem
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)  # Create new node to insert

        current = head  # Begin iteration at head of list
        if current:  # If the head is not None
            while current.next:  # Iterate as long as there is a .next aka to end of list
                current = current.next
            # Once at the end (tail), insert the newly created node
            current.next = node
        else:  # If the head is None, simply make the head the new node
            head = node

        return head  # Return a reference to the first node in the list


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
