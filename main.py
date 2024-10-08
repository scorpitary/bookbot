def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(word_count)
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words =  text.split()
    return len(words)

def count_characters(text):
    lower_case = text.lower()
    characters = list(lower_case)
    character_count = {}
    for c in characters:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count




main()