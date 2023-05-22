import numpy
import random
import json
import pygame
import pygame_widgets
from pygame_widgets.button import Button

def randrange(start, end):
    end += 1
    if start == end:
        return(start)
    return(random.randrange(start, end))

def importStuff ():
    with open("questions_1_save.json", "r") as questions_1_save_file:
        global questions_1
        questions_1 = json.load(questions_1_save_file)
    with open("questions_2_save.json", "r") as questions_2_save_file:
        global questions_2
        questions_2 = json.load(questions_2_save_file)
    with open("questions_3_save.json", "r") as questions_3_save_file:
        global questions_3
        questions_3 = json.load(questions_3_save_file)

    with open("countries_DE_save.json", "r") as countries_DE_save_file:
        global countries_DE
        countries_DE = json.load(countries_DE_save_file)
    with open("countries_EN_save.json", "r") as countries_EN_save_file:
        global countries_EN
        countries_EN = json.load(countries_EN_save_file)
    with open("countries_NATIVE_save.json", "r") as countries_NATIVE_save_file:
        global countries_NATIVE
        countries_NATIVE = json.load(countries_NATIVE_save_file)
    with open("countries_SHORT_save.json", "r") as countries_SHORT_save_file:
        global countries_SHORT
        countries_SHORT = json.load(countries_SHORT_save_file)

def createNumpy ():
    global countries_DE_np
    global countries_EN_np
    global countries_NATIVE_np
    global countries_SHORT_np
    countries_DE_np = numpy.array(countries_DE)
    countries_EN_np = numpy.array(countries_EN)
    countries_NATIVE_np = numpy.array(countries_NATIVE)
    countries_SHORT_np = numpy.array(countries_SHORT)

importStuff()
createNumpy()

def merge_colors (color1, color2):
    return([i+j for i,j in zip(color1, color2)])

BLACK = (0, 0, 0)
LIGHTGREY = (63, 63, 63)
DARKGREY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
LIGHT_RED = (127, 0, 0)
LIGHT_GREEN = (0, 127, 0)
LIGHT_BLUE = (0, 127, 0)

YELLOW = merge_colors(RED,GREEN)
MAGENTA = merge_colors(RED, BLUE)
CYAN = merge_colors(GREEN, BLUE)

ORANGE = merge_colors(RED, LIGHT_GREEN)
LIME = merge_colors(GREEN, LIGHT_RED)
SPRINGGREEN = merge_colors(GREEN, LIGHT_BLUE)
OCEAN = merge_colors(BLUE, LIGHT_GREEN)
VIOLET = merge_colors(BLUE, LIGHT_RED)
ROSE = merge_colors(RED, LIGHT_BLUE)

pygame.init() # pygame setup

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FONTSIZE = 20
TEXTSIZE = FONTSIZE + 3
HSPACING = 8
VSPACING = 6

Font = pygame.font.SysFont('timesnewroman',  FONTSIZE)

pygame.display.set_caption("MapInfo")

buttonAnswer1 = Button(
    screen, 0+VSPACING/2, 200-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion(1)
)

buttonAnswer2 = Button(
    screen, SCREEN_WIDTH/2+VSPACING/2, 200-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion(2)
)

buttonAnswer3 = Button(
    screen, 0+VSPACING/2, 250-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion(3)
)

buttonAnswer4 = Button(
    screen, SCREEN_WIDTH/2+VSPACING/2, 250-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion(4)
)

global QuestionCount
QuestionCount = 0

def wrongAnswers (countryNR, questionNR, questionDifficulty):
    global Answer1Text_text
    global Answer2Text_text
    global Answer3Text_text
    global Answer4Text_text
    if questionDifficulty == 1:
        Answer1Text_text = ("Antwort 1: " + questions_1[countryNR][questionNR][2])
        Answer2Text_text = ("Antwort 2: " + questions_1[countryNR][questionNR][3])
        Answer3Text_text = ("Antwort 3: " + questions_1[countryNR][questionNR][4])
        Answer4Text_text = ("Antwort 4: " + questions_1[countryNR][questionNR][5])
    if questionDifficulty == 2:
        Answer1Text_text = ("Antwort 1: " + questions_2[countryNR][questionNR][2])
        Answer2Text_text = ("Antwort 2: " + questions_2[countryNR][questionNR][3])
        Answer3Text_text = ("Antwort 3: " + questions_2[countryNR][questionNR][4])
        Answer4Text_text = ("Antwort 4: " + questions_2[countryNR][questionNR][5])
    if questionDifficulty == 3:
        Answer1Text_text = ("Antwort 1: " + questions_3[countryNR][questionNR][2])
        Answer2Text_text = ("Antwort 2: " + questions_3[countryNR][questionNR][3])
        Answer3Text_text = ("Antwort 3: " + questions_3[countryNR][questionNR][4])
        Answer4Text_text = ("Antwort 4: " + questions_3[countryNR][questionNR][5])

