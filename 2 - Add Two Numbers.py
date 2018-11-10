# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time : 1hr

class Solution:
    
    def __init__(self):
        self.increment = False
    
    def addDigit(self, i1,i2):
        i_sum = i1+i2
        if self.increment == True:
            i_sum += 1
            self.increment = False
        if i_sum >= 10:
            i_sum = i_sum%10
            self.increment = True
        return i_sum

    def finishOne(self,i):
        digit = self.addDigit(i.val,0)
        return digit
        
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1=l1
        i2=l2
        reversed_sum = []
        while i1 is not None and i2 is not None:
            i_sum = self.addDigit(i1.val,i2.val)
            reversed_sum.append(i_sum)
            i1 = i1.next
            i2 = i2.next
        while i1 is not None:
            reversed_sum.append(self.finishOne(i1))
            i1 = i1.next
        while i2 is not None:
            reversed_sum.append(self.finishOne(i2))
            i2 = i2.next
        if self.increment == True :
            reversed_sum.append(1)
        return reversed_sum
