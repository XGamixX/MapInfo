from deep_translator import GoogleTranslator
import random
import json

with open("books.json", "r", encoding="utf-8") as books_file:
    global books
    books = json.load(books_file)
