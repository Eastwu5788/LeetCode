# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-09 16:15'
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0

        for cursor in range(len(s)):
            high = low = cursor

            for idx in range(low + 1, len(s)):
                if s[low] != s[idx]:
                    break
                high = idx

            while low > 0 and high < len(s) - 1 and s[low - 1] == s[high + 1]:
                low -= 1
                high += 1

            if high - low >= end - start:
                start, end = low, high

        return s[start: end + 1]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))