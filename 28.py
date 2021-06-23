# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-16 14:03'

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
"""


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        m, n = len(haystack), len(needle)
        left = width = 0

        while left <= m - n:

            if haystack[left + width] != needle[width]:
                left += 1
                width = 0
                continue

            if width == n - 1:
                return left
            width += 1

        return -1


if __name__ == "__main__":
    print(Solution().strStr("mississippi", "issip"))
