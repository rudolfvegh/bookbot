def word_count(text):
    words=text.split()
    return len(words)

def character_count(text):
    lowercase_text=text.lower()
    char_dict={}
    for s in lowercase_text:
        if s in char_dict:
            char_dict[s] += 1
        else:
            char_dict[s] = 1
    return char_dict

