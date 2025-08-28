def words_count(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def chars_count(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars

def get_num(dictionary):
    return dictionary["num"]

def special_chars_count(char_dict):
    chars_to_sort = []
    lines = []
    for char, count in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            chars_to_sort.append(new_dict)
    chars_to_sort.sort(key=get_num, reverse=True)
    for dict in chars_to_sort:
        lines.append(f"{dict['char']}: {dict['num']}")
    return "\n".join(lines)
