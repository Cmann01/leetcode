class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            # Find the index of the first occurrence of the minimum value
            min_index = nums.index(min(nums))
            # Replace the minimum value with its multiplied value
            nums[min_index] *= multiplier
        return nums
