# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2019-10-25 17:35'
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:

    def two_sum(self, nums, target):

        hash_map = dict()

        for idx, item in enumerate(nums):

            target_index = hash_map.get(target - item)

            if target_index is None:
                hash_map[item] = idx
                continue

            return [target_index, idx]


if __name__ == "__main__":
    print(Solution().two_sum([2, 7, 11, 15], 9))
