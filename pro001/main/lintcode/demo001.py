#coding=utf-8

## 刷题网址：http://lintcode.com/zh-cn/problem/#


# 612、 K个最近的点
# 给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序。

# 给出 points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
# 返回 [[1,1],[2,5],[4,4]]

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution1:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        list = []
        for point in points:
            distance = self.getDistance(point, origin)
            list.append(PointXY(point.x,point.y,distance))
        sortList = sorted(list,key=lambda PointXY:(PointXY.dis,abs(PointXY.x)))
        out=[]
        for pointXY in sortList[0:k]:
            out.append(Point(pointXY.x,pointXY.y))
        return out



    def getDistance(self,point,origin):
        return (point.x-origin.x)*(point.x-origin.x)+(point.y-origin.y)*(point.y-origin.y)

class PointXY:
    def __init__(self, a=0, b=0,dis=0):
        self.x = a
        self.y = b
        self.dis = dis

# points = [Point(4,6),Point(4,7),Point(4,4),Point(-1,-1),Point(1,1)]
#
# print Solution().kClosest(points,Point(0,0),3)


# 382 、给定一个整数数组，在该数组中，寻找三个数，分别代表三角形三条边的长度，问，可以寻找到多少组这样的三个数来组成三角形？
# 给定数组 S = {3,4,6,7}，返回 3
# 其中我们可以找到的三个三角形为：
# {3,4,6}
# {3,6,7}
# {4,6,7}
# 给定数组 S = {4,4,4,4}, 返回 4
# 其中我们可以找到的三个三角形为：
# {4(1),4(2),4(3)}
# {4(1),4(2),4(4)}
# {4(1),4(3),4(4)}
# {4(2),4(3),4(4)}
import itertools
class Solution2:
    def triangleCount(self, S):
        count = 0
        for iter in itertools.combinations(S,3):
            if self.isTrigle(iter):
                count += 1
        return count

    def isTrigle(self,tuple):
        list = sorted(tuple)
        if list[0]+list[1]>list[2]:
            return True
        return False

    def combine_increase(self,arr,startIndex,result,count,num,arr_len):
        for i in range(startIndex,arr_len):
            result[count-1]=i
            if count-1 == 0:
                print result
            else:
                self.combine_increase(arr,i+1,result,count-1,num,arr_len)
        pass

arr = [1,2,3,4]
outArr =[0]*3
Solution2().combine_increase(arr,0,outArr,3,3,4)
import numpy
#[1,2,7,8,5]  k =3
def medianSlidingWindow( nums, k):
    out = []
    if len(nums) == 0:
        return out
    for i in range(0,len(nums)-k+1):
        midArr = nums[i:k+i]
        out.append(getMidNum(midArr))
    return out

def getMidNum(midArr):
    # numpy.sort(midArr)
    midArr.sort()
    arrLen = len(midArr)
    if arrLen%2 == 0:
        return midArr[arrLen/2-1]
    else:
        return midArr[(arrLen-1)/2]

aaa = [1,2,7,7,2]
print medianSlidingWindow(aaa,3)




