#https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回
"""


#712ms+5720k   这个是O(n)的算法
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            for i in range(len(rotateArray)-1):
                if rotateArray[i] > rotateArray[i+1]:
                    return rotateArray[i+1]


if __name__ == "__main__":
    num = [3,4,5,1,2]
    solution = Solution()
    result = solution.minNumberInRotateArray(num)
    print(result)
