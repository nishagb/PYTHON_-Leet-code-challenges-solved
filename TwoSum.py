class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum=0;
        for i in range(0,len(nums)):   #for(i=0;i<len(nums);i++)
                for j in range(i+1,len(nums)):     #for(j=i+1;j<len(nums);j++):
                    sum=0
                    sum=nums[i]+nums[j]
                    if (sum == target): 
                        List=[j,i]
                        break
                    #j=j+1
               # i=i+1
        return List
