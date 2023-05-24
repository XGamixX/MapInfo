from deep_translator import GoogleTranslator
import random
import json

def randrange(start, end):
    end += 1
    if start == end:
        return(start)
    return(random.randrange(start, end))

with open("books.json", "r", encoding="utf-8") as books_file:
    global books
    books = json.load(books_file)

for book in books:
    BookName = book[0]