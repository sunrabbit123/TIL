input = [[2, 7, 11, 15], 9]
_output = [0, 1]

# Brute force
def twoSum1(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == taget:
                return [i, j]


# use in
def twoSum2(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = targe - n

        if complement in nums[i + 1 :]:
            return [nums.index(n), nums[i + 1 :].index(complement) + (i + 1)]


# 첫 번째 수를 뺀 결과 키 조회
def twoSum3(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(num):
        if target - num in nums_map and i != nums_map[target - num]:
            return [nums.index(n), nums_map[target - num]]


# 조회 구조 개선
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
