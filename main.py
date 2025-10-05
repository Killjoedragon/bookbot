def get_book_text(filepath):
	with open (filepath) as f: 
		text = f.read()
		return text
def main():
	Frank = get_book_text("books/frankenstein.txt")
	print(Frank)

main()
