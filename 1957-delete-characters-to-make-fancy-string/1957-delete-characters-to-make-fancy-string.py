class Solution:
    def makeFancyString(self, s: str) -> str:
        # List to store the final characters of the fancy string
        result = []
        
        # Initialize a counter to count consecutive duplicates
        count = 1
        
        # Add the first character to the result
        result.append(s[0])
        
        # Iterate over the string starting from the second character
        for i in range(1, len(s)):
            # If the current character is the same as the previous one, increment count
            if s[i] == s[i - 1]:
                count += 1
            else:
                # Reset the count when a new character is found
                count = 1
            
            # Only add the character if count is less than or equal to 2
            if count <= 2:
                result.append(s[i])
        
        # Join the result list to form the final fancy string
        return ''.join(result)
