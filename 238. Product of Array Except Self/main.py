def productExceptSelf(nums: list[int]) -> list[int]:
    #  O(n) is demanded here
    n = len(nums)
    result = [1] * n
    left, right = 1, 1
    
    for i in range(n):
        result[i] = left
        left *= nums[i]
        
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n
    left, right = 1, 1
    
    for i in range(n):
        result[i] *= left         
        result[n - 1 - i] *= right  # goes backwards
        left *= nums[i]
        right *= nums[n - 1 - i]

    return result

test_cases = [
    {"name": "Case 1", "input": [1,2,3,4], "expected": [24,12,8,6]},
    {"name": "Case 2", "input": [-1,1,0,-3,3], "expected": [0,0,9,0,0]},
    # {"name": "Case 2", "input": ("a good   example"), "expected": "example good a"},
]

for test in test_cases:
    flowerbed_copy = test["input"]
    result = productExceptSelf(test["input"])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
