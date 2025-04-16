def increasingTriplet(nums: list[int]) -> bool:
    first_num = float('inf') # unbound interger that can be used to check that are lower value
    second_num = float('inf')
    
    for num in nums:
        if num <= first_num:
            first_num = num
        elif num <= second_num:
            second_num = num
        else:
            return True
        
    return False

test_cases = [
    {"name": "Case 1", "input": [1,2,3,4,5], "expected": True},
    {"name": "Case 2", "input": [5,4,3,2,1], "expected": False},
    {"name": "Case 3", "input": [2,1,5,0,4,6], "expected": True},
    {"name": "Case 4", "input": [20,100,10,12,5,13], "expected": True},
    {"name": "Case 5", "input": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                 1,1,1,1], "expected": False},
    {"name": "Case 6", "input": [1,2,2147483647], "expected": True},
    # {"name": "Case 7", "input": [1,2,2147483647], "expected": True},
]

for test in test_cases:
    flowerbed_copy = test["input"]
    result = increasingTriplet(test["input"])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
