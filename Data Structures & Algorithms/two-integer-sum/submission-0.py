class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i, num in enumerate(nums):
            complement = str(target - num)

            if complement in targets:
                return [targets[complement], i]
            
            targets[str(num)] = i
        
        return [-1, -1]