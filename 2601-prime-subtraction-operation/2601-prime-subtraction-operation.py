from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Helper function to generate all primes less than `n` using the Sieve of Eratosthenes
        def sieve(n: int) -> List[int]:
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [i for i, prime in enumerate(is_prime) if prime]

        # Precompute all primes less than 1000
        primes = sieve(1000)
        
        # Traverse the array and apply prime subtraction to maintain strictly increasing order
        prev = 0  # Initially, the "previous" number to compare is 0 (no restriction on the first element)
        
        for num in nums:
            # We need to make `num` greater than `prev`
            for p in reversed(primes):
                if p < num and num - p > prev:
                    num -= p
                    break  # Apply the first applicable prime and break
            
            # After operation, check if the current num is still greater than the previous element
            if num <= prev:
                return False
            prev = num  # Update prev to current num after modification
        
        return True
