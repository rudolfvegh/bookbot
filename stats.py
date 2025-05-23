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

def sort_on(dict):
    return dict["num"]

def sorted_list(char_dict):
    sorted_list=[]
    for s in char_dict:
        helper_dict = {}
        helper_dict["char"] = s
        helper_dict["num"] = char_dict[s]
        sorted_list.append(helper_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    



