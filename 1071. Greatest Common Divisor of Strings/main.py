def gcdOfStrings(str1: str, str2: str) -> str:
    
    # edge case
    if str1 + str2 != str2 + str1: return ""
    
    def check(s, t):
        while t:
            s, t = t, s % t
        return s
    
    return str1[:check(len(str1), len(str2))]

test_cases = [
    {"name": "Case 1", "input": ("ABCABC", "ABC"), "expected": "ABC"},
    {"name": "Case 2", "input": ("ABABAB", "ABAB"), "expected": "AB"},
    {"name": "Case 3", "input": ("LEET", "CODE"), "expected": ""},
]

for case in test_cases:
    result = gcdOfStrings(*case["input"])
    print(f"{case['name']}: got '{result}', expected '{case['expected']}' - {'✅ PASS' if result == case['expected'] else '❌ FAIL'}")
