def get_num_of_words(content):
    words = content.split()
    return len(words)

def get_chars_nums(content):
    content = content.lower()
    d = {}
    for char in content:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

def sort_on(items):
    return items["num"]

def sort_dict(d):
    result_list = []
    for key in d:
        new_d = {"char": key, "num": d[key]}
        result_list.append(new_d)
    result_list.sort(reverse=True, key=sort_on)
    return result_list
