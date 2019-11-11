#https://leetcode-cn.com/problems/maximize-distance-to-closest-person/

"""
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
至少有一个空座位，且至少有一人坐在座位上。
亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
返回他到离他最近的人的最大距离。

示例 1：输入：[1,0,0,0,1,0,1];输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。

示例 2：输入：[1,0,0,0]输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
"""



class Solution:
    def maxDistToClosest(self, seats: list):
        """
        这道题目分成三个部分来考虑，也就是这个人坐在两边和中间。
        """
        tmp = []
        if seats[0] == 0:
            for i in range(1,len(seats)):
                if seats[i] == 1:
                    tmp.append(i)
                    break
        if len(tmp) == 0:
            tmp.append(0)

        if seats[-1] == 0:
            for j in range(len(seats)-1,-1,-1):
                if seats[j] == 1:
                    tmp.append(len(seats) - 1 - j)
                    break
        if len(tmp) == 1:
            tmp.append(0)

        middle = []
        count = 1
        for k in range(tmp[0],len(seats)-tmp[1]-1):
            if seats[k] == 0 and seats[k+1] == 0:
                count = count + 1
                middle.append(count)
            else:
                count = 1
        if len(middle) == 0:
            middle.append(1)

        tmp.append(int((max(middle)+1)/2))
        return max(tmp)


if __name__ == "__main__":
    seats = [1,0,1]
    solution = Solution()
    result = solution.maxDistToClosest(seats)
    print(result)


