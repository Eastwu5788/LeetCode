# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-24 11:14'
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
"""


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = [0] * n

        for idx in range(0, n):
            if idx == 0:
                answer[idx] = 1
            elif idx == 1:
                answer[idx] = 2

            else:
                answer[idx] = answer[idx - 1] + answer[idx - 2]

        return answer[-1]


if __name__ == "__main__":
    print(Solution().climbStairs(3))
