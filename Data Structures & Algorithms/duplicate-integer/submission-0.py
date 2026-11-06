class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=len(nums)
        p=set(nums)
        if s>len(p):
            return True
        return False