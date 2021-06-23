# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-22 15:40'
"""
给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。

由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。

返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。

 

示例 1：

输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：文件系统将会这样创建文件名：
"pes" --> 之前未分配，仍为 "pes"
"fifa" --> 之前未分配，仍为 "fifa"
"gta" --> 之前未分配，仍为 "gta"
"pes(2019)" --> 之前未分配，仍为 "pes(2019)"
"""


class Solution(object):

    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        answer, cache_map = list(), dict()

        def find_name_ext(f_name):
            for end, char in enumerate(f_name[::-1]):
                cur_index = len(f_name) - end - 1
                if end == 0 and char != ")":
                    return f_name, 0

                if char == "(":
                    return f_name[0: cur_index], int(f_name[cur_index + 1: len(f_name) - 1])

        for name in names:
            fmt_name, idx = find_name_ext(name)
            name_idx_ls = cache_map.get(name, list())

            new_idx = max(name_idx_ls) + 1 if idx in name_idx_ls else 0
            if new_idx:
                name += "(%d)" % (max(name_idx_ls) + 1)

            answer.append(name)
            cache_map.setdefault(name, list()).append(new_idx)

            if name != fmt_name:
                cache_map.setdefault(fmt_name, list()).append(idx)

        return answer


if __name__ == "__main__":
    # print(Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))
    # print(Solution().getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
    # print(Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]))
    print(Solution().getFolderNames(["wano","wano","wano","wano"]))
