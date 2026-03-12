def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


main()
