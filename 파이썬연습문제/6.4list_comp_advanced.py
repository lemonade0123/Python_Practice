# 6.4 [1, 2, 3, 4, 5]의 각 요소에 10을 더한 후 2로 나눈 결과를 리스트로 생성하세요.

numbers = [1, 2, 3, 4, 5]

result = [(num + 10) / 2 for num in numbers]

print(result)