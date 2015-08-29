#!/usr/bin/env python

from unittest import TestCase, main

def swap(array, this_index, that_index):
    array[this_index], array[that_index] = array[that_index], array[this_index]


def find_min_index(array, start_index):
    min_index, min_value = start_index, array[start_index]

    for i in range(start_index, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            min_index = i

    return min_index


def sort(array):
    for i in range(len(array)):
        min_index = find_min_index(array, i)
        swap(array, i, min_index)

    return array


class TestSelectionSort(TestCase):
    def test_sort(self):
        array = [8, 2, 3, 9, 7]

        result = sort(array)

        self.assertEqual(result, [2, 3, 7, 8, 9])

main()