def Answer1_right (countryNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 1
    global Answer1Text_text
    if questionDifficulty == 1:
        Answer1Text_text = ("Antwort 1: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer1Text_text = ("Antwort 1: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer1Text_text = ("Antwort 1: " + questions_3[countryNR][questionNR][1])

def Answer2_right (countryNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 2
    global Answer2Text_text
    if questionDifficulty == 1:
        Answer2Text_text = ("Antwort 2: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer2Text_text = ("Antwort 2: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer2Text_text = ("Antwort 2: " + questions_3[countryNR][questionNR][1])

def Answer3_right (countryNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 3
    global Answer3Text_text
    if questionDifficulty == 1:
        Answer3Text_text = ("Antwort 3: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer3Text_text = ("Antwort 3: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer3Text_text = ("Antwort 3: " + questions_3[countryNR][questionNR][1])

def Answer4_right (countryNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 4
    global Answer4Text_text
    if questionDifficulty == 1:
        Answer4Text_text = ("Antwort 4: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer4Text_text = ("Antwort 4: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer4Text_text = ("Antwort 4: " + questions_3[countryNR][questionNR][1])

def NewQuestion (answerNR):
    global countries_DE
    global countries_EN
    global countries_NATIVE
    global countries_SHORT
    global points
    if correctAnswer == answerNR and answerNR!=0:
        points += 1
        print(points)
    try:
        countryNR = randrange(0, int(len(countries_DE))) - 1
        questionDifficulty = randrange(0, 3)
        if questionDifficulty == 1:
            questionNR = randrange(1, (int(len(questions_1[countryNR])) - 1))
        if questionDifficulty == 2:
            questionNR = randrange(1, (int(len(questions_2[countryNR])) - 1)) 
        if questionDifficulty == 3:
            questionNR = randrange(1, (int(len(questions_3[countryNR])) - 1))

        global QuestionCount
        QuestionCount += 1

        wrongAnswers(countryNR, questionNR, questionDifficulty)

        random.choice([Answer1_right, Answer2_right, Answer3_right, Answer4_right])(countryNR, questionNR, questionDifficulty)

        global TitleText
        global QuestionNRText
        global CountryText
        global QuestionText
        global Answer1Text
        global Answer2Text
        global Answer3Text
        global Answer4Text
        TitleText=Font.render("Länder Quiz!!!!!!!", False, BLACK, WHITE)
        QuestionNRText_text = str(QuestionCount) + ". Frage!!!!!!!!!!"
        QuestionNRText=Font.render(QuestionNRText_text, False, BLACK, WHITE)
        CountryText_text = ("DE: " + countries_DE[countryNR] + ", EN: " + countries_EN[countryNR] + ", Native: " + countries_NATIVE[countryNR] + ", Short: " + countries_SHORT[countryNR])
        CountryText=Font.render(CountryText_text, False, BLACK, WHITE)
        if questionDifficulty == 1:
            QuestionText_text = questions_1[countryNR][questionNR][0]
        if questionDifficulty == 2:
            QuestionText_text = questions_2[countryNR][questionNR][0]
        if questionDifficulty == 3:
            QuestionText_text = questions_3[countryNR][questionNR][0]
        QuestionText=Font.render(QuestionText_text, False, BLACK, WHITE)
        Answer1Text=Font.render(Answer1Text_text, False, BLACK, WHITE)
        Answer2Text=Font.render(Answer2Text_text, False, BLACK, WHITE)
        Answer3Text=Font.render(Answer3Text_text, False, BLACK, WHITE)
        Answer4Text=Font.render(Answer4Text_text, False, BLACK, WHITE)
    except:
        QuestionCount -=1
        NewQuestion(answerNR)

running = True

i = 0

points = 0

correctAnswer = 0
NewQuestion(0)

while running:

    i += 1

    events = pygame.event.get()
    for event in events: # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close the window
            running = False

    screen.fill("Lime") # fill the screen with a color to wipe away anything from last frame

    #### start of renderer

    pygame_widgets.update(events)

    screen.blit(TitleText, (0, 0))
    screen.blit(QuestionNRText, (0, 50))
    screen.blit(CountryText, (0, 100))
    screen.blit(QuestionText, (0, 150))
    screen.blit(Answer1Text, (0+15, 200))
    screen.blit(Answer2Text, (SCREEN_WIDTH/2+15, 200))
    screen.blit(Answer3Text, (00+15, 250))
    screen.blit(Answer4Text, (SCREEN_WIDTH/2+15, 250))

    pygame.display.update()

    #### end of renderer

    pygame.time.wait(10)

pygame.quit()
