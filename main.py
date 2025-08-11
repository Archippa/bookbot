import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_chars
from stats import sorted_num_chars

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_number = get_num_words(text)
    char_number = get_num_chars(text)
    sorted_chars = sorted_num_chars(char_number)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_path)
    print("----------- Word Count ----------")
    print("Found", word_number, "total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()
