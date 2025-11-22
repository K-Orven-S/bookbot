def count_words(text):
    return len(text.split())

def count_char(text):
    result = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in result:
            result[char_lower] += 1
        else:
            result[char_lower] = 1
    return result

def sort_on(items):
    return items["num"]

def sort_items(char_dict):
    new_list = []
    for key in char_dict:
        dict_pair = {"char": key, "num": char_dict[key]}
        new_list.append(dict_pair)
    new_list.sort(reverse=True, key=sort_on)
    return new_list