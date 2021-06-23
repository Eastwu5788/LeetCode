# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-23 16:47'
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
"""


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        answer = [[0] * n for _ in range(m)]

        for row in range(0, m):
            for col in range(0, n):
                if row == 0 or col == 0:
                    answer[row][col] = 1
                else:
                    answer[row][col] = answer[row - 1][col] + answer[row][col - 1]

        return answer[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(7, 3))
