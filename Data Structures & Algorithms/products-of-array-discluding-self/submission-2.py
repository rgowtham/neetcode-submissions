class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pp = [1] * n
        sp = [1] * n
        ans = [1] * n

        for i in range(1, n):
            pp[i] = pp[i-1] * nums[i-1]
        # print(pp)
        suffix_prod = 1
        for i in range(n-2, -1, -1):
            pp[i] *= suffix_prod * nums[i+1]
            suffix_prod *= nums[i+1]

        return pp