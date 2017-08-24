# coding:utf-8


class Solution1(object):
    def twoSum(self, nums, target):
        index = list()
        for i in nums:
            if target - i == i:
                if nums.count(i) > 1:
                    index.append(nums.index(i))
                    index.append(nums.index(i, nums.index(i) + 1))
                    break
                else:
                    continue
            if target - i in nums:
                index.append(nums.index(i))
                index.append(nums.index(target - i))
                break
        return index

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        return

class Solution7(object):


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            return self.reverseInt(x)
        elif x == 0:
            return 0
        else:
            return -self.reverseInt(abs(x))

    def reverseInt(self, x):
        a = int(str(x)[::-1])
        if a > sys.maxint:
            return 0
        return a



# s = Solution1()
# list1 = [3, 2, 4]
# target = 6
# print list1.count(3)
# list2 = s.twoSum(list1, target)
# print list2
# a=123456
# b = str(a)
# c = list()
# for i in b:
#     c.append(i)
# c.reverse()
# print b[::-1]
import sys
s = Solution7()
print sys.maxint
print s.reverse(-1534236469)

