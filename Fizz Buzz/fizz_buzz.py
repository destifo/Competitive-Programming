class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final_list = list()
        for num in range(n + 1):
            if num == 0:
                continue
            if num % 15 == 0:
                final_list.append("FizzBuzz")
                continue
            if num % 3 == 0:
                final_list.append("Fizz")
                continue
            if num % 5 == 0:
                final_list.append("Buzz")
                continue
            final_list.append(str(num))
        return final_list