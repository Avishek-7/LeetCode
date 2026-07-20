class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squared_digits(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow = n
        fast = n

        while True:
            slow = sum_of_squared_digits(slow)
            fast = sum_of_squared_digits(sum_of_squared_digits(fast))

            if slow == fast:
                break
            if slow == 1:
                return True
        return slow == 1

        