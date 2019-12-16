#https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

"""
给定一个二叉树，返回它的中序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=None    #左子树
        self.right=None  #右子树

class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

class Solution:
    def inorderTraversal(self, root: Node):
        if root == None:
            return []
        else:
            result = [root.value]
            left = self.inorderTraversal(root.left)
            right = self.inorderTraversal(root.right)
            return left+result+right


if __name__ == "__main__":
    tree = Tree()
    num = [1,2,3]
    for w in num:
        tree.add(w)
    solution = Solution()
    result = solution.inorderTraversal(tree.root)
    print(result)
