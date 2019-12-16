#https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

"""
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        if root == None:
            return []
        else:
            result = [root.val]
            left = self.postorderTraversal(root.left)
            right = self.postorderTraversal(root.right)
        return left+right+result