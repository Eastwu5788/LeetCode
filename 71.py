# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-24 11:25'
"""
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

 

示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。

示例 5：

输入："/a/../../b/../c//.//"
输出："/c"
"""


class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        def find_node(pth):
            """ 发现一层文件节点

            :param pth: 文件路径
            """
            if not pth:
                return "", ""

            split_idx = 0
            for idx in range(0, len(pth)):
                split_idx = idx
                if pth[idx] == "/":
                    break

            return pth[:split_idx + 1], pth[split_idx + 1:]

        result, path = ["/"], path[1:] if path.startswith("/") else path
        while True:
            node, path = find_node(path)
            if not node:
                break

            if node in ["/", "./", "."]:
                continue
            elif node in ["../", ".."]:
                result = result[:-1] if len(result) > 1 else ["/"]
            else:
                result.append(node)

        # 去除结尾 /
        if len(result) > 1 and result[-1].endswith("/"):
            result[-1] = result[-1][:-1]

        return "".join(result)


if __name__ == "__main__":
    print(Solution().simplifyPath("/a//b////c/d//././/.."))
