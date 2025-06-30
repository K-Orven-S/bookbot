from stats import get_book_words
from stats import count_char
from stats import sort_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text(sys.argv[1])
    book_words = get_book_words(text)
    word_count = count_char(text)
    sorted_list = sort_list(word_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        for key in item:
            if key.isalpha():
                print(f"{key}: {item[key]}")
            else:
                pass
    print("============= END ===============")
 
main()
