from stats import count_words, count_char, sort_items
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

if len(sys.argv) == 2:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_char(book_text)
    word_count_list = sort_items(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in word_count_list:
        if item["char"].isalpha() == False:
            continue
        print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()