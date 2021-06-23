# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-16 09:05'
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:

    def __init__(self, x=None):
        """ 链表节点

        :param x: 节点值
        """
        self.val = x
        self.next = None


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


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(0)

        while l1 or l2:

            if not l1 or not l2:
                tail.next = l1 or l2
                break

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        return head.next


if __name__ == "__main__":
    print(link_2_list(Solution().mergeTwoLists(list_2_link([1, 2, 4]), list_2_link([1, 3, 4, 5, 6]))))
