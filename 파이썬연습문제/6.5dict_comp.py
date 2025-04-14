# 6.5 ["apple", "banana", "cherry"]에서 각 단어의 길이를 딕셔너리로 만드세요.

words = ["apple", "banana", "cherry"]

word_lengths = {word: len(word) for word in words}

print(word_lengths)