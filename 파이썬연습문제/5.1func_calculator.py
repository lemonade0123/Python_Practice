# 5.1 두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요.

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

nums = [1, 2, 3, 4, 5]
squared_nums = [calculator(num, num, "*") for num in nums]

print(squared_nums)
