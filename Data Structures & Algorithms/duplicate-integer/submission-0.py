class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if str(num) in map:
                return True
            
            map[str(num)] = 1
            

        return False