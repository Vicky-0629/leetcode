# # ！/usr/bin/env python3
# # -*- coding:utf-8 -*-
# # Author: Vicky.chen
# # Time: 2021/9/3 14:43


class Dynamic_Programming(object):
    """
    动态规划
    """
    # 最大子序和
    def max_sub_sequence(self, nums):
        """
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        :param nums: 整数数组
        :return:
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        result = max(dp)
        return result

    # 实现斐波拉契数列
    def fib(self, n):
        """
        斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，

        后面的每一项数字都是前面两项数字的和。也就是： F(0) = 0，F(1) = 1 F(n) = F(n - 1) + F(n - 2)，

        其中 n > 1 给你n ，请计算 F(n) 。
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        if n >= 2:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # 爬楼梯
    def climbStairs(self, n):
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

        注意：给定 n 是一个正整数。
        :param n:
        :return:
        """
        dp = [1] * (n + 1)
        if n >= 2:
            dp[2] = 2
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]

    # 使用最小花费爬楼梯
    def minCostClimbingStairs(self, cost):
        """
        数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

        每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

        请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[len(cost) - 1], dp[len(cost) - 2])

    # 不同路径
    def uniquePaths(self, m, n):
        """
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

        问总共有多少条不同的路径？
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # 不同路径Ⅱ
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

        现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

        网格中的障碍物和空位置分别用 1 和 0 来表示。
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # 整数拆分
    def integerBreak(self, n):
        """
        给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                tmp = max(j * (i - j), j * dp[i - j])
                dp[i] = max(dp[i], tmp)
        return dp[-1]





#  实现斐波拉契数列
# class Fibonacci(object):
#     def __init__(self):
#         pass
#
#     def recursion(self, n):
#         if n <= 1:
#             return n
#         return self.recursion(n-1) + self.recursion(n-2)
#
#     def memorandum(self, n):
#         memo = []
#         for i in range(n+1):
#             res = self.fib(i, memo)
#             memo.append(res)
#         return memo[n]
#
#     @staticmethod
#     def fib(n, memo):
#         if n <= 1:
#             return n
#         return memo[n-1] + memo[n-2]
#
#     def dynamic_programming(self, n):
#         memo = list(range(n+1))
#         for i in range(n+1):
#             if i <= 1:
#                 memo[i] = i
#             else:
#                 memo[i] = memo[i-1] + memo[i-2]
#         return memo[n]
#
#     # dp数组
#     def fib_dp(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         dp = [0] * (n + 1)
#         dp[1] = 1
#         if n >= 2:
#             for i in range(2, n + 1):
#                 dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]


#  最长回文子串
# class Palidrome(object):
#     def __init__(self, s):
#         self.s = s
#         self.s_length = len(self.s)
#
#     # 方法一：暴力解法
#     def violence(self):
#         if self.s_length < 2:
#             return self.s
#         maxLen = 1
#         begin = 0
#         for i in range(self.s_length - 1):
#             for j in range(i + 1, self.s_length):
#                 if j - i + 1 > maxLen and self.vio_is_palidrome(i, j):
#                     begin = i
#                     maxLen = j - i +1
#         return self.s[begin:begin + maxLen]
#
#     def vio_is_palidrome(self, i, j):
#         while(i < j):
#             if self.s[i] != self.s[j]:
#                 return False
#             else:
#                 i += 1
#                 j -= 1
#         return True
#
#     # 方法二：中心扩散
#     def center(self):
#         if self.s_length < 2:
#             return self.s
#         start, end = 0, 0
#         for i in range(self.s_length - 1):
#             left1, right1 = self.cen_is_palidrome(i, i)
#             left2, right2 = self.cen_is_palidrome(i, i + 1)
#             if right1 - left1 > end - start:
#                 start = left1
#                 end = right1
#             if right2 - left2 > end - start:
#                 start = left2
#                 end = right2
#         return self.s[start:end + 1]
#
#     def cen_is_palidrome(self, left, right):
#         while(left >= 0 and right < self.s_length and self.s[left] == self.s[right]):
#             left -= 1
#             right += 1
#         return left + 1, right - 1
#
#     # 方法三：动态规划
#     def dynamic_pro(self):
#
#         begin = 0
#         maxlen = 0
#         if self.s_length < 2:
#             return self.s
#
#         dp = [[False] * self.s_length for _ in range(self.s_length)]
#
#         for i in range(self.s_length):
#             dp[i][i] = True
#
#         for L in range(2, self.s_length + 1):
#             for i in range(self.s_length):
#                 j = i + L - 1
#
#                 if j >= self.s_length:
#                     break
#
#                 if self.s[i] != self.s[j]:
#                     dp[i][j] = False
#                 else:
#                     if j - i <= 2:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 if dp[i][j] and j - i + 1 > maxlen:
#                     begin = i
#                     maxlen = j - i + 1
#         return self.s[begin:begin+maxlen]


