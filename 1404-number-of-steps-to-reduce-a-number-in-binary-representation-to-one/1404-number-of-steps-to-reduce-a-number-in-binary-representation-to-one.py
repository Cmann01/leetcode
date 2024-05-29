class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        s = list(s)  # Convert the string to a list to make it mutable

        while len(s) > 1:
            if s[-1] == '0':  # If the number is even
                s.pop()  # Equivalent to dividing by 2
            else:  # If the number is odd
                # We need to add 1 to the binary number
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i >= 0:
                    s[i] = '1'
                else:
                    s.insert(0, '1')
            steps += 1

        return steps
