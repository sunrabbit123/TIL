input1 = "babad"
output1 = "bab"

input2 = "cbbd"
output2 = "bb"

# 중앙을 중심으로 확장
def longest_Palindrome(self, s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1 : right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    for i in range(0, len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result
