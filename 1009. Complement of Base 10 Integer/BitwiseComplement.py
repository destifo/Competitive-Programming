class Solution:

    # O(logn) time,
    # O(logn) space,
    # Approach: bit operations,
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bits = []
        while n > 0:

            remainder = n % 2
            bits.append(str(remainder))

            n //= 2

        inverted_bits = []
        # print(bits)
        for bit in reversed(bits):
            inverted = "0" if bit == "1" else "1"
            inverted_bits.append(inverted)

        # print(inverted_bits)
        return int("".join(inverted_bits), 2)
