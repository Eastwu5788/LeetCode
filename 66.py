# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-24 10:08'
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, digits_cnt = 0, len(digits)

        for idx in range(digits_cnt - 1, -1, -1):
            num = digits[idx] + carry

            if idx == digits_cnt - 1:
                num += 1

            carry = num // 10
            num = num % 10
            digits[idx] = num

        if carry:
            digits.insert(0, carry)

        return digits


if __name__ == "__main__":
    print(Solution().plusOne([9, 9, 9, 9]))
