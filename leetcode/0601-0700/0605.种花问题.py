# https://leetcode-cn.com/problems/can-place-flowers/

"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:输入: flowerbed = [1,0,0,0,1], n = 1;输出: True
示例 2:输入: flowerbed = [1,0,0,0,1], n = 2;输出: False
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        tmp = [-1]
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                tmp.append(i)
        tmp.append(len(flowerbed))
        if len(tmp) == 2:
            return int((len(flowerbed)+1)/2) >= n
        else:
            count = count + int((tmp[1]-tmp[0]-1)/2) + int((tmp[-1]-tmp[-2]-1)/2)
            for j in range(1,len(tmp) - 2):
                if (tmp[j + 1] - tmp[j] - 1) > 2:
                    count = count + int((tmp[j + 1] - tmp[j] - 2) / 2)
        return count>=n


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    solution = Solution()
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)