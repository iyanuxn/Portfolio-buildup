class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists = list(nums)
        n = len(lists)
        return [[lists[k] for k in range(n) if i&1<<k] for i in range(2**n)]
        return(subsets())
        