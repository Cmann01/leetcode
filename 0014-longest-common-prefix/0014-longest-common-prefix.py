class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Sort the list of strings to bring the common prefixes together
        strs.sort()

        # Take the first and last string in the sorted list
        first_str = strs[0]
        last_str = strs[-1]

        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        return "".join(common_prefix)

# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))      # Output: ""
