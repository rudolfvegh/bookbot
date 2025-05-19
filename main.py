from stats import word_count

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path="books/frankenstein.txt"
    book=get_book_text(book_path)
    word_number=word_count(book)
    return print(f"{word_number} words found in the document")

main()