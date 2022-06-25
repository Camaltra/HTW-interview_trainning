#!/usr/bin/python3

def containDuplicate(nums):
  alreadyVisitedNumber = {}
  for num in nums:
    if num in alreadyVisitedNumber:
      return True
    else:
      alreadyVisitedNumber[num] = True
  return False
