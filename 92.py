# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2021
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '6/23/21 5:11 PM'
"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

"""
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    linked = node = ListNode()

    for idx, val in enumerate(ls):
        node.val = val

        if idx < len(ls) - 1:
            node.next = ListNode()
            node = node.next

    return linked



class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        new_head = ListNode()
        new_head.next = head

        left_idx = right_idx = new_head

        # 将左右指针移动到需要对换的
        for idx in range(right):
            right_idx = right_idx.next
            if idx < left - 1:
                left_idx = left_idx.next

        while left_idx.next != right_idx:
            tmp_node = left_idx.next
            left_idx.next = tmp_node.next

            tmp_node.next = right_idx.next
            right_idx.next = tmp_node

        return new_head.next


if __name__ == "__main__":
    head = list_2_link([1, 2])
    head = Solution().reverseBetween(head, 1, 2)
    print(link_2_list(head))
