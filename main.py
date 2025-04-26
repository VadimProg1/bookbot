from stats import get_book_text
from stats import get_num_words
from stats import get_char_dictionary
from stats import get_clean_sorted_char_list_by_count

path_to_file = "./books/frankenstein.txt"

def main():
    num_words = get_num_words(get_book_text(path_to_file))
    dictionary = get_char_dictionary(get_book_text(path_to_file))
    sorted_char_list = get_clean_sorted_char_list_by_count(dictionary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        print(f"{i}: {dictionary[i]}")
    print("============= END ===============")
    
main()