# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-11 09:54'

"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""


class Solution:

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 去除左右空格
        str = str.lstrip().rstrip()
        if not str:
            return 0

        negative = False
        ans = 0
        int_max = 2 ** 31 - 1
        for idx, char in enumerate(list(str)):
            if idx == 0 and char in ["-", "+"]:
                negative = char == "-"
                continue

            if not char.isdigit():
                return -ans if negative else ans

            ans = ans * 10 + int(char)
            if ans > int_max:
                return -int_max - 1 if negative else int_max

        return -ans if negative else ans


if __name__ == "__main__":
    print(Solution().myAtoi("3.14159"))
