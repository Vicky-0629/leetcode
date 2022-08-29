#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2021/10/25 14:37

class Hash(object):

    # 有效的字母异位词
    def isAnagram(self, s, t):
        """
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

        注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
        :type s: str
        :type t: str
        :rtype: bool
        """



    # 快乐数
    def isHappy(self, n):
        """
        编写一个算法来判断一个数 n 是不是快乐数。

        「快乐数」定义为：

        对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。

        然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。

        如果 可以变为  1，那么这个数就是快乐数。

        如果 n 是快乐数就返回 true ；不是，则返回 false 。
        :type n: int
        :rtype: bool
        """
        def calculate_happy(num):
            sum = 0
            while num > 0:
                sum += (num % 10) ** 2
                num = num // 10
            return sum

        record = []
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            elif n in record:
                return False
            else:
                record.append(n)














if __name__ == '__main__':
    hash = Hash()

    # 有效的字母异位词
    s = "anagram"
    t = "nagaram"

    n =19
    res = hash.isHappy(19)
    print(res)