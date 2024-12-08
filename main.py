def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    word_count = get_word_count(text)
    # print(f"{word_count} words were in this doc.")
    char_counts = get_char_counts(text)
    print(char_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    lowered_string = text.lower()
    char_counts={}
    
    for character in lowered_string:
        if character not in char_counts:
            char_counts[character] = 1
        else:
            char_counts[character] += 1

    return char_counts


main()
