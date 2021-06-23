# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-22 13:32'
"""
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
"""


class Solution(object):

    def patternMatching(self, pattern, value):
        """
        :type pattern: str
        :type value: str
        :rtype: bool
        """
        pattern_len, value_len, a_num = len(pattern), len(value), pattern.count("a")
        b_num = pattern_len - a_num

        if a_num < b_num:
            a_num, b_num = b_num, a_num
            pattern = ["a" if char == "b" else "b" for char in pattern]

        if pattern_len == 0:
            return value_len == 0

        if value_len == 0:
            if a_num == 0 or b_num == 0:
                return True
            return False

        for a_len in range(0, value_len // a_num + 1):
            b_str_len = value_len - a_len * a_num
            if b_num > 0 and b_str_len % b_num != 0:
                continue

            b_len = b_str_len // b_num if b_num > 0 else 0

            new_char, comb_char = "", {"a": "", "b": ""}
            for char in pattern:
                start_idx = len(new_char)
                sub_char = value[start_idx: start_idx + (a_len if char == "a" else b_len)]

                # 字符无法对应
                if comb_char[char] and comb_char[char] != sub_char:
                    break

                new_char += sub_char
                comb_char[char] = sub_char

            if new_char == value:
                return True

        return False


if __name__ == "__main__":
    print(Solution().patternMatching("ab", ""))  # False
    # print(Solution().patternMatching("", "x"))
    # print(Solution().patternMatching("bbbb", "dogcatcatdog"))
    # print(Solution().patternMatching("abba", "dogdogdogdog"))
    print(Solution().patternMatching("aaaaab", "xahnxdxyaahnxdxyaahnxdxyaahnxdxyaauxuhuo"))  # True
