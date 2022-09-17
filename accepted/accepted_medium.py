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

    def convert_linear_str_to_zigzag(self, s: str, numRows: int) -> str:
        # sourcery skip: use-contextlib-suppress
        """
            Link: https://leetcode.com/problems/zigzag-conversion/
            Runtime: 72 ms
        """
        len_s = len(s)
        if len_s < 3 or numRows == 1: return s
        def x(l, t):
            if len(l) < t:
                l.append(None)
                x(l, t)
            return l
        l = []
        t = 0
        while t < len_s:
            l.append(list(s[t:numRows+t]))
            t += numRows
            l.append(list(reversed(x(list(s[t:numRows-2+t]), numRows-2))))
            t += numRows-2
        l = l[:-1] if l[-1] == [] else l
        len_l = len(l)
        s1 = ''
        s2 = ''
        s3 = ''
        t = len(l[0]) - 2
        for i in range(0, len_l, 2):
            s1 += l[i].pop(0)
            try:s3 += l[i].pop(t)
            except IndexError: pass
        for i in range(len(l[0])):
            for j in range(len_l):
                try:
                    if l[j][i] is not None:
                        s2 += l[j][i]
                except IndexError: pass
        return s1 + s2 + s3

    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        # sourcery skip: list-comprehension, use-itertools-product
        for i in board:
            r = [j for j in i if j != '.' ]
            if len(set(r)) < len(r): return False

        for i in range(9):
            r = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(set(r)) < len(r): return False

        for i in (0, 3, 6):
            for t in (0, 3, 6):
                r = []
                for j in range(i, i+3):
                    for k in range(t, t+3):
                        if board[j][k] != '.':
                            r.append(board[j][k])
                if len(set(r)) < len(r): return False

        return True