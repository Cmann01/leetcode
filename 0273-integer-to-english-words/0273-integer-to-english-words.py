class Solution:
    def __init__(self):
        self.less_than_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
            "Seventeen", "Eighteen", "Nineteen"
        ]
        self.tens = [
            "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
        
        return res.strip()

    def helper(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num % 100)

# Example usage
solution = Solution()
print(solution.numberToWords(123))        # Output: "One Hundred Twenty Three"
print(solution.numberToWords(12345))      # Output: "Twelve Thousand Three Hundred Forty Five"
print(solution.numberToWords(1234567))    # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
