def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    character_count.sort(key=sort_on, reverse=True)
    print(f"{word_count} words found in this document")
    for item in character_count:
        print(f"the character {item['char']} was found {item['count']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words =  text.split()
    return len(words)

def count_characters(text):
    lower_case = text.lower()
    char = list(lower_case)
    char_count = {}
    char_list = []
    for c in char:
        if c.isalpha():
            char_count[c] = char_count.get(c, 0) + 1

    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_on(dict):
    return dict["count"]
    
    char_list.sort(key=sort_on, reverse=True)

main()