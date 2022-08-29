#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2021/10/20 18:48


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkList(object):

    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.head == None

    def length(self):
        """
        链表长度
        :return:
        """
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next

    def add(self, val):
        """
        头插法
        :param val:
        :return:
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def insert(self, pos, val):
        """
        自定义插入
        :param pos:
        :param val:
        :return:
        """
        if pos <= 0:
            self.add(val)
        elif pos > self.length() - 1:
            self.append(val)
        else:
            count = 0
            node = ListNode(val)
            cur = self.head
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self, val):
        """
        查询是否链表中是否包含val
        :param val:
        :return:
        """
        cur = self.head
        while cur != None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    def append(self, val):
        """
        尾插
        :param val:
        :return:
        """
        node = ListNode(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def remove(self, val):
        """
        移除节点
        :return:
        """
        cur = self.head
        while cur != None:
            if cur.val == val:
                if cur == self.head:
                    self.head = cur.next
                else:
                    cur.next = cur.next.next
                break
            else:
                cur = cur.next
        return cur

    # 移除链表元素
    def remove_elements(self, head, val):
        """
        给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(next=head)
        node = dummy_head
        while node.next != None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy_head.next

    # 翻转链表
    def reverse_list(self):
        """
        给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = self.head
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.head = pre
        self.travel()

    # 两两交换链表中的节点
    def swap_pairs(self, head):
        """
        给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = head.next
        head.next = self.swap_pairs(cur.next)
        cur.next = head
        return cur

    # 876 链表的中间结点
    def middle_node(self, head: ListNode) -> ListNode:
        """
        给定一个头结点为 head 的非空单链表，返回链表的中间结点。

        如果有两个中间结点，则返回第二个中间结点。
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 19 删除链表的倒数第 N 个结点
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        """
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
        :param head:
        :param n:
        :return:
        """
        L = self.length()
        cur = head
        count = 0
        while count < L - n:
            cur = cur.next
            count += 1
        if count == 0:
            return cur.next
        else:
            cur.next = cur.next.next
            return cur


if __name__ == '__main__':
    single_link_list = SingleLinkList()
    data = [1, 2, 6, 3, 4]
    value = 6
    for i in data:
        single_link_list.append(i)
    # single_link_list.travel()
    # single_link_list.add(100)
    # single_link_list.travel()
    # single_link_list.insert(2, 200)
    # single_link_list.travel()
    # res1 = single_link_list.search(3)
    # print(res1)
    # single_link_list.remove(100)
    # single_link_list.travel()

    # 移除链表元素
    res = single_link_list.remove_elements(single_link_list.head, value)
    print(res)

    # 翻转链表
    res = single_link_list.reverse_list()
    print(res)

    # 两两交换链表中的节点
    res = single_link_list.swap_pairs(single_link_list.head)
    print(res)

    # 876链表的中间结点
    res = single_link_list.middle_node(single_link_list.head)
    print("中间结点：%s" % res)

    # 19 删除链表的倒数第 N 个结点
    res = single_link_list.remove_nth_from_end(single_link_list.head, 2)
    print("中间结点：%s" % res)
