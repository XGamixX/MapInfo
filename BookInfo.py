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

def append_1 (bookNR, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4):
    global questions_1
    questions_1[bookNR].append([question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4])

def append_2 (bookNR, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4):
    global questions_2
    questions_2[bookNR].append([question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4])

def append_3 (bookNR, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4):
    global questions_3
    questions_3[bookNR].append([question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4])

for bookNR, book in enumerate(books):
    BookName = book[0]
    global questions_1
    global questions_2
    global questions_3