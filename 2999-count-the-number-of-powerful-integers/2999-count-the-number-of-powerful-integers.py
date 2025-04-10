class Solution:
    def solve(self, num_str: str, suffix: str, limit: int) -> int:
        if len(num_str) < len(suffix):
            return 0

        count = 0
        prefix_len = len(num_str) - len(suffix)
        trailing = num_str[-len(suffix):] if len(suffix) > 0 else ""

        for i in range(prefix_len):
            digit = int(num_str[i])
            if digit <= limit:
                count += digit * pow(limit + 1, prefix_len - i - 1)
            else:
                count += pow(limit + 1, prefix_len - i)
                return count

        # After building the same-length prefix, check if suffix part is >= target
        if trailing >= suffix:
            count += 1

        return count

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.solve(str(finish), s, limit) - self.solve(str(start - 1), s, limit)
