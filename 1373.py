# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2021
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '7/20/21 10:11 AM'
"""
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

二叉搜索树的定义如下：

任意节点的左子树中的键值都 小于 此节点的键值。
任意节点的右子树中的键值都 大于 此节点的键值。
任意节点的左子树和右子树都是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_2_tree(l):
    """ 数组转换成二叉树 广度优先

    tree = list_2_tree([1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6])

    https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_1_1709.png
    """

    root = TreeNode(val=l[0])
    node_queue, idx = [root], 1

    while idx < len(l):
        parent = node_queue.pop(0)

        if l[idx] is not None:
            parent.left = TreeNode(val=l[idx])
            node_queue.append(parent.left)

        if l[idx + 1] is not None:
            parent.right = TreeNode(val=l[idx + 1])
            node_queue.append(parent.right)

        idx += 2

    return root


class Solution(object):

    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_bst_sum = [0]

        def bst(node):
            """ 检查是否是
            """
            if not node:
                return True, None, None, 0

            l_bst, left_min, left_max, sm_left_val = bst(node.left)
            r_bst, right_min, right_max, sm_right_val = bst(node.right)

            if not l_bst or not r_bst:
                return False, None, None, 0

            if left_max and left_max >= node.val:
                return False, None, None, 0

            if right_min and right_min <= node.val:
                return False, None, None, 0

            max_bst_sum.append(node.val + sm_left_val + sm_right_val)

            left_min = min(left_min, node.val) if left_min else node.val
            right_max = max(right_max, node.val) if right_max else node.val
            return True, left_min, right_max, max_bst_sum[-1]

        bst(root)

        return max(max_bst_sum)


if __name__ == "__main__":
    # tree = list_2_tree([1,4,3,2,4,2,5,None,None,None,None,None,None,4,6])
    tree = list_2_tree([1,None,10,-5,20])
    # tree = list_2_tree([4, 3, None, 1, 2])
    # tree = list_2_tree([5,4,8,3,None,6,3])
    print(Solution().maxSumBST(tree))
