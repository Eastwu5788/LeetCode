# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-16 10:23'


class Solution(object):

    letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = list()
        if not digits:
            return ans

        # 回溯法
        def backtrack(cs, char):
            if not cs:
                ans.append(char)
                return

            for c in self.letter_map[cs[0]]:
                backtrack(cs[1:], char + c)

        backtrack(list(digits), "")
        return ans


if __name__ == "__main__":
    print(Solution().letterCombinations(""))
