# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-07-29 09:28'
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
"""


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row_len, col_len = len(board), len(board[0])

        def traceback(cmb, sub_word):
            if not sub_word:
                return True

            cur_row, cur_col = cmb[-1][0], cmb[-1][1]

            def check_pos(row, col):
                if (row, col) in cmb:
                    return False

                if board[row][col] != sub_word[0]:
                    return False

                # 查找结束
                if len(sub_word) == 1:
                    return True

                return traceback(cmb + [(row, col)], sub_word[1:])

            if cur_col > 0:
                next_col = cur_col - 1
                if check_pos(cur_row, next_col):
                    return True

            if cur_col < col_len - 1:
                next_col = cur_col + 1
                if check_pos(cur_row, next_col):
                    return True

            if cur_row > 0:
                next_row = cur_row - 1
                if check_pos(next_row, cur_col):
                    return True

            if cur_row < row_len - 1:
                next_row = cur_row + 1
                if check_pos(next_row, cur_col):
                    return True

            return False

        for row in range(0, row_len):
            for col in range(0, col_len):
                b_char = board[row][col]
                if b_char != word[0]:
                    continue
                combine = [
                    (row, col)
                ]
                if traceback(combine, word[1:]):
                    return True

        return False


if __name__ == "__main__":
    # board = [
    #     ["A", "B", "C", "E"],
    #     ["S", "F", "C", "S"],
    #     ["A", "D", "E", "E"]
    # ]
    board = [
        ["a"]
    ]
    print(Solution().exist(board, "a"))
