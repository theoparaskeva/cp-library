# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.


# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: date = "2019-02-10"
# Output: 41


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        t = 28
        if int(year) % 4 == 0:
            t = 29
        if int(year) == 1900:
            t = 28

        y = [31, t, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        ans = 0

        for x in range(len(y)):
            if x == int(month)-1:
                break
            ans += y[x]

        return ans + int(day)


# leap year stuff
#  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
