#coding=utf-8

class A:

    __instance = None

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls):
        if A.__instance is None:
            A.__instance = A()
        return A.__instance

    def a(self):
        self.b()

    def b(self):
        print "aaaa"

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

## 递归
## 1、取root的值与target比较，大 pass,小 ：返回val值，分别递归比较左右节点 与target-rootVal 比较

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        pass

    G_OK = "ok"
    G_FAIL = "fail"

    def everyRootTree(self,node,target,arr):
        if node == None :
            if target ==0:
                return Solution.G_OK
            else:
                return Solution.G_FAIL
        returnVal = None
        if node.val < target :
            arr.append(node.val)
            returnVal = node.val
            leftVal = self.everyRootTree(self,node.left,target-node.val)
            rightVal = self.everyRootTree(self,node.right,target-node.val)
        return returnVal


# from collections import OrderedDict
# # list = [1,4,2,3]
# # list2 = list[:]
# # list.sort()
# # print list
# # print list2
# dic = OrderedDict()
# dic["z"] = [0,0]
# dic["a"] = [1,2]
# dic["d"] = [2,2]
# dic["c"] = [1,1]
#
# list = [1,2,3,4,5,6]
#
# print list[1:5]
class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return '(Student: %s, %s,%s)' % (self.name,self.grade,self.age)
    __repr__ = __str__

    def __getitem__(self, item):
        if item==0:
            return self.name
        elif item==1:
            return self.grade
        else:
            return self.age

from operator import itemgetter,attrgetter
# students = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10),Student('dave', 'A', 10)]
#
# # print sorted(students, key=lambda Student : (Student.age,Student.grade)) # sort by age
# list2 = [1,2,3,4,5,6]
# print list2
# list2.sort(reverse=True)
# # students.sort(key=lambda Student : (Student.age,Student.grade))
# students.sort(key=itemgetter(2,1))
# # sorted(students,key=itemgetter(2))
# print students
#
# d = {'data1':3, 'data3':1, 'data2':2, 'data4':4}
# # print sorted(d.iteritems(), key=itemgetter(0), reverse=True)
# tup =(4,7,5)
# print sorted(tup)
#
# str1 = "aba"
# str2 = str1[::-1]
# print str1
# print str2
# print str1==str2
# print str1.replace("a","",1)
# print len(str1)
# if 'a'in str2:
#     print True
# a = 121
# b = str(a)[::-1]
# print str(a)
# print b
# print str(a)==b
def test():
    for i in range(0,5):
        if i == 2:
            print 'i=%d' %i
            return True
        print i
    return False

print test()

