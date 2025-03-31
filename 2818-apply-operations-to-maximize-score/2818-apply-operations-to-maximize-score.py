from collections import deque
from math import sqrt

MOD = 10**9 + 7

class Solution:
    def count_prime_factors(self, n):
        count = 0
        if n % 2 == 0:
            count += 1
            while n % 2 == 0:
                n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                count += 1
                while n % i == 0:
                    n //= i
        if n > 1:
            count += 1
        return count

    def maximumScore(self, nums, k):
        n = len(nums)
        prime_scores = [self.count_prime_factors(num) for num in nums]
        
        next_greater = [n] * n
        prev_greater = [-1] * n
        stack = deque()
        
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            next_greater[i] = stack[-1] if stack else n
            stack.append(i)
        
        subarrays = [(nums[i], i, (next_greater[i] - i) * (i - prev_greater[i])) for i in range(n)]
        subarrays.sort(reverse=True, key=lambda x: (x[0], x[1]))
        
        score = 1
        idx = 0
        while k > 0:
            num, i, freq = subarrays[idx]
            use = min(freq, k)
            score = (score * pow(num, use, MOD)) % MOD
            k -= use
            idx += 1
        
        return score