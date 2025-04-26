def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dictionary(text):
    dictionary = {}
    for i in range(0, len(text)):
        char = text[i].lower();
        if char in dictionary.keys():
            dictionary[char] += 1
        else: 
            dictionary[char] = 1

    return dictionary

def sort_on(dict):
    return dict

def get_clean_sorted_char_list_by_count(dictionary):
    s_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    result_list = []
    
    for item in s_list:
        if item[0].isalpha():
            result_list.append(item[0])

    return result_list
