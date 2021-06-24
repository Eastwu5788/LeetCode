# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2021
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '6/23/21 5:14 PM'


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
