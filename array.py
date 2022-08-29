#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2021/10/16 17:05

class Array(object):

    # 二分查找
    def search(self, nums, target):
        """
        给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，

        如果目标值存在返回下标，否则返回 -1。
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            medium = left + (right - left) // 2
            if nums[medium] == target:
                return medium
            elif nums[medium] > target:
                right = medium
            elif nums[medium] < target:
                left = medium + 1
        return -1

    # x 的平方根
    def mySqrt(self, x):
        """
        给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

        由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

        注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left, right = 0, x
        while right - left > 1:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid
        return left

    # 有序数组的平方
    def sortedSquares(self, nums):
        """
        给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [0] * len(nums)
        left, right = 0, len(nums) - 1
        index = len(nums) - 1
        while left <= right:
            lr = nums[left] * nums[left]
            rr = nums[right] * nums[right]
            if lr < rr:
                dp[index] = rr
                right -= 1
            else:
                dp[index] = lr
                left += 1
            index -= 1
        return dp

    # 长度最小的子数组
    def minSubArrayLen(self, target, nums):
        """
        给定一个含有 n 个正整数的数组和一个正整数 target 。

        找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。

        如果不存在符合条件的子数组，返回 0
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        length = float("inf")
        tmp = float("inf")
        while right <= len(nums):
            if sum(nums[left: right + 1]) >= target:
                tmp = right - left + 1
                left += 1
            else:
                right += 1
            length = min(length, tmp)
        return 0 if length == float("inf") else length


if __name__ == '__main__':
    array = Array()
    # 二分查找
    nums, target = [-4, -1, 0, 3, 10], 2
    res = array.search(nums, target)
    print(res)

    # x 的平方根
    x = 88
    res = array.mySqrt(x)
    print(res)

    # 有序数组的平方
    res = array.sortedSquares(nums)
    print(res)

    # 长度最小的子数组
    nums, target = [2, 3, 1, 2, 4, 7], 7
    res = array.minSubArrayLen(target, nums)
    print(res)