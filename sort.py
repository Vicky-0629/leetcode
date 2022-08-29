#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author : Vicky.chen
# Time : 2022/8/25 13:21


class Sort:
    def __init__(self):
        pass

    def quick_sort(self, my_list, start, end):
        """
        快速排序
        :param my_list:
        :param start:
        :param end:
        :return:
        """
        if start < end:
            i, j = start, end
            base = my_list[i]
            while i < j:
                while i < j and my_list[j] >= base:
                    j -= 1
                my_list[i] = my_list[j]
                while i < j and my_list[i] <= base:
                    i += 1
                my_list[j] = my_list[i]
            my_list[i] = base
            self.quick_sort(my_list, start, i - 1)
            self.quick_sort(my_list, i + 1, end)
        return my_list

    def bubble_sort(self, my_list):
        """
        冒泡排序
        :param my_list:
        :return:
        """
        length = len(my_list)
        if length <= 1:
            return my_list
        for i in range(length):
            for j in range(length - 1 - i):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list

    def insert_sort(self, my_list):
        """
        插入排序
        :return:
        """
        length = len(my_list)
        if length <= 1:
            return my_list
        for i in range(1, length):
            value = my_list[i]
            j = i - 1
            while j >= 0 and my_list[j] > value:
                my_list[j + 1] = my_list[j]
                j -= 1
            my_list[j + 1] = value
        return my_list


if __name__ == '__main__':
    nums = [3, 6, 78, 34, 2, 68, 40, 59, 34, 1]
    my_sort = Sort()
    res = my_sort.quick_sort(nums, 0, len(nums) - 1)
    print(res)
    res = my_sort.bubble_sort(nums)
    print(res)
    res = my_sort.insert_sort(nums)
    print(res)
