# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-12 10:34'
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head, tail, max_area = 0, len(height) - 1, 0

        while head < tail:
            # 计算最低的高度 （使用min比较耗时）
            h = height[head] if height[head] < height[tail] else height[tail]
            # 计算当前面积
            area = h * (tail - head)
            # 计算最大面积
            max_area = area if area > max_area else max_area

            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1

        return max_area


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
