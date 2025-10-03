import sys
from stats import get_num_words, get_char_count, get_sorted_list

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    frankenstein_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    total_num_words = get_num_words(frankenstein_text)
    print(f"Found {total_num_words} total words")
    count_map = get_char_count(frankenstein_text)
    count_list = get_sorted_list(count_map)
    print("--------- Character Count -------")    
    for char_dict in count_list:
        char, num = char_dict["char"], char_dict["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("============= END ===============")
if __name__ == "__main__":
    main()