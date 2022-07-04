#!/usr/bin/python3

def twoSum(nums, target)
    dictOfNum = {}
    for i, value in enumerate(nums):
        diff = target - value
        if diff in dictOfNum:
            return [i, dictOfNum[diff]]
        dictOfNum[nums[i]] = i
