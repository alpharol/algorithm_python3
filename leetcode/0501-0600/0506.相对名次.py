#https://leetcode-cn.com/problems/relative-ranks/solution/python-by-phelan/

"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)

示例 1:输入: [5, 4, 3, 2, 1];输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
"""

class Solution:
    def findRelativeRanks(self, nums: list):
        tmp = []
        ans = [0]*len(nums)
        for i in range(len(nums)):
            tmp.append([nums[i],i])
        tmp_1 = sorted(tmp,key=lambda x:x[0],reverse=True)
        for k in range(len(tmp_1)):
            if k == 0:
                ans[tmp_1[0][1]] = "Gold Medal"
            elif k == 1:
                ans[tmp_1[1][1]] = "Silver Medal"
            elif k == 2:
                ans[tmp_1[2][1]] = "Bronze Medal"
            else:
                ans[tmp_1[k][1]] = str(k+1)
        return ans

if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    solution = Solution()
    result = solution.findRelativeRanks(nums)
    print(result)