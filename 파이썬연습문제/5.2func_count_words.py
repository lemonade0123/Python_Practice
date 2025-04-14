# 5.2 문자열을 인자로 받아 단어 수를 반환하는 count_words 함수를 작성하세요. 

def count_words(sentence):
    words = sentence.split()
    return len(words) 

sentence = "This is a test"

print("단어 수:", count_words(sentence))
