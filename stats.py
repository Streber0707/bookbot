def word_count(book_text):
    words = book_text.split()
    count = len(words)
    return count
    
def char_count(book_text):
    low_book_text = book_text.lower()
    char_dict = {}
    for character in low_book_text:
        if character not in char_dict:
            char_dict[character] = 1
        elif character in char_dict:
            char_dict[character] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict_list(char_dict):
    char_list = []
    for character in char_dict:
        character_count = char_dict[character]
        reformated_dict ={"char": character, "num": character_count}
        char_list.append(reformated_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
