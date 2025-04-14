# 2.4 "Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.

text = "Python is awesome"

vowels = "aeiouAEIOU"

count = 0
for char in text:
    if char in vowels:
        count += 1

print("모음 개수 :", count)