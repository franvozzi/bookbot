# BookBot

## Description
BookBot is a Python program that analyzes a text file (book) and reports the total number of words and the frequency of each letter (a-z) in the book, sorted from most to least frequent.

## Requirements
- Python 3.x

## Usage
1. Place your book files (plain text, UTF-8) in a directory, e.g., `books/`.
2. Run the program from the command line:

```sh
python3 main.py <path_to_book>
```

**Example:**
```sh
python3 main.py books/frankenstein.txt
```

If you do not provide a file path, the program will print:
```
Usage: python3 main.py <path_to_book>
```

## Output
The program will print:
- The total number of words in the book
- The count of each letter (a-z), sorted from most to least frequent, e.g.:

```
Found 75767 total words
e: 44538
t: 29493
a: 25894
...
``` 