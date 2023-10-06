from typing import List


class AcceptedEasy:
    def roman_to_int(self, s: str) -> int:
        """
            Link: https://leetcode.com/problems/roman-to-integer/
            Runtime: 103 ms
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        num = roman_map[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                num += roman_map[s[i]]
            else:
                num -= roman_map[s[i]]
        return num

    def length_of_last_word(self, s: str) -> int:
        """
            Link: https://leetcode.com/problems/length-of-last-word/
            Runtime: 54 ms
        """
        strIndex = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                strIndex = i
                break

        spaceIndex = -1
        for i in range(strIndex, -1, -1):
            if s[i] == ' ':
                spaceIndex = i
                break
        return strIndex - spaceIndex

    def plus_one(self, digits: List[int]) -> List[int]:
        """
            Link: https://leetcode.com/problems/plus-one/
            Runtime: 34 ms
        """
        number = 0
        for i in digits:
            number = (number + i) * 10
        number = number // 10 + 1

        number_list = []
        for i in str(number):
            number_list.append(int(i))

        return number_list

    def is_palindrome(x: int) -> bool:
        """
            Link: https://leetcode.com/problems/palindrome-number/
            Runtime: 61 ms
        """
        if x < 0:
            return False

        reverse_x = 0
        x2 = x

        while x2 > 0:
            reverse_x  = (reverse_x + (x2 % 10)) * 10
            x2 //= 10

        reverse_x //= 10
        return reverse_x == x