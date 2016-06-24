"""
258. Add Digits
https://leetcode.com/problems/add-digits/
https://en.wikipedia.org/wiki/Digital_root
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num - (num-1)/9*9 if num else 0
        
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num if num < 10 else self.addDigits(num%10 + self.addDigits(num/10))
