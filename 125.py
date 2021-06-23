# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-19 16:16'
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1

        while start < end:
            start_char = s[start]
            if not start_char.isalnum():
                start += 1
                continue

            end_char = s[end]
            if not end_char.isalnum():
                end -= 1
                continue

            if start_char.lower() != end_char.lower():
                return False

            start += 1
            end -= 1

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("1A man, a plan, a canal: Panama2"))
