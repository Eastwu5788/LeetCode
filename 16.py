# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-24 09:11'
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, nums_cnt, ans_sum = sorted(nums), len(nums), None

        for idx in range(0, nums_cnt - 2):
            start, end = idx + 1, nums_cnt - 1
            while start < end:
                cur_sum = nums[idx] + nums[start] + nums[end]

                # 当前和与target相等，直接返回结果
                if cur_sum == target:
                    return cur_sum

                # 记录当前情况的最优解
                if ans_sum is None or abs(ans_sum - target) > abs(cur_sum - target):
                    ans_sum = cur_sum

                if cur_sum < target:
                    start += 1
                else:
                    end -= 1

        return ans_sum


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1,2,1,-4], 1))
