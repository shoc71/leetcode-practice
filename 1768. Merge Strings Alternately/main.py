def mergeAlternately(word1: str, word2: str) -> str:
    
    list1 = [w for w in word1]
    list2 = [w for w in word2]
    final_string = []

    for char in range(len(list1) + len(list2)):
        if char < len(list1): final_string.append(list1[char])
        if char < len(list2): final_string.append(list2[char])      
        
    return "".join(final_string)

test_cases = [
    {"name": "Case 1", "input": ("abc", "pqr"), "expected": "apbqcr"},
    {"name": "Case 2", "input": ("ab", "pqrs"), "expected": "apbqrs"},
    {"name": "Case 3", "input": ("abcd", "pq"), "expected": "apbqcd"},
]

for case in test_cases:
    result = mergeAlternately(*case["input"])
    print(f"{case['name']}: got '{result}', expected '{case['expected']}' - {'✅ PASS' if result == case['expected'] else '❌ FAIL'}")
