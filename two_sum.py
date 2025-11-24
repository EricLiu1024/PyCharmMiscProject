class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        harsh_map = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in harsh_map:
                print(harsh_map[complement],i)
            harsh_map[num] = i