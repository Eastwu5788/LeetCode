# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-22 13:15'
"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        answer = list()

        for idx in range(0, len(intervals)):
            item = intervals[idx]
            last_item = answer[-1] if answer else None

            if not last_item or item[0] > last_item[1]:
                answer.append(item)

            elif item[1] >= last_item[1]:
                last_item[1] = item[1]

        return answer


if __name__ == "__main__":
    print(Solution().merge([[1,4],[4,5]]))
