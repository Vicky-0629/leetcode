#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2022/8/24 14:52
from collections import deque

order_res = []
level_res = []


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def construct(self, nums):
        if not nums:
            return None
        tree_list = []
        for num in nums:
            if num is None:
                tree_list.append(None)
            else:
                tree_list.append(TreeNode(num))
        for i in range(len(nums) // 2):
            if i * 2 + 1 < len(nums) and tree_list[i * 2 + 1]:
                tree_list[i].left = tree_list[i * 2 + 1]

            if i * 2 + 2 < len(nums) and tree_list[i * 2 + 2]:
                tree_list[i].right = tree_list[i * 2 + 2]
        self.root = tree_list[0]

    def pre_order(self, cur):
        """
        递归前序遍历
        :param cur:
        :return:
        """
        if cur is None:
            return
        order_res.append(cur.val)
        self.pre_order(cur.left)
        self.pre_order(cur.right)

    @staticmethod
    def pre_order_non_recursive(cur):
        """
        非递归前序遍历
        :param cur:
        :return:
        """
        if not cur:
            return
        stack = []
        stack.append(cur)
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            order_res.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)

    def in_order(self, cur):
        """
        递归中序遍历
        :param cur:
        :return:
        """
        if cur is None:
            return
        self.in_order(cur.left)
        order_res.append(cur.val)
        self.in_order(cur.right)

    @staticmethod
    def in_order_non_recursive(cur):
        """
        非递归中序遍历
        :param cur:
        :return:
        """
        if not cur:
            return
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            order_res.append(cur.val)
            cur = cur.right

    def past_order(self, cur):
        """
        递归后序遍历
        :param cur:
        :return:
        """
        if cur is None:
            return
        self.past_order(cur.left)
        self.past_order(cur.right)
        order_res.append(cur.val)

    @staticmethod
    def past_order_non_recursive(cur):
        """
        非递归后序遍历
        :param cur:
        :return:
        """
        if not cur:
            return
        stack = []
        stack2 = []
        while stack2 or cur:
            while cur:
                stack.append(cur)
                stack2.append(cur)
                cur = cur.right
            cur = stack2.pop()
            cur = cur.left
        while stack:
            cur = stack.pop()
            order_res.append(cur.val)

    def level_order(self, cur, depth):
        """
        层序遍历
        :param cur:
        :return:
        """
        if not cur:
            return
        if len(level_res) == depth:
            level_res.append([])
        level_res[depth].append(cur.val)
        if cur.left:
            self.level_order(cur.left, depth + 1)
        if cur.right:
            self.level_order(cur.right, depth + 1)

    @staticmethod
    def level_order_non_recursive(cur):
        dq = deque()
        dq.append(cur)
        while dq:
            tmp = dq.popleft()
            if not tmp:
                continue
            print(tmp.val)
            dq.append(tmp.left)
            dq.append(tmp.right)

    def inverse_tree(self, cur):
        """
        翻转二叉树
        :param cur:
        :return:
        """
        if not cur:
            return
        cur.left, cur.right = cur.right, cur.left

        self.inverse_tree(cur.left)
        self.inverse_tree(cur.right)

    def is_symmetric(self, root):
        """
        给定一个二叉树，检查它是否是镜像对称的。
        :param root:
        :return:
        """
        # 递归法






        # 迭代法——队列
        if not root:
            return True
        de = deque()
        de.append(root.left)
        de.append(root.right)
        while de:
            left_node = de.popleft()
            right_node = de.popleft()
            if not left_node and not right_node:
                continue
            elif not left_node or not right_node or left_node.val != right_node.val:
                return False
            de.append(left_node.left)
            de.append(right_node.right)
            de.append(left_node.right)
            de.append(right_node.left)
        return True

    def maxdepth(self, root):
        """
        给定一个二叉树，找出其最大深度。

        二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

        说明: 叶子节点是指没有子节点的节点。
        :param root:
        :return:
        """
        if not root:
            return 0
        de = deque()
        de.append(root)
        depth = 0
        while de:
            depth += 1
            length = len(de)
            for i in range(length):
                node = de.popleft()
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)
        return depth

    def max_depth(self, root):
        """
        给定一个 N 叉树，找到其最大深度。

        最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

        N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
        :param root:
        :return:
        """
        if not root:
            return 0
        de = deque()
        de.append(root)
        depth = 0
        while de:
            depth += 1
            length = len(de)
            for i in range(length):
                node = de.popleft()
                for child in node.children:
                    de.append(child)
        return depth

    def min_depth(self, root):
        """
        给定一个二叉树，找出其最小深度。

        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

        说明: 叶子节点是指没有子节点的节点。
        :param root:
        :return:
        """
        if not root:
            return 0
        de = deque()
        de.append(root)
        depth = 0
        while de:
            depth += 1
            length = len(de)
            for i in range(length):
                node = de.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)

    def count_nodes(self, root: TreeNode):
        """
        给出一个完全二叉树，求出该树的节点个数。
        :param root:
        :return:
        """
        if not root:
            return 0
        de = deque()
        de.append(root)
        counts = 0
        while de:
            length = len(de)
            counts += length
            for i in range(length):
                node = de.popleft()
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)
        return counts




if __name__ == '__main__':
    l = [2, 3, 4, 5, None, 7]
    t = Tree()
    t.construct(l)
    print("pre order:")
    t.pre_order(t.root)
    t.pre_order_non_recursive(t.root)
    print(order_res)
    print("in order:")
    t.in_order(t.root)
    t.in_order_non_recursive(t.root)
    print(order_res)
    print("post order:")
    t.past_order(t.root)
    t.past_order_non_recursive(t.root)
    print(order_res)
    print("level order:")
    t.level_order_non_recursive(t.root)
    t.level_order(t.root, 0)
    print(level_res)
    t.inverse_tree(t.root)
    t.pre_order(t.root)
    print(order_res)
