#！usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    def twoSum(nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
if __name__ == "__main__":
    Solution.twoSum(input(),input())