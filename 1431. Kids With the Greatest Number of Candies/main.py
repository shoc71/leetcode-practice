def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    final_result = []
    for candy in candies:
        final_result.append(True) if (candy + extraCandies) >= max(candies) else final_result.append(False)

    return final_result

test_cases = [
    {"name": "Case 1", "input": ([2,3,5,1,3], 3), "expected": [True,True,True,False,True]},
    {"name": "Case 2", "input": ([4,2,1,1,2], 1), "expected": [True,False,False,False,False]},
    {"name": "Case 3", "input": ([12,1,12], 10), "expected": [True,False,True]},
]

for case in test_cases:
    result = kidsWithCandies(*case["input"])
    print(f"{case['name']}: got '{result}', expected '{case['expected']}' - {'✅ PASS' if result == case['expected'] else '❌ FAIL'}")
