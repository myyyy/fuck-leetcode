#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [i for i in s]
        l = len(s)
        if l==1:return 0
        print l,s
        for i in range(l):
            print s[i],s[i+1:]
            if s[i] not in s[i+1:]:
                return i
        return -1
# @lc code=end

