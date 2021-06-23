# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-22 15:22'

"""
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

 

示例 1：

输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。
"""


class Solution(object):

    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        answer = start

        for idx in range(1, n):
            value = start + idx * 2
            answer ^= value

        return answer


if __name__ == "__main__":
    print(Solution().xorOperation(1, 7))
