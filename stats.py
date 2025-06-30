def get_book_words(book_text):
    number_of_words = len(book_text.split())
    return number_of_words

def count_char(book_text):
    lower_case = book_text.lower()
    letters = {}
    for letter in lower_case:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters

def sort_on(items):
    for key in items:
        value = items[key]
    return value

def sort_list(char_dict):
    char_list_of_dic = []
    for key in char_dict:
        one_char_dic = {}
        one_char_dic[key] = char_dict[key]
        char_list_of_dic.append(one_char_dic)
    sorted_list = char_list_of_dic.sort(reverse=True, key=sort_on)
    return char_list_of_dic

