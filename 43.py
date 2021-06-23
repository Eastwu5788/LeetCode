# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-18 17:12'
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
"""


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        a_ident, answer = 0, list()

        for i, val1 in enumerate(num2[::-1]):
            # 整型值和进位值
            val1, ident = int(val1), 0

            for j, val2 in enumerate(num1[::-1]):
                val = val1 * int(val2) + ident
                ident = val // 10
                val = val % 10

                if i + j >= len(answer):
                    val += a_ident
                    a_ident = val // 10
                    answer.append(val % 10)

                else:
                    val = answer[i + j] + val + a_ident
                    a_ident = val // 10
                    answer[i + j] = val % 10

            if ident > 0:
                answer.append(ident)

        if a_ident > 0:
            if len(answer) == len(num1) + len(num2):
                answer[-1] += a_ident
            else:
                answer.append(a_ident)

        return "".join([str(i) for i in answer[::-1]])


if __name__ == "__main__":
    print(Solution().multiply("999", "999"))

