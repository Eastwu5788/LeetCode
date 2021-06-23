# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-17 17:02'
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
"""

class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = list()

        candidates = sorted(candidates)

        def back_trace(sub_target, combine):
            """ 回溯法求解

            :param sub_target: 子目标值
            :param combine: 当前组合
            """
            # 当前组合没有可行解
            if sub_target < candidates[0]:
                return

            for num in candidates:

                if combine and num < combine[-1]:
                    continue

                if num == sub_target:
                    ans.append(combine + [num])
                    return

                combine.append(num)
                back_trace(sub_target - num, combine)
                combine.pop(-1)

        back_trace(target, [])

        return ans


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 5], 8))
