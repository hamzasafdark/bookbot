def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    generate_report(count_letters(text))



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = text.lower()
    letter_mapping = {}
    count = 0

    for c in [*letters]:
        try:
            letter_mapping[c] += 1
        except:
            letter_mapping[c] = 1

def generate_report(data):
    

    return letter_mapping

    
main()

