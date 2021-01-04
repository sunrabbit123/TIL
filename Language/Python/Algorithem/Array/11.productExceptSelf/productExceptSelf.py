input1 = [1, 2, 3, 4]
output1 = [24, 12, 8, 6]
# 주의사항 % 나눗셈을 하지 않고 O(n)에 풀이하라 %

# 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def productExceptSelf(nums):
    out = []
    p = 1

    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]
    
    p = 1

    for i in range(len(nums) - 1,  -1, -1):
        out[i] *= p
        p *= nums[i]
    return out

print(productExceptSelf(input1))
