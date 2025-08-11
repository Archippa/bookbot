def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_chars
from stats import sorted_num_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_number = get_num_words(text)
    char_number = get_num_chars(text)
    sorted_chars = sorted_num_chars(char_number)
    print(word_number, "words found in the document")
    print(sorted_chars)

main()
