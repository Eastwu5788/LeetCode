# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-23 09:51'
"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
"""


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idx_a, idx_b, ident = len(a) - 1, len(b) - 1, 0
        answer = list()

        while idx_a >= 0 or idx_b >= 0:
            val = ident

            if idx_a >= 0:
                val += int(a[idx_a])
                idx_a -= 1

            if idx_b >= 0:
                val += int(b[idx_b])
                idx_b -= 1

            ident = val // 2
            val = val % 2

            answer.append(val)

        if ident > 0:
            answer.append(ident)

        return "".join([str(val) for val in answer[::-1]])


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("1010", "1011"))
