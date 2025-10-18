import sys
from stats import get_book_text, count_words, count_letters, sort_on
if  len(sys.argv) != 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
book_path = sys.argv[1]
Book = get_book_text(book_path)

letters = count_letters(Book)
num_words = count_words(Book)

stats_list = []
for ch, count in letters.items():
    if ch.isalpha():
        stats_list.append({"char": ch, "num": count})
stats_list.sort(reverse=True, key=sort_on)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for item in stats_list:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")
