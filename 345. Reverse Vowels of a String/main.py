def reverseVowels(s: str) -> str:
    reversed_vowels = [vowel for vowel in s if vowel in 'aeiouAEIOU'][::-1]
    s_list = list(s)
    
    for index in range(len(list(s))):
        if s_list[index] in 'aeiouAEIOU':
            s_list[index] = reversed_vowels[0]
            reversed_vowels.pop(0)
    
    return ''.join(s_list)

test_cases = [
    {"name": "Case 1", "input": ("IceCreAm"), "expected": "AceCreIm"},
    {"name": "Case 2", "input": ("leetcode"), "expected": "leotcede"},
]

for test in test_cases:
    flowerbed_copy = test["input"]
    result = reverseVowels(test["input"])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
