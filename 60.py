# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-23 11:00'
"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
"""


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        answer_inf = dict(cnt=0, answer=[])

        def back_track(rank, combine):
            rank_len = len(rank)

            for idx, num in enumerate(rank):
                if answer_inf["cnt"] == k:
                    return

                if rank_len == 1:
                    answer_inf["cnt"] += 1
                    if answer_inf["cnt"] == k:
                        answer_inf["answer"] = [*combine] + [num]
                        return
                    continue

                back_track(rank[0: idx] + rank[idx + 1:], [*combine] + [num])

        back_track([i for i in range(1, n + 1)], [])

        return "".join([str(obj) for obj in answer_inf["answer"]])


if __name__ == "__main__":
    import time
    start_time = time.time()
    print(Solution().getPermutation(9, 296662))
    print(time.time() - start_time)
