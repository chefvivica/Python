from typing import ItemsView


def max_value(nums):
    max = float('-inf')
    for item in nums:
        if item > max:
            max = item 
    return max


print(max_value([4, 7, 2, 8, 10, 9]))