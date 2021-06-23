# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-17 10:10'
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        input_len = len(nums)
        if input_len <= 1:
            return

        i = j = input_len - 1

        # 找到第一个 num[i] < num[j] 位置
        for idx in range(input_len - 1, 0, -1):
            if nums[idx - 1] < nums[idx]:
                i = idx - 1
                j = idx
                break

        # 从后往前查找第一个 num[k] > num[i], 互换位置
        for idx in range(input_len - 1, j - 1, -1):
            if nums[idx] > nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        # 如果 i == j 说明没有找到递减序列，需要整体翻转
        if j == i:
            j = 0

        # 将 num[j] 到 end 的数据翻转
        for idx in range(j, input_len):
            r_idx = input_len - (idx - j) - 1
            if idx < r_idx:
                nums[idx], nums[r_idx] = nums[r_idx], nums[idx]


if __name__ == "__main__":
    ns = [1, 2, 3]
    Solution().nextPermutation(ns)
    print(ns)
