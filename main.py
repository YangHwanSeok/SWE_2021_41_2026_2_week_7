from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(length - i):
            if (j != 0) and (target == nums[i] + nums[i+j]) :
                return [i,i+j]