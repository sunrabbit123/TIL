input = [-1, 0, 1, 2, -1, -4]
output = [[-1, 0, 1], [-1, -1, -2]]

# Brute force
def threeSum(self, nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))
    return results


def threeSum2(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results


print(threeSum2(nums=input))
