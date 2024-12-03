class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        # Create a list to store the modified string
        result = []
        prev_index = 0
        
        # Iterate over the spaces indices
        for space in spaces:
            # Add the substring from the previous index to the current space index
            result.append(s[prev_index:space])
            # Add a space
            result.append(" ")
            # Update the previous index to the current space index
            prev_index = space
        
        # Add the remaining part of the string
        result.append(s[prev_index:])
        
        # Join the parts into a single string and return
        return "".join(result)
