# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        sum = str(int((''.join(map(str, l1)))) + int((''.join(map(str, l2)))))
        sum = [int(i) for i in sum]

        return sum


s = Solution()
print(s.addTwoNumbers([1, 2, 3], [3, 2, 1]))
