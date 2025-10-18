def get_book_text(book_path):
        with open (book_path) as f:
                return f.read()
def count_letters(text):
	letters = {}
	lowered = text.lower()
	for ch in lowered:
		letters[ch] = letters.get(ch, 0) +1
	return letters
def count_words(text):
	return len(text.split())
def sort_on(item):
	return item["num"]

