def count_words(text):
    return len(text.split())

def count_characters(text):
    from bisect import bisect_left, bisect_right

    # Only count English alphabet letters (a-z)
    letters = sorted([c.lower() for c in text if c.lower() in 'abcdefghijklmnopqrstuvwxyz'])
    unique_letters = sorted(set(letters))
    counts = {}

    for letter in unique_letters:
        left = bisect_left(letters, letter)
        right = bisect_right(letters, letter)
        counts[letter] = right - left

    return counts

def sort_character_counts(counts):
    # Create a list of dictionaries from the counts dict
    char_list = [{"char": char, "num": num} for char, num in counts.items()]
    # Sort the list by 'num' in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

