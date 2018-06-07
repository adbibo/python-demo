#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return False

        result_list = list()
        temp_dict = dict()
        for index in range(len(nums)):
            for index2 in range(index, len(nums)):
                _sum = nums[index] + nums[index2]
                if (0-_sum) not in temp_dict:
                    temp_dict[0-_sum] = [index, index2]
                else:
                    result_list.append([nums[index], nums[temp_dict[0-_sum][0]], nums[temp_dict[0-_sum][1]]])

        return result_list



