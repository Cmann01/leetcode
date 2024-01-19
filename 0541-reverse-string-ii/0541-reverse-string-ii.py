class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Convert string to list for easy manipulation
        s_list = list(s)
        
        # Iterate through the string with steps of 2k
        for i in range(0, len(s_list), 2*k):
            # Reverse the first k characters if there are at least k characters remaining
            s_list[i:i+k] = reversed(s_list[i:i+k])
        
        # Convert the list back to string and return
        return ''.join(s_list)

# Example usage:
solution = Solution()
output1 = solution.reverseStr("abcdefg", 2)
output2 = solution.reverseStr("abcd", 2)

print(output1)  # Output: "bacdfeg"
print(output2)  # Output: "bacd"
