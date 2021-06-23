# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-23 15:45'

"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
"""


class ListNode:

    def __init__(self, x=None):
        """ 链表节点

        :param x: 节点值
        """
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
    linked = node = ListNode()

    for idx, val in enumerate(ls):
        node.val = val

        if idx < len(ls) - 1:
            node.next = ListNode()
            node = node.next

    return linked



class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        start = end = head

        if not head or not head.next:
            return head

        def get_link_len(link):
            link_len = 0
            while link:
                link_len += 1
                link = link.next
            return link_len

        head_len = get_link_len(head)
        k = k % head_len

        # 将节点右移，与head节点产生偏差
        for _ in range(0, k):
            end = end.next

        # 移动到尾部
        while end.next:
            start = start.next
            end = end.next

        end.next = head
        head = start.next
        start.next = None

        return head


if __name__ == "__main__":
    i1 = list_2_link([1, 2, 3])
    rst = Solution().rotateRight(i1, 2000000000)
    print(link_2_list(rst))
