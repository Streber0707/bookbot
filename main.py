import sys
from stats import word_count, char_count, sort_dict_list

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_chars_dict = char_count(book)
    num_words = word_count(book)
    num_chars = sort_dict_list(num_chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in num_chars:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

main()
