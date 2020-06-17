#! usr/local/bin/python3.7

# Bubblesort implementation

# Creating random table, containing 10 numbers.

from random import randint

table = [randint(1, 50) for i in range(10)]
print("Unsorted table: ", table)


def sort(table_to_sort):
    for i in range(len(table_to_sort)):
        last_index = len(table_to_sort)-1
        while last_index > i:
            if table[last_index] < table[last_index-1]:
                temp = table_to_sort[last_index]
                table_to_sort[last_index] = table_to_sort[last_index-1]
                table_to_sort[last_index-1] = temp
            last_index -= 1
    return table_to_sort


print("Sorted table: ", sort(table))
