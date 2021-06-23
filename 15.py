# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-15 16:39'


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n_len = len(nums)

        # 不足三个的情况
        if n_len < 3:
            return []

        # 刚好数据为3个的情况
        if n_len == 3:
            return [nums] if sum(nums) == 0 else []

        ans, nums, idx = list(), sorted(nums), 0

        while idx < n_len - 1:
            left, right = idx - 1, idx + 1

            while left >= 0 and right < n_len:
                sum_idx = nums[left] + nums[idx] + nums[right]

                if sum_idx == 0:
                    ans.append([nums[left], nums[idx], nums[right]])

                    while left - 1 > 0 and nums[left - 1] == nums[left]:
                        left -= 1

                    while right + 1 < n_len and nums[right + 1] == nums[right]:
                        right += 1

                    left -= 1
                    right += 1

                elif sum_idx > 0:
                    left -= 1

                else:
                    right += 1

            while idx + 1 < n_len - 1 and nums[idx + 1] == nums[idx]:
                idx += 1
            idx += 1
            print(idx)
        return ans


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
