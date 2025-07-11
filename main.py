from stats import count_words
from stats import count_characters
from stats import sort_character_counts
import sys
import os

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    text = get_book_text()
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    letters = sorted([c.lower() for c in text if c.lower() in 'abcdefghijklmnopqrstuvwxyz'])
    for item in sort_character_counts(count_characters(text)):
        print(f"{item['char']}: {item['num']}")

main()