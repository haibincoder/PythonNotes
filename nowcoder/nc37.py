"""
题目描述
给出一组区间，请合并所有重叠的区间。
示例1
输入
复制
[[10,30],[20,60],[80,100],[150,180]]
返回值
复制
[[10,60],[80,100],[150,180]]
"""

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals ):
        # write code here
        result = []
        intervals.sort(key=lambda x:x.start)

        for item in intervals:
            if len(result) < 1 or result[-1].end < item.start:
                result.append(item)
            else:
                result[-1].end = max(result[-1].end, item.end)
        return result