# 有效括号
# class Solution:
#     # def generateParenthesis(self, n):
#     #     def generate(A):
#     #         if len(A) == 2*n:
#     #             if valid(A):
#     #                 ans.append("".join(A))
#     #         else:
#     #             A.append('(')
#     #             generate(A)
#     #             A.pop()
#     #             A.append(')')
#     #             generate(A)
#     #             A.pop()
#     #
#     #     def valid(A):
#     #         bal = 0
#     #         for c in A:
#     #             if c == '(':
#     #                 bal += 1
#     #             else:
#     #                 bal -= 1
#     #             if bal < 0:
#     #                 return False
#     #         return bal == 0
#     #
#     #     ans = []
#     #     generate([])
#     #     return ans
#
#
#     # def generateParenthesis(self, n):
#     #     ans = []
#     #
#     #     def backtrack(S, left, right):
#     #         if len(S) == 2 * n:
#     #             ans.append(''.join(S))
#     #             return
#     #         if left < n:
#     #             S.append('(')
#     #             backtrack(S, left + 1, right)
#     #             S.pop()
#     #         if right < left:
#     #             S.append(')')
#     #             backtrack(S, left, right + 1)
#     #             S.pop()
#     #
#     #     backtrack([], 0, 0)
#     #     return ans
#
#     def generateParenthesis(self, n):
#         if n == 1:
#             return list({'()'})
#         res = set()
#         for i in self.generateParenthesis(n - 1):
#             for j in range(len(i) + 1):
#                 res.add(i[0:j] + '()' + i[j:])
#         return list(res)

if __name__ == "__main__":
    # 斐波那契数列
    # value = 10
    # fibocci = Fibonacci()
    # result = fibocci.recursion(value)
    # result1 = fibocci.memorandum(value)
    # result2 = fibocci.dynamic_programming(value)
    # result3 = fibocci.fib_dp(value)
    # print(result, result1, result2, result3)

    # 最长回文子串
    # s = "dfjdjfhoeadadadagjgjhao"
    # palidrome = Palidrome(s)
    # result3 = palidrome.violence()
    # result4 = palidrome.center()
    # result5 = palidrome.dynamic_pro()
    # print(result3, '\n', result4, '\n', result5)

    # 有效括号
    # solution = Solution()
    # result6 = solution.generateParenthesis(4)
    # print(result6)

    dynamic_programming = Dynamic_Programming()

    # 最大子序和
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_num = dynamic_programming.max_sub_sequence(nums)
    print(max_num)

    # 斐波那契数列
    value = 10
    res = dynamic_programming.fib(value)
    print(res)

    # 爬楼梯
    res = dynamic_programming.climbStairs(value)
    print(res)

    # 使用最小花费爬楼梯
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = dynamic_programming.minCostClimbingStairs(cost)
    print(res)

    #不同路径
    m, n = 3, 7
    res = dynamic_programming.uniquePaths(m, n)
    print(res)

    # 不同路径Ⅱ
    obstacleGrid = [[0], [1]]
    res = dynamic_programming.uniquePathsWithObstacles(obstacleGrid)
    print(res)

    # 整数拆分
    res = dynamic_programming.integerBreak(n)
    print(res)




# def left_bound(nums, target):
#     if len(nums) == 0:
#         return -1
#     left = 0
#     right = len(nums)   #// 注意
#
#     while left < right:  #// 注意
#         mid = left + (right - left) // 2
#         if nums[mid] == target:
#             right = mid
#         elif nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid  # // 注意
#     return left
#
#
# nums = [1, 2, 2, 2, 3]
# target = 2
# res = left_bound(nums, target)
# print(res)
