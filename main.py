def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letters_dict = count_letters(text)
    letters_sorted_list = letters_dict_to_sorted_list(letters_dict)
    
    print('--- Begin report of %s ---\n %i words froun in the document\n\n' % (book_path, word_count))

    for item in letters_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print('--- End report ---')



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_mapping = {}

    for c in text:
        lowerc = c.lower()
        if lowerc in letter_mapping:
             letter_mapping[lowerc] += 1
        else:
            letter_mapping[lowerc] = 1

    return letter_mapping

def sort_on(d):
    return d["num"]


def letters_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

