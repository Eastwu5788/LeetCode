# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-19 17:03'
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
"""


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answer = list()

        def n_queen(depth, row, combine):
            if depth == n:
                answer.append(combine)
                return

            for col in range(0, n):
                # 当前列不符合
                if 1 in row[col]:
                    continue

                cur_row = "." * col + "Q" + "." * (n - col - 1)

                new_row = [[0] * 3 for _ in range(n)]
                for idx, val in enumerate(row):
                    if idx == col or val[1] == 1:
                        new_row[idx][1] = 1

                    if idx > 0 and (val[0] == 1 or idx == col):
                        new_row[idx - 1][0] = 1

                    if idx < n - 1 and (val[2] == 1 or idx == col):
                        new_row[idx + 1][2] = 1

                n_queen(depth + 1, new_row, combine + [cur_row])

        n_queen(0, [[0] * 3 for _ in range(n)], [])
        return answer


if __name__ == "__main__":
    print(Solution().solveNQueens(4))
