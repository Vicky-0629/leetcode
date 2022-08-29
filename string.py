#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2021/10/26 20:05

class String(object):

    # 反转字符串
    def reverseString(self, s):
        """
        编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

        不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

        你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverseWords(self, s):
        """
        给你一个字符串 s ，逐个翻转字符串中的所有 单词 。

        单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

        请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

        说明：

         输入字符串 s 可以在前面、后面或者单词间包含多余的空格。

         翻转后单词间应当仅用一个空格分隔。

         翻转后的字符串中不应包含额外的空格
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        left, right = 0, len(s_list) - 1
        while right > 0:
            if s_list[left] == " ":
                left += 1
            elif s_list[right] == " ":
                right -= 1
            else:




if __name__ == '__main__':
    string = String()

    # 反转字符串
    s = ["h", "e", "l", "l", "o"]
    res = string.reverseString(s)
    print(res)