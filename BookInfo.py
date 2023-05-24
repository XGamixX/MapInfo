from deep_translator import GoogleTranslator
import random
import json
import argparse

global questions_1
global questions_2
global questions_3
questions_1 = []
questions_2 = []
questions_3 = []

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

def findWrongAuthor (correctAuthor):
    try:
        WrongAuthor = (books[randrange(1, int(len(books))) - 1][2])
    except:
        WrongAuthor = findWrongAuthor(correctAuthor)

    if WrongAuthor == correctAuthor:
        WrongAuthor = findWrongAuthor(correctAuthor)

    return(WrongAuthor)

for bookNR, book in enumerate(books):
    BookName = book[1]
    questions_1.append([BookName])
    questions_2.append([BookName])
    questions_3.append([BookName])
    #1: author [2]
    #2: publisher [11]
    #3: page count [7], publish date [10]
    correctAnswer_author = book[2]
    WrongAuthor1 = findWrongAuthor(correctAnswer_author)
    WrongAuthor2 = findWrongAuthor(correctAnswer_author)
    WrongAuthor3 = findWrongAuthor(correctAnswer_author)
    WrongAuthor4 = findWrongAuthor(correctAnswer_author)
    question = 'Wer hat "' + BookName + '" geschrieben?'
    append_1(bookNR, question, correctAnswer_author, WrongAuthor1, WrongAuthor2, WrongAuthor3, WrongAuthor4)

Parser = argparse.ArgumentParser()
Parser.add_argument("-f", "--folder", required=True)
Folder = Parser.parse_args().folder

with open(Folder + "questions_1_save.json", "w") as questions_1_save_file:
    json.dump(questions_1, questions_1_save_file)
with open(Folder + "questions_2_save.json", "w") as questions_2_save_file:
    json.dump(questions_2, questions_2_save_file)
with open(Folder + "questions_3_save.json", "w") as questions_3_save_file:
    json.dump(questions_3, questions_3_save_file)