class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        count = 0
        for i in nums:
            seen.add(i)
            count += 1
        if len(seen) != count:
            return True
        return False
            
            