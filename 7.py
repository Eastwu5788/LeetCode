# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-10 11:24'
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rst, is_res = 0, x < 0
        x = abs(x)

        while x != 0:
            rst = rst * 10 + x % 10
            x = x // 10

        if rst > 0x7fffffff:
            return 0

        return -rst if is_res else rst


if __name__ == "__main__":
    print(Solution().reverse(123))
