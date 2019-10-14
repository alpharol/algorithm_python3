#https://leetcode-cn.com/problems/two-city-scheduling/

"""
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

示例：输入：[[10,20],[30,200],[400,50],[30,20]];输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
"""


#执行用时 :68 ms, 在所有 Python3 提交中击败了29.00%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def twoCitySchedCost(self, costs:list):
        #tmp = [0]*len(costs)
        for i in range(len(costs)):
            costs[i].append(costs[i][1]-costs[i][0])
        tmp = sorted(costs,key=(lambda x:x[-1]))

        ans = 0
        for i in range(len(costs)):
            if i <= len(costs)/2-1:
                ans = ans + tmp[i][1]
            else:
                ans = ans + tmp[i][0]
        return ans

if __name__ == "__main__":
    costs = [[10,20],[30,200],[400,50],[30,20]]
    solution = Solution()
    result = solution.twoCitySchedCost(costs)
    print(result)