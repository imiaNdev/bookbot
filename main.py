def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def generate_report(word_count, char_count, file_path):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert dictionary to a list of dictionaries
    sorted_char_count = sorted(
        char_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Print character counts
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"

    with open(book_path, "r") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    generate_report(word_count, char_count, book_path)

if __name__ == "__main__":
    main()
