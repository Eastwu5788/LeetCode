# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-16 09:19'


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """



if __name__ == "__main__":
    print(Solution().generateParenthesis(n=4))
    ans = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    my = ['((())()())()', '(()())(())', '((()))()()', '((()))(())', '(())((()))()', '(())(()())()', '(((()))())()', '(()())()()', '((())(()))()', '((()())())()', '(())(())(())', '(())(())()()']
    # print(set(ans) - set(my))
    # print(set(my) - set(ans))
