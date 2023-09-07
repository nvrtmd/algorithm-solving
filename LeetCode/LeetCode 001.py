# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        roman_number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = []
        result = 0
        for i in s:
            number.append(roman_number[i])

        number = list(reversed(number))
        print(number)
        for i in range(len(number)):
            if i < 1:
                result += number[i]
            else:
                if number[i] < number[i - 1]:
                    result -= number[i]
                else:
                    result += number[i]

        return result
