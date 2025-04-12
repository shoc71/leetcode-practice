# cant place flowers in adjacent pots

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:   
    # edge cases
    if len(flowerbed) == 0: return False
    if n == 0: return True
    
    count = 0
    length = len(flowerbed)
    
    for i in range(length):
        
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    
    return False

test_cases = [
    {"name": "Case 1", "input": ([1, 0, 0, 0, 1], 1), "expected": True},
    {"name": "Case 2", "input": ([1, 0, 0, 0, 1], 2), "expected": False},
    {"name": "Case 3", "input": ([0, 0, 0, 0, 0], 3), "expected": True},
    {"name": "Case 4", "input": ([0, 0], 2), "expected": False},
    {"name": "Case 5", "input": ([0, 0], 1), "expected": True},
    {"name": "Case 6", "input": ([0], 2), "expected": False},
    {"name": "Case 7", "input": ([0], 1), "expected": True},
    {"name": "Case 9", "input": ([1,0,1,0,1,0,1], 0), "expected": True},
]

for test in test_cases:
    flowerbed_copy = test["input"][0].copy()  # avoid modifying the original in-place
    result = canPlaceFlowers(flowerbed_copy, test["input"][1])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
