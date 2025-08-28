def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document"

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    print(word_count(book_text))

main()
    
