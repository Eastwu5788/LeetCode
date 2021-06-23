# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-22 10:35'
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
"""


class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        row_cnt, col_cnt = len(matrix), len(matrix[0])
        cur_row, cur_col = 0, 0
        direct_idx = depth = 0

        answer = list()

        while len(answer) < row_cnt * col_cnt:

            direct = direction[direct_idx % 4]

            if direct[0] == 0:
                rng = range(depth, col_cnt - depth) if direct[1] == 1 else range(col_cnt - depth, depth)
                for col in rng:

                    answer.append(matrix[cur_row][cur_col])
                    cur_row += direct[0]
                    cur_col += direct[1]

            else:

                for row in range()


