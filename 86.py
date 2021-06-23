# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-08-27 10:25'
"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def link_2_list(lk):
    """ 链表转换成数组
    """
    ls = list()

    while lk:
        ls.append(lk.val)
        lk = lk.next

    return ls


def list_2_link(ls):
    """ 数组转换成链表

    :param ls: 数组
    """
    linked = node = ListNode(None)

    for idx, val in enumerate(ls):
        node.val = val

        if idx < len(ls) - 1:
            node.next = ListNode(None)
            node = node.next

    return linked


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_head, right_head = ListNode(None), ListNode(None)
        left, right = left_head, right_head

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        left.next = right_head.next
        right.next = None
        return left_head.next


if __name__ == "__main__":
    link = [1, 4, 3, 2, 5, 2]
    # link = [1, 2, 2]
    print(link_2_list(Solution().partition(list_2_link(link), 3)))
