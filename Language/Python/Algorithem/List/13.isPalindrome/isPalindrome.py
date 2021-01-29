input1 = [1,2]
output1 = False

input1 = [1,2,2,1]
output2 = True

#1 List 변환
def isPalindrome(head) -> bool:
    q = List()

    if not head:
        return True
    
    node = head

    for i in node:
        if i is None:
            break
        q.append(i)

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

#2 Deque 이용

from typing import Deque
import collections

def isPalindrome(head) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head

    for i in node:
        if i is None:
            break
        q.append(i)
    # 달라진점 
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True
