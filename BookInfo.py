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

def findWrongItem (correctItem, ID):
    try:
        WrongItem = (books[randrange(1, int(len(books))) - 1][ID])
    except:
        WrongItem = findWrongItem(correctItem, ID)

    if WrongItem == correctItem:
        WrongItem = findWrongItem(correctItem, ID)

    return(WrongItem)

for bookNR, book in enumerate(books):
    BookName = book[0]
    questions_1.append([BookName])
    questions_2.append([BookName])
    questions_3.append([BookName])
    #1: author [0]
    #2: publisher [3]
    #3: page count [1], publish date [2]
    correctAnswer_author = book[0]
    WrongAuthor1 = findWrongItem(correctAnswer_author, 0)
    WrongAuthor2 = findWrongItem(correctAnswer_author, 0)
    WrongAuthor3 = findWrongItem(correctAnswer_author, 0)
    WrongAuthor4 = findWrongItem(correctAnswer_author, 0)
    question_author = 'Wer hat "' + BookName + '" geschrieben?'
    append_1(bookNR, question_author, correctAnswer_author, WrongAuthor1, WrongAuthor2, WrongAuthor3, WrongAuthor4)

    correctAnswer_publisher = book[3]
    WrongPublisher1 = findWrongItem(correctAnswer_publisher, 3)
    WrongPublisher2 = findWrongItem(correctAnswer_publisher, 3)
    WrongPublisher3 = findWrongItem(correctAnswer_publisher, 3)
    WrongPublisher4 = findWrongItem(correctAnswer_publisher, 3)
    question_publisher = 'Welcher Verlag hat "' + BookName + '" veröffentlich?'
    append_2(bookNR, question_publisher, correctAnswer_publisher, WrongPublisher1, WrongPublisher2, WrongPublisher3, WrongPublisher4)

    correctAnswer_PageCount = str(book[1])
    WrongPageCount1 = str(findWrongItem(correctAnswer_PageCount, 1))
    WrongPageCount2 = str(findWrongItem(correctAnswer_PageCount, 1))
    WrongPageCount3 = str(findWrongItem(correctAnswer_PageCount, 1))
    WrongPageCount4 = str(findWrongItem(correctAnswer_PageCount, 1))
    question_pageCount = 'Wie viele Seiten hat "' + BookName + '"?'
    append_3(bookNR, question_pageCount, correctAnswer_PageCount, WrongPageCount1, WrongPageCount2, WrongPageCount3, WrongPageCount4)

    correctAnswer_publishDate = book[2]
    WrongPublishDate1 = findWrongItem(correctAnswer_publishDate, 2)
    WrongPublishDate2 = findWrongItem(correctAnswer_publishDate, 2)
    WrongPublishDate3 = findWrongItem(correctAnswer_publishDate, 2)
    WrongPublishDate4 = findWrongItem(correctAnswer_publishDate, 2)
    question_publishDate = 'Wann wurde "' + BookName + '" veröffentlicht?'
    append_3(bookNR, question_publishDate, correctAnswer_publishDate, WrongPublishDate1, WrongPublishDate2, WrongPublishDate3, WrongPublishDate4)

Parser = argparse.ArgumentParser()
Parser.add_argument("-f", "--folder", required=False)
Folder = Parser.parse_args().folder

with open(Folder + "questions_1_save.json", "w") as questions_1_save_file:
    json.dump(questions_1, questions_1_save_file)
with open(Folder + "questions_2_save.json", "w") as questions_2_save_file:
    json.dump(questions_2, questions_2_save_file)
with open(Folder + "questions_3_save.json", "w") as questions_3_save_file:
    json.dump(questions_3, questions_3_save_file)