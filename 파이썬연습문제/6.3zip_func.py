# 6.3 두 리스트 [1, 2, 3]과 [10, 20, 30]의 요소들을 짝지어 출력하세요.

list1 = [1, 2, 3]
list2 = [10, 20, 30]

for a, b in zip(list1, list2):
    print(a, b)