# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-19 10:36'
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = list()

        def back_track(sub_nums, combine):
            sub_nums_len = len(sub_nums)
            for idx, num in enumerate(sub_nums):

                # 仅有一组数据时，说明已经到达叶子节点
                if sub_nums_len <= 1:
                    answer.append(combine + [num])
                    return

                new_sub_nums = [*sub_nums]
                new_sub_nums.pop(idx)
                back_track(new_sub_nums, combine + [num])

        back_track(nums, [])

        return answer


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
