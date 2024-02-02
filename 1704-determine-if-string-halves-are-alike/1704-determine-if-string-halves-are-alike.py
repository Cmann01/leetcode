class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def count_vowels(string):
            vowels = set("aeiouAEIOU")
            count = 0
            for char in string:
                if char in vowels:
                    count += 1
            return count
        
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        
        return count_vowels(a) == count_vowels(b)

# Test cases
solution = Solution()
print(solution.halvesAreAlike("book"))      # Output: true
print(solution.halvesAreAlike("textbook"))  # Output: false
