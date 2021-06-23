# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-23 17:16'

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
"""


class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[-1])
        answer = [[0] * n for _ in range(m)]

        for row in range(0, m):
            for col in range(0, n):
                if obstacleGrid[row][col] == 1:
                    answer[row][col] = 0
                    continue

                if row == 0 or col == 0:
                    if row == 0 and col == 0:
                        answer[row][col] = 1
                    elif row == 0:
                        answer[row][col] = answer[row][col - 1]
                    elif col == 0:
                        answer[row][col] = answer[row - 1][col]
                else:
                    answer[row][col] = answer[row - 1][col] + answer[row][col - 1]

        return answer[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([
        [1, 0],
    ]))
