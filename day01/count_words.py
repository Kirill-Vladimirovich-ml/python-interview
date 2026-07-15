import re

def count_words(text):
    word_dict = {}
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    words = text.split()
    
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
        
    return word_dict

text = "hello world Hello, python world hello"
print(count_words(text))
