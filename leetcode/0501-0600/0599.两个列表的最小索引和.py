#https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/

"""
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

示例 2:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
"""

# 执行用时 :300 ms, 在所有 python3 提交中击败了45%的用户
# 内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.52%的用户

class Solution:
    def findRestaurant(self, list1: list, list2: list):
        ans = []
        tmp = []
        for i in range(len(list1)):
            if list1[i] in list2:
                ans.append([i+list2.index(list1[i]),list1[i]])
        ans_sorted = sorted(ans,key= lambda x:x[0])
        for i in range(len(ans_sorted)):
            if ans_sorted[i][0] == ans_sorted[0][0]:
                tmp.append(ans_sorted[i][1])
        return tmp

if __name__ == "__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]

    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    solution = Solution()
    result = solution.findRestaurant(list1,list2)
    print(result)
