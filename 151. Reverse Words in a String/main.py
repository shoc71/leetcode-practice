def reverseWords(s: str) -> str:
    s_list = s.lstrip().rstrip().split(" ")[::-1]    
    result = list(filter(None, s_list)) # filtering out extra spaces looking like '' bewteen words
    
    return ' '.join(result)

# better solution
def reverseWords(s: str) -> str:
    lst = s.split()
    lst.reverse()
    return " ".join(lst)

test_cases = [
    {"name": "Case 1", "input": ("the sky is blue"), "expected": "blue is sky the"},
    {"name": "Case 2", "input": ("  hello world  "), "expected": "world hello"},
    {"name": "Case 2", "input": ("a good   example"), "expected": "example good a"},
]

for test in test_cases:
    flowerbed_copy = test["input"]
    result = reverseWords(test["input"])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
