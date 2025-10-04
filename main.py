import sys

from stats import get_num_of_words
from stats import get_chars_nums
from stats import sort_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    contents = get_book_contents(book_path)
    num_words = get_num_of_words(contents)
    char_nums = get_chars_nums(contents)
    sorted_dict = sort_dict(char_nums)
    print_result(num_words, sorted_dict, book_path)


def get_book_contents(filepath):
    with open(filepath) as f:
        return f.read()

def print_result(word_count, character_count, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in character_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()