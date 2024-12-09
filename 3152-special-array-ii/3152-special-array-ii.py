class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # Step 1: Preprocess to find mismatched pairs
        mismatch = [0] * (n - 1)
        for i in range(n - 1):
            if (nums[i] % 2 == nums[i + 1] % 2):  # same parity
                mismatch[i] = 1
        
        # Step 2: Create a prefix sum array
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + mismatch[i - 1]
        
        # Step 3: Answer each query
        result = []
        for fromi, toi in queries:
            # Count mismatches in the range [fromi, toi - 1]
            if fromi == toi:  # single element subarray is always special
                result.append(True)
            else:
                mismatches = prefix_sum[toi] - prefix_sum[fromi]
                result.append(mismatches == 0)
        
        return result
