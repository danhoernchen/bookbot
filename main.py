def main ():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
        word_count = wordCount(book_contents)
        char_count = charCount(book_contents)
        print("--- Beginn report of books/frankensteint.txt ---")
        print(f"{word_count} words found in the book\n")
        for char in char_count:
            print(f"The character {char['char']} was found {char['count']} times.")
        print("--- End report ---")
            



def wordCount(book):
    book = book.split()
    return len(book)

def charCount(book):
    char_count = {}
    for word in book:
        for char in word:
            if char.isalpha():
                if char.lower() not in char_count:
                    char_count[char.lower()] = 1
                else:
                    char_count[char.lower()] += 1
    char_count = sortCharacters(char_count)
    return char_count

def sortCharacters(char_dict):
    char_list = []
    for key,value in char_dict.items():
        current = {"char" : key, "count" : value}
        char_list.append(current)
    char_list.sort(reverse=True, key=getCharValue)
    return char_list
    
def getCharValue(char_dict):
    return char_dict["count"]

    

main()