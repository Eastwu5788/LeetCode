# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-19 13:10'
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = list()

        def back_track(sub_nums, combine):
            sub_nums_len = len(sub_nums)
            used_nums = []
            for idx, num in enumerate(sub_nums):

                # 仅有一组数据时，说明已经到达叶子节点
                if sub_nums_len <= 1:
                    answer.append(combine + [num])
                    return

                # 去除层上的重复节点
                if num in used_nums:
                    continue
                used_nums.append(num)

                new_sub_nums = [*sub_nums]
                new_sub_nums.pop(idx)
                back_track(new_sub_nums, combine + [num])

        back_track(nums, [])

        return answer


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
