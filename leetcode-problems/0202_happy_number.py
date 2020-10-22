"""
Approach 1: Detect Cycles with a HashSet
- Time: O(243⋅3+logn+loglogn+logloglogn) = O(log n)
- Space: O(log n)

Approach 2: Floyd's Cycle-Finding Algorithm
- O(log n), O(1)

Approach 3: Hardcoding the Only Cycle (Advanced)
- O(log n), O(1)
"""
class Solution:
    def isHappy1(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

    def isHappy2(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

    def isHappy3(self, n: int) -> bool:

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1

    def isHappy3_2(self, n: int) -> bool:

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n != 4:
            n = get_next(n)

        return n == 1

    def isHappy(self, n: int) -> bool:
        while n > 4 or n == 1:
            # print("The number: ", n)
            square_num_sum = sum([int(i) ** 2 for i in str(n)])
            n = square_num_sum
            if n == 1:
                return True
            else:
                continue
        else:
            return False