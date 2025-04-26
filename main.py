from stats import get_book_text
from stats import get_num_words
from stats import get_char_dictionary
from stats import get_clean_sorted_char_list_by_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    num_words = get_num_words(get_book_text(path_to_file))
    dictionary = get_char_dictionary(get_book_text(path_to_file))
    sorted_char_list = get_clean_sorted_char_list_by_count(dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        print(f"{i}: {dictionary[i]}")
    print("============= END ===============")

main()