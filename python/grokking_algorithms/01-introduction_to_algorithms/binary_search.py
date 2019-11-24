#/usr/bin/env python

'''
注：仅当列表是有序的时候，二分查找法才管用
二分查找法：
对于包含n个元素的列表，用二分查找最多需要logn步
'''

def binary_search(search_list, item):
    low = 0
    high = len(search_list) -1

    while low <= high:
        mid = int((low + high) / 2)
        guess = search_list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))