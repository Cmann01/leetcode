class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        # Edge case for 1-digit numbers
        if length == 1:
            return str(int(n) - 1)
        
        # Larger and smaller than n edge cases
        candidates.add(str(10**length + 1))  # Smallest palindrome larger than n
        candidates.add(str(10**(length-1) - 1))  # Largest palindrome smaller than n
        
        # Middle part of n
        prefix = int(n[:(length + 1) // 2])
        
        # Create palindromes by modifying the prefix
        for i in [-1, 0, 1]:
            candidate = str(prefix + i)
            if length % 2 == 0:
                candidate = candidate + candidate[::-1]
            else:
                candidate = candidate + candidate[-2::-1]
            candidates.add(candidate)
        
        candidates.discard(n)  # Remove the original number if it's a palindrome
        
        # Find the closest palindrome
        def difference(x):
            return abs(int(x) - int(n))
        
        return min(candidates, key=lambda x: (difference(x), int(x)))

# Example Usage:
# sol = Solution()
# print(sol.nearestPalindromic("123"))  # Output: "121"
# print(sol.nearestPalindromic("1"))    # Output: "0"
