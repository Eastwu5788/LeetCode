# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-18 11:04'
"""
我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。

输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    cur_idx = 0

    def recoverFromPreorder(self, S: str) -> TreeNode:

        def get_number(idx):
            w = 0
            while idx < len(S) and S[idx].isdigit():
                w += 1
                idx += 1
            return w

        self.cur_idx = 0

        def recover_tree(depth):
            # 层级不匹配
            sep_char = "-" * depth
            if not S[self.cur_idx:].startswith(sep_char):
                return None

            # 更新游标位置
            self.cur_idx += len(sep_char)

            # 计算出数字，及移动游标到新的位置
            w = get_number(self.cur_idx)
            val = S[self.cur_idx: self.cur_idx + w]
            self.cur_idx += w

            # 生成当前节点
            node = TreeNode(val)
            node.left = recover_tree(depth + 1)
            node.right = recover_tree(depth + 1)
            return node

        return recover_tree(0)


if __name__ == "__main__":
    rs = Solution().recoverFromPreorder("1-2--3---4-5--6---7")
    print(rs)

