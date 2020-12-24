input = [1, 4, 3, 2]
output = 4

# asc sort

def arrayPairSum(nums: List[int]):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    
    return sum

# 짝수 번째 값 계산

def arrayPairSum(nums: List[int]):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum

def arrayPairSum(nums : List[int]):
    return sum(sorted(nums[::2]))
    