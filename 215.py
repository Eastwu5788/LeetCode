# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-29 11:21'
"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_len = len(nums)

        def build_tree(start, end):
            """ 从数组的起始位置和结束位置，构建符合大根堆的树
            """
            if start > end:
                return

            left = 2 * start + 1
            right = 2 * start + 2

            large_idx = start

            if left <= end and nums[large_idx] < nums[left]:
                large_idx = left

            if right <= end and nums[large_idx] < nums[right]:
                large_idx = right

            if large_idx != start:
                nums[start], nums[large_idx] = nums[large_idx], nums[start]
                build_tree(large_idx, end)

        last_node = (nums_len - 1 - nums_len % 2) // 2
        for idx in range(last_node, -1, -1):
            build_tree(idx, nums_len - 1)

        for idx in range(0, k):
            nums[0], nums[nums_len - idx - 1] = nums[nums_len - idx - 1], nums[0]
            build_tree(0, nums_len - idx - 2)

        return nums[nums_len - k]


if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))
