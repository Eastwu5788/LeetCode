# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-19 16:28'
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow(x, sub_n):
            if sub_n == 0:
                return 1

            if sub_n == 1:
                return x

            if sub_n == 2:
                return x * x

            val = pow(x, sub_n // 2)
            return val * val if sub_n % 2 == 0 else val * val * x

        rst = pow(x, abs(n))
        return rst if n > 0 else 1 / rst


if __name__ == "__main__":
    print(Solution().myPow(-2, -3))
