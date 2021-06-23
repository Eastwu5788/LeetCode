# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-08 09:07'
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


class ListNode:

    def __init__(self, x=None):
        """ 链表节点

        :param x: 节点值
        """
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """ LeetCode-2: 两数相加
        """
        head = cursor = ListNode()
        carry = 0

        while True:
            val = carry + getattr(l1, "val", 0) + getattr(l2, "val", 0)
            carry, cursor.val = val // 10, val % 10

            l1, l2 = getattr(l1, "next", None), getattr(l2, "next", None)
            if not l1 and not l2 and carry == 0:
                return head

            cursor.next = ListNode()
            cursor = cursor.next


def list_2_link(ls):
    """ 数组转换成链表

    :param ls: 数组
    """
    linked = node = ListNode()

    for idx, val in enumerate(ls):
        node.val = val

        if idx < len(ls) - 1:
            node.next = ListNode()
            node = node.next

    return linked


def link_2_list(lk):
    """ 链表转换成数组
    """
    ls = list()

    while lk:
        ls.append(lk.val)
        lk = lk.next

    return ls


if __name__ == "__main__":
    i1 = list_2_link([2, 4, 3, 5])
    i2 = list_2_link([5, 6, 4])
    rst = Solution().addTwoNumbers(i1, i2)
    print(link_2_list(rst))
