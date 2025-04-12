from math import factorial
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        st = set()

        d = (n + 1) // 2
        start = 10 ** (d - 1)
        end = 10 ** d

        for num in range(start, end):
            left_half = str(num)
            if n % 2 == 0:
                right_half = left_half[::-1]
                full = left_half + right_half
            else:
                right_half = left_half[:-1][::-1]
                full = left_half + right_half

            number = int(full)
            if number % k != 0:
                continue

            sorted_digits = ''.join(sorted(full))
            st.add(sorted_digits)

        # Precompute factorials up to 10!
        factorials = [1] * 11
        for i in range(1, 11):
            factorials[i] = factorials[i - 1] * i

        result = 0
        for s in st:
            count = Counter(s)

            total_digits = len(s)
            zero_digits = count['0']
            non_zero_digits = total_digits - zero_digits

            # Count valid permutations without leading zero
            # Fix one non-zero digit at first position
            temp = 0
            for d in count:
                if d == '0':
                    continue
                count[d] -= 1

                perm = factorials[total_digits - 1]
                for val in count.values():
                    perm //= factorials[val]
                temp += perm

                count[d] += 1  # Restore

            result += temp

        return result
