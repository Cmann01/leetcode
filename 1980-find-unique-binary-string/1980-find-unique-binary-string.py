class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # Construct a binary string using diagonalization
        result = ""
        for i in range(n):
            # Flip the i-th bit of the i-th string
            result += "0" if nums[i][i] == "1" else "1"
        return result
