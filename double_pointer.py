#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2022/1/26 20:15


class Double_Pointer(object):
    """
    双指针
    """
    # 167 两数之和Ⅱ
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, self.found_target(numbers, target)
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return l + 1, r + 1
            if sum > target:
                l = 0
                r -= 1
            if sum < target:
                l += 1

    def found_target(self, numbers, target):
        n = len(numbers)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] == target:
                return mid - 1
            elif numbers[mid] > target:
                r -= 1
            elif numbers[mid] < target:
                l += 1
        if l > target:
            return l - 1
        elif r < target:
            return r if r == n - 1 else r + 1
        else:
            return r - 1

    # 557 反转字符串中的单词III
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        l, r = 0, 1
        while r < n:
            if s[r] == " ":
                s[l: r] = self.reverse(s[l: r])
                l = r + 1
                r = l + 1
            else:
                r += 1
        s = "".join(s)
        return s

    def reverse(self, s):
        n = len(s)
        if n == 1:
            return s
        l, r = 0, n - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s


if __name__ == '__main__':
    double_pointer = Double_Pointer()

    # 167 两数之和Ⅱ
    # numbers = [-1, 0]
    # terget = -1
    # res = double_pointer.twoSum(numbers, terget)
    # print(res)

    # 557 反转字符串中的单词III
    s = "Let's take LeetCode contest"
    res = double_pointer.reverseWords(s)
    print(res)
