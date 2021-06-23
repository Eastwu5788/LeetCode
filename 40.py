# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-18 09:06'
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        size, candidates = len(candidates), sorted(candidates)

        def back_track(idx, tg, combine):
            """ 回溯算法

            :param tg: 当前节点的目标值
            :param combine: 当前的组合
            """
            # 当前分支没有可行解
            if idx >= size or tg < candidates[idx]:
                return

            for i, val in enumerate(candidates[idx:]):
                # 只保留递增序列
                if combine and val < combine[-1]:
                    continue

                # 剔除掉同一层重复元素, 此时的索引应该是 idx + i - 1
                if i > 0 and candidates[idx + i - 1] == val:
                    continue

                # 找到可行解
                if val == tg:
                    answer.append(combine + [val])
                    return

                # 剪枝，去除重复的结果
                combine.append(val)
                # 下一层的索引应该从 idx + i + 1 开始
                back_track(idx + i + 1, tg - val, combine)
                combine.pop()

        back_track(0, target, [])
        return answer


if __name__ == "__main__":
    print(Solution().combinationSum2([1, 2], 4))
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
    print(Solution().combinationSum2([2,5,2,1,2], 5))
