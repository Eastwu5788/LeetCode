# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-07-24 10:11'
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = list()

        def backtrace(sub_s, combine, size):
            """ 回溯查找包含N个元素的组合
            """
            if size == 0:
                output.append(combine[:])
                return

            for idx, val in enumerate(sub_s):
                combine.append(val)
                backtrace(sub_s[idx + 1:], combine, size - 1)
                combine.pop()

        for size in range(0, len(nums) + 1):
            if size == 0:
                output.append([])
                continue

            if size == len(nums):
                output.append(nums[:])
                continue

            backtrace(nums, [], size)

        return output


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
