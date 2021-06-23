# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-07-24 09:34'
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        n_s = [idx for idx in range(1, n + 1)]

        def sub_combine(sub_s, sub_k):
            """ 生成基于子数组的N个组合

            :param sub_s: 子数组
            :param sub_k: 元素个数
            """
            if sub_k == 1:
                return [[val] for val in sub_s]

            combine = list()

            for s_idx in range(0, len(sub_s) - sub_k + 1):
                cmb = sub_combine(sub_s[s_idx + 1:], sub_k - 1)
                for sub_comb in cmb:
                    sub_comb.insert(0, sub_s[s_idx])
                combine.extend(cmb)
            return combine

        return sub_combine(n_s, k)


if __name__ == "__main__":
    print(Solution().combine(4, 2))
