#!/usr/bin/env python

def get_sum_using_recursion(lis):

    def loop(lis):
        if lis:
            return lis[-1] + loop(lis[:-1])

        return 0

    def loop2(i, lis):
        if i == len(lis): # sentinel value
            return 0

        return lis[i] + loop2(i + 1, lis)

    def loop3(i, lis):
        if i + 1 < len(lis):
            return lis[i] + loop3(i + 1, lis)

        return lis[i]

    return loop(lis), loop2(0, lis), loop3(0, lis)

print(get_sum_using_recursion([1, 2, 3, 4, 5, 6]))

def get_sum_of_consecutive_numbers(start, sentinel):
    if start == sentinel: # sentinel value
        return 0

    return start + get_sum_of_consecutive_numbers(start + 1, sentinel)

print(get_sum_of_consecutive_numbers(1, 7))