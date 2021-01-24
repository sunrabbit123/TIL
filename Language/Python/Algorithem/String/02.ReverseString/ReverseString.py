_input1 = ["H", "e", "l", "l", "o"]
_output1 = ["o", "l", "l", "e", "H"]

_input2 = ["H", "a", "n", "n", "a", "h"]
_output2 = ["h", "a", "n", "n", "a", "H"]

# Two point Swap
def reverseString1(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1


# like Python
def reverseString2(s) -> None:
    s.reverse()


def reverseString3(s) -> None:
    s[:] = s[::-1]
