# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-15 18:19'


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        op_stack = []

        op_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in op_map.values():
                op_stack.append(c)
            else:
                if len(op_stack) == 0:
                    return False
                elif op_stack[-1] != op_map.get(c):
                    return False
                else:
                    op_stack.pop(-1)

        return not op_stack


if __name__ == "__main__":
    print(Solution().isValid("["))
