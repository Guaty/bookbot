def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    word_count = get_word_count(text)
    # print(f"{word_count} words were in this doc.")
    char_dict = get_char_dict(text)
    char_list = get_sorted_char_list(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in char_list:
        print(f"The '{char["letter"]}' character was found {char["num"]} times")
    print(f"-- End report --")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    lowered_string = text.lower()
    char_counts={}
    
    for character in lowered_string:
        if character not in char_counts:
            char_counts[character] = 1
        else:
            char_counts[character] += 1

    return char_counts

def sort_on(dict):
    return dict["num"]

def get_sorted_char_list(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"letter": char, "num" : char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


main()
