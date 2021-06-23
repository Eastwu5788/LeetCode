# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-24 10:42'
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x // 2 + 1

        while left < right:
            mid = (right + left + 1) // 2

            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    print(Solution().mySqrt(9))
