def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def ternary_to_decimal(ternary_str):
    return int(ternary_str, 3)

def find_original_number(a, b):
    # 2진수 후보들 찾기
    binary_candidates = set()
    for i in range(len(a)):
        flipped = '0' if a[i] == '1' else '1'
        candidate = a[:i] + flipped + a[i+1:]
        binary_candidates.add(binary_to_decimal(candidate))

    # 3진수 후보들 찾기
    ternary_candidates = set()
    for i in range(len(b)):
        for digit in '012':
            if b[i] != digit:
                candidate = b[:i] + digit + b[i+1:]
                ternary_candidates.add(ternary_to_decimal(candidate))
    
    # 공통된 값 찾기
    for candidate in binary_candidates:
        if candidate in ternary_candidates:
            return candidate

# 예제
a = "0110"
b = "102"
result = find_original_number(a, b)
print(result)  # 출력: N의 값