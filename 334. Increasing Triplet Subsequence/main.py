def increasingTriplet(nums: list[int]) -> bool:
    
    pass

test_cases = [
    {"name": "Case 1", "input": [1,2,3,4,5], "expected": True},
    {"name": "Case 2", "input": [5,4,3,2,1], "expected": False},
    {"name": "Case 3", "input": [2,1,5,0,4,6], "expected": True},
]

for test in test_cases:
    flowerbed_copy = test["input"]
    result = increasingTriplet(test["input"])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
