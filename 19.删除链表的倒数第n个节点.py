#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nn = 0
        while head:
            nn+=1
        temp = head
        while temp:
            if nn==n:
                temp.next=temp.next.next
                temp.val = temp.next.val
                break
            else:
                n-=1
                temp = temp.next
        print head
        return head
# @lc code=end

