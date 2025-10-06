# python
import sys
from stats import count_words, count_chars, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")

    counts = count_chars(text)
    sorted_counts = sort_char_counts(counts)

    for entry in sorted_counts:
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()