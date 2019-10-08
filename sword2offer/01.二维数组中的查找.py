#https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

# ************************************#
# *************solution 2*************#
# ************************************#
##这个算法实现了二分查找，复杂度应该是O(N*logM)。
#212ms+5740k
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array[0]) == 0:
            return False
        for i in range(len(array)-1,-1,-1):
            if array[i][0] > target:
                pass
            elif array[i][0] == target:
                return True
            else:
                m,n = 0,len(array[0])-1
                while m <= n:
                    middle = (m+n)//2
                    if array[i][middle] == target:
                        return True
                    elif array[i][middle] > target:
                        n = middle-1
                    else:
                        m = middle+1
        return False


if __name__ == "__main__":
    target = 7
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13]]
    solution = Solution()
    result = solution.Find(target,array)
    print(result)


#214ms+5852k，这个的算法复杂度应该是O(N*M)
# ************************************#
# *************solution 1*************#
# ************************************#
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array[0]) == 0:
            return False
        for i in range(len(array)-1,-1,-1):
            if array[i][0] > target:
                pass
            elif array[i][0] == target:
                return True
            else:
                for j in range(len(array[0])):
                    if array[i][j] == target:
                        return True
        return False
"""