# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-07-23 10:57'
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start_idx, end_idx, cur_idx = 0, len(nums) - 1, 0

        while end_idx >= cur_idx:
            val = nums[cur_idx]

            if val == 0:
                nums[start_idx], nums[cur_idx] = nums[cur_idx], nums[start_idx]
                start_idx += 1
                cur_idx += 1
            elif val == 2:
                nums[end_idx], nums[cur_idx] = nums[cur_idx], nums[end_idx]
                end_idx -= 1

            elif val == 1:
                cur_idx += 1


if __name__ == "__main__":
    nums = [2, 1]
    Solution().sortColors(nums)
    print(nums)
