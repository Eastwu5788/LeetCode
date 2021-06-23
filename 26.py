# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-16 13:17'
"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, width, nums_len = 1, 0, len(nums)

        if nums_len < 2:
            return nums_len

        while idx < nums_len:

            if nums[idx - 1] == nums[idx]:
                width += 1
            elif width > 0:
                nums[idx - width] = nums[idx]
            idx += 1

        return nums_len - width


if __name__ == "__main__":
    ns = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(ns))
    print(ns)