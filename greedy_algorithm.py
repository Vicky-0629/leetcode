#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2021/10/13 19:45

class GreedyAlgrithm(object):
    """
    贪心算法
    """
    def __init__(self):
        super(GreedyAlgrithm, self).__init__()

    # 跳跃游戏Ⅱ
    def jump_game(self, nums):
        """
        给定一个非负整数数组，你最初位于数组的第一个位置。

        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        你的目标是使用最少的跳跃次数到达数组的最后一个位置。

        思路：每次决定跳跃次数是否加1的时候都要等到遍历完当前最大的覆盖范围
        :param nums: 非负整数数组
        :return:
        """
        start = 0
        step = 0
        cover = 0
        next_cover = 0
        while cover < len(nums) - 1:
            next_cover = max(next_cover, start + nums[start])
            if cover == start:
                step += 1
                cover = next_cover
                if cover >= len(nums) - 1:
                    break
            start += 1
        return step

    # 分发饼干
    def distribution_cookies(self, g, s):
        """
        假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

        对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。

        如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，

        并输出这个最大数值
        :param g: 孩子胃口值
        :param s: 饼干尺寸
        :return:
        """
        g = sorted(g)
        s = sorted(s)
        num = 0
        for i in s:
            if i >= g[num]:
                num += 1
                if num > len(g) - 1:
                    break
        return num

    # 摆动序列
    def wiggle_sequence(self, nums):
        """
        如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。

        第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

        给你一个整数数组 nums ，返回 nums 中作为 摆动序列的最长子序列的长度 。
        :param nums:
        :return:
        """

    # 最大子序和
    def max_sub_sequence(self, nums):
        """
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        :param nums: 整数数组
        :return:
        """
        res = -float("inf")
        count = 0
        for i in nums:
            count += i
            res = max(res, count)
            if count < 0:
                count = 0
        return res


if __name__ == '__main__':
    greedy_algorithm = GreedyAlgrithm()
    # # 跳跃游戏Ⅱ
    # nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    # step = greedy_algorithm.jump_game(nums)
    # print(step)

    # # 分发饼干
    # g = [1, 2]
    # s = [1, 2, 3]
    # num = greedy_algorithm.distribution_cookies(g, s)
    # print(num)
    # 摆动序列

    # 最大子序和
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_num = greedy_algorithm.max_sub_sequence(nums)
    print(max_num)


