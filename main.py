import sys

from stats import (
    word_count, 
    character_count, 
    sorted_list
)

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    book=get_book_text(book_path)
    word_number=word_count(book)
    character_dictionary=character_count(book)
    final_list = sorted_list(character_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_number} total words")
    print("--------- Character Count -------")
    for a in final_list:
        if a["char"].isalpha() == True:
            print(f"{a["char"]}: {a["num"]}")
    print("============= END ===============")

main()