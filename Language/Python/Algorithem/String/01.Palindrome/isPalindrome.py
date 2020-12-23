_input1 = 'A man, A plan, a canal: Panama'
_output1 = True

_input2 = 'race a car'
_output2 = False

import collections
# list
def isPalindrome1(s : str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
        
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True


# Deque
def isPalindrome2(s : str) -> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False
    
    return True

# Sliceing
import re
def isPalindrome3(s : str) -> bool:
    s = s.lower()

    # 필터링
    s = re.sub('[^a-z0-9]', '', s)

    # 뒤집은 값과, 안뒤집은 값이 동일한지 비교
    return s == s[::-1]

