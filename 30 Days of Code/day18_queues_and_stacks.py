'''
Title     : Queues and Stacks
Subdomain : 30 Days of Code
Domain    : Python 3
Author    : Manuel Zabala
Created   : 2/19/2019
Problem   : https://www.hackerrank.com/challenges/30-queues-stacks/problem
'''
#!/bin/python3


import sys


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        # Array character to end of array which will function as stack
        self.stack.append(char)

    def enqueueCharacter(self, char):
        # Insert char at first index in array that will function as queue
        self.queue.insert(0, char)

    def popCharacter(self):
        # Remove the last char in the stack array aka the most recently inserted char.
        # This is because stacks are a LIFO structure so last element = first out
        return self.stack.pop()

    def dequeueCharacter(self):
        # Similarly, return the last element in the array which is the first element inserted
        # This is because queues are FIFO structure
        return self.queue.pop()


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
