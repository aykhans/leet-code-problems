from typing import List


class AcceptedMedium:
    def reverse_int(self, x: int) -> int:
        """
            Link: https://leetcode.com/problems/reverse-integer/
            Runtime: 36 ms
        """
        ctr = 1
        if x < 0:
            ctr = -1
            x *= -1

        nr = 0
        while x > 0:
            nr = (nr + (x % 10)) * 10
            x //= 10
        nr //= 10

        return nr * ctr if -2147483648 <= nr <= 2147483647 else 0

    def letter_combinations(self, digits: str) -> List[str]:
        """
            Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
            Runtime: 39 ms
        """
        # sourcery skip: use-itertools-product
        number_to_string = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        l = ['']
        l2 = []

        for n in digits:
            for s in number_to_string[n]:
                for i in l:
                    l2.append(i+s)
            l = l2.copy()
            l2 = []
        return [] if l[0] == '' else l