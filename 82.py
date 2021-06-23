# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-07-29 14:09'
"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
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

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        new_head = ListNode(None)
        new_tail = new_head

        left, right = head, head.next
        if not right:
            return left

        while right:
            if left.val == right.val:
                right = right.next
                continue

            if left.next == right:
                new_tail.next = left
                new_tail = new_tail.next
                new_tail.next = None

            left = right
            right = right.next
            # 处理最后一个
            if not right:
                new_tail.next = left

        return new_head.next


if __name__ == "__main__":
    link = [1, 2, 3, 3, 4, 4, 5]
    # link = [1, 2, 2]
    print(link_2_list(Solution().deleteDuplicates(list_2_link(link))))
