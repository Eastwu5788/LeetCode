# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-07-29 13:27'
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
"""


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        def binary_search(array, tg):
            start, end = 0, len(array) - 1

            while start <= end:
                mid = (start + end) // 2

                if array[mid] == tg:
                    return True

                if array[mid] < tg:
                    start = mid + 1
                else:
                    end = mid - 1

            return False

        for idx in range(0, len(nums)):
            if nums[idx] == target:
                return True

            if idx + 1 < len(nums) and nums[idx] > nums[idx + 1]:
                if target < nums[idx + 1]:
                    return False

                if target > nums[-1]:
                    return False

                return binary_search(nums[idx + 1:], target)

        return False


if __name__ == "__main__":
    nums = [3, 1]
    print(Solution().search(nums, 1))
