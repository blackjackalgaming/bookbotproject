import sys
from stats import get_num_words, count_words, get_top_words, count_characters, sort_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book> [title] [author]")
        sys.exit(1)

    book_path = sys.argv[1]

    if len(sys.argv) >= 4:
        book_title = sys.argv[2]
        book_author = sys.argv[3]
    else:
        book_title = "Unknown Title"
        book_author = "Unknown Author"

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    sorted_chars = sort_characters(count_characters(book_text))
    word_counts = count_words(book_text)
    top_words = get_top_words(word_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing '{book_title}' by {book_author}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Top Words -----------")
    for item in top_words:
        print(f"{item['word']}: {item['num']}")
        print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
