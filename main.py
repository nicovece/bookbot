import sys
from stats import words_count, chars_count, special_chars_count
args = sys.argv

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(book_path):
    book_text = get_book_text(book_path)
    print("=" *12 + " BOOKBOT " + "=" *12)
    print(f"Analyzing book found at {book_path}")
    print("-" *12 + " Word Count " + "-" *12)
    print(words_count(book_text)) 
    print("-" *12 + " Character Count " + "-" *12)
    chars_dict = chars_count(book_text)
    print(special_chars_count(chars_dict))
    print("=" *12 + " END " + "=" *12)

if len(sys.argv) == 2:
    main(args[1])
    sys.exit(0)
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
