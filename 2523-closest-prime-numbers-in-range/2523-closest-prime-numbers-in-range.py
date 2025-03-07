from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n: int) -> List[bool]:
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime
        
        is_prime = sieve(right)
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        closest_pair = [-1, -1]
        
        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                closest_pair = [primes[i], primes[i + 1]]
                
        return closest_pair
