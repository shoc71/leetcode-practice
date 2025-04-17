def compress(chars: list[str]) -> int:
    
    empty_dict = {}
    
    # for char in range(len(chars)):    
    #     if chars[char] not in empty_dick:
    #         empty_dick[chars[char]] = 1
    #     else:
    #         empty_dick[chars[char]] += 1
            
    # empty_dick = {char: chars[:i+1].count(char) for i, char in enumerate(chars)}
    empty_dict = {}; [empty_dict.update({c: empty_dict.get(c, 0) + 1}) for c in chars]

    new_list_2 = list(''.join([f"{key}" if value == 1 else f"{key}{value}" for key, value in empty_dict.items()]))
    
    return new_list_2

test_cases = [
    {"name": "Case 1", "input": ["a","a","b","b","c","c","c"], "expected": ["a","2","b","2","c","3"]},
    {"name": "Case 2", "input": ['a'], "expected": ['a']},
    {"name": "Case 3", "input": ['a','b','a'], "expected": ['a','2','b']},
    {"name": "Case 4", "input": ["a","b","b","b","b","b","b","b","b","b","b","b","b"], "expected": ["a","b","1","2"]}
]

for test in test_cases:
    flowerbed_copy = test["input"]
    result = compress(test["input"])
    passed = result == test["expected"]
    print(f"{test['name']}: expected {test['expected']}, got {result} - {'✅ PASS' if passed else '❌ FAIL'}")
