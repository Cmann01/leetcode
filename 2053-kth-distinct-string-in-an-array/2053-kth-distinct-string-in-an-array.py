class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Step 1: Count the frequency of each string
        frequency = {}
        for string in arr:
            if string in frequency:
                frequency[string] += 1
            else:
                frequency[string] = 1
        
        # Step 2: Collect distinct strings in the order of their appearance
        distinct_strings = [string for string in arr if frequency[string] == 1]
        
        # Step 3: Return the k-th distinct string or an empty string if not enough distinct strings
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""
