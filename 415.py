# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-18 18:18'

"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        idx1, idx2, indent = len(num1) - 1, len(num2) - 1, 0
        answer = ""

        while idx1 >= 0 or idx2 >= 0:
            val = indent
            if idx1 >= 0:
                val += int(num1[idx1])

            if idx2 >= 0:
                val += int(num2[idx2])

            indent = val // 10
            answer = str(val % 10) + answer

            idx1, idx2 = idx1 - 1, idx2 - 1

        return str(indent) + answer if indent else answer


if __name__ == "__main__":
    print(Solution().addStrings("99", "99"))
    print(Solution().addStrings("999", "999"))
