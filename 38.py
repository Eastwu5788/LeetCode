# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-17 14:31'

"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
"""


class Solution(object):


    def trans_int(self, n):
        ans, sub_char = "", list()

        for c in str(n):
            if not sub_char or sub_char[-1] == c:
                sub_char.append(c)
                continue

            ans += str(len(sub_char)) + str(sub_char[-1])
            sub_char = list()
            sub_char.append(c)

        ans += str(len(sub_char)) + str(sub_char[-1])
        return ans


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = 1
        for idx in range(1, n):
            ans = self.trans_int(ans)
        return str(ans)

if __name__ == "__main__":
    print(Solution().countAndSay(1))
