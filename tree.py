# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2021
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '7/20/21 10:13 AM'


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


if __name__ == "__main__":
    # tree = list_2_tree([1,4,3,2,4,2,5,None,None,None,None,None,None,4,6])
    tree = list_2_tree([1,None,10,-5,20])
    print(tree)
