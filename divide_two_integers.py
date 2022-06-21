# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
# truncated to 8, and -2.7335 would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
#     [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and
#     if the quotient is strictly less than -2^31, then return -2^31.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg_dividend = False
        neg_divisor = False
        if dividend < 0:
            neg_dividend = True
        if divisor < 0:
            neg_divisor = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            count += 1
            dividend = dividend - divisor
        if (neg_divisor == False) and (neg_dividend == False):
            pass
        elif neg_divisor and neg_dividend:
            pass
        else:
            count = -count
        return count


soln = Solution()
print(soln.divide(10, 3))
print(soln.divide(7, -3))
print(soln.divide(-7, 3))
print(soln.divide(-19, -3))
