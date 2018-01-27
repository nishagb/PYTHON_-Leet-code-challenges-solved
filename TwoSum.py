#Author: Nisha Gurunath Bharathi
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum=0;
        for i in range(0,len(nums)):   #for(i=0;i<len(nums);i++) //java for loop
                for j in range(i+1,len(nums)):     #for(j=i+1;j<len(nums);j++): //java for loop
                    sum=0
                    sum=nums[i]+nums[j]
                    if (sum == target): 
                        List=[j,i]
                        break
                    #j=j+1
               # i=i+1
        return List
