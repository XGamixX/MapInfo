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
        WrongItem = findWrongItem(correctItem)

    if WrongItem == correctItem:
        WrongItem = findWrongItem(correctItem)

    return(WrongAItem)

for bookNR, book in enumerate(books):
    BookName = book[1]
    questions_1.append([BookName])
    questions_2.append([BookName])
    questions_3.append([BookName])
    #1: author [2]
    #2: publisher [11]
    #3: page count [7], publish date [10]
    correctAnswer_author = book[2]
    WrongAuthor1 = findWrongItem(correctAnswer_author, 2)
    WrongAuthor2 = findWrongItem(correctAnswer_author, 2)
    WrongAuthor3 = findWrongItem(correctAnswer_author, 2)
    WrongAuthor4 = findWrongItem(correctAnswer_author, 2)
    question_author = 'Wer hat "' + BookName + '" geschrieben?'
    append_1(bookNR, question_author, correctAnswer_author, WrongAuthor1, WrongAuthor2, WrongAuthor3, WrongAuthor4)

    correctAnswer_publisher = book[11]
    WrongPublisher1 = findWrongItem(correctAnswer_publisher, 11)
    WrongPublisher2 = findWrongItem(correctAnswer_publisher, 11)
    WrongPublisher3 = findWrongItem(correctAnswer_publisher, 11)
    WrongPublisher4 = findWrongItem(correctAnswer_publisher, 11)
    question_publisher = 'Wer hat "' + BookName + '" geschrieben?'
    append_2(bookNR, question_publisher, correctAnswer_publisher, WrongPublisher1, WrongPublisher2, WrongPublisher3, WrongPublisher4)

    correctAnswer_PageCount = book[7]
    WrongPageCount1 = findWrongItem(correctAnswer_PageCount, 7)
    WrongPageCount2 = findWrongItem(correctAnswer_PageCount, 7)
    WrongPageCount3 = findWrongItem(correctAnswer_PageCount, 7)
    WrongPageCount4 = findWrongItem(correctAnswer_PageCount, 7)
    question_pageCount = 'Wer hat "' + BookName + '" geschrieben?'
    append_3(bookNR, question_pageCount, correctAnswer_PageCount, WrongPageCount1, WrongPageCount2, WrongPageCount3, WrongPageCount4)

    correctAnswer_publishDate = book[10]
    WrongPublishDate1 = findWrongItem(correctAnswer_publishDate, 10)
    WrongPublishDate2 = findWrongItem(correctAnswer_publishDate, 10)
    WrongPublishDate3 = findWrongItem(correctAnswer_publishDate, 10)
    WrongPublishDate4 = findWrongItem(correctAnswer_publishDate, 10)
    question_publishDate = 'Wer hat "' + BookName + '" geschrieben?'
    append_3(bookNR, question_publishDate, correctAnswer_publishDate, WrongPublishDate1, WrongPublishDate2, WrongPublishDate3, WrongPublishDate4)

Parser = argparse.ArgumentParser()
Parser.add_argument("-f", "--folder", required=True)
Folder = Parser.parse_args().folder

with open(Folder + "questions_1_save.json", "w") as questions_1_save_file:
    json.dump(questions_1, questions_1_save_file)
with open(Folder + "questions_2_save.json", "w") as questions_2_save_file:
    json.dump(questions_2, questions_2_save_file)
with open(Folder + "questions_3_save.json", "w") as questions_3_save_file:
    json.dump(questions_3, questions_3_save_file)