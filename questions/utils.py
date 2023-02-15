def filter_text(description: str) -> str:
    with open('forbidden_words.txt') as forbidden_words:
        bad_words = forbidden_words.read().split()
        for word in bad_words:
            quantity = text.lower().count(word.lower())
            if word in lower_text:
                for iteration in range(quantity):
                    start = lower_text.find(word)
                    lower_text = lower_text.replace(word,'*'*len(word),1)                        
                    text = text.replace(text[start:start + len(word):], '*'*len(word))
    return text
