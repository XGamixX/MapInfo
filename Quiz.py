import random
import json
import pygame
import pygame_widgets
import argparse
from pygame_widgets.button import Button

def randrange(start, end):
    end += 1
    if start == end:
        return(start)
    return(random.randrange(start, end))

Parser = argparse.ArgumentParser()
Parser.add_argument("-f", "--folder", required=False)
Parser.add_argument("-n", "--name", required=False)
Folder = Parser.parse_args().folder
if not os.path.exists(Folder):
    os.makedirs(Folder)
QuizName = Parser.parse_args().name

def importStuff ():
    with open(Folder + "questions_1_save.json", "r", encoding="utf-8") as questions_1_save_file:
        global questions_1
        questions_1 = json.load(questions_1_save_file)
    with open(Folder + "questions_2_save.json", "r", encoding="utf-8") as questions_2_save_file:
        global questions_2
        questions_2 = json.load(questions_2_save_file)
    with open(Folder + "questions_3_save.json", "r", encoding="utf-8") as questions_3_save_file:
        global questions_3
        questions_3 = json.load(questions_3_save_file)

importStuff()

def merge_colors (color1, color2):
    return([i+j for i,j in zip(color1, color2)])

BLACK = (0, 0, 0)
LIGHTGREY = (63, 63, 63)
GREY = (127, 127, 127)
DARKGREY = (191, 191, 191)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_RED = (127, 0, 0)
LIGHT_GREEN = (0, 127, 0)
LIGHT_BLUE = (0, 0, 127)

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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
FONTSIZE = 20
TEXTSIZE = FONTSIZE + 3
HSPACING = 8
VSPACING = 6

Font = pygame.font.SysFont('timesnewroman',  FONTSIZE)

pygame.display.set_caption(QuizName + " Quiz")

INACTIVE_COLOR=BLUE
HOVER_COLOR=VIOLET
PRESSED_COLOR=ROSE

buttonAnswer1 = Button(
    screen, 0+VSPACING/2, 150-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=INACTIVE_COLOR,
    hoverColour=HOVER_COLOR,
    pressedColour=PRESSED_COLOR, radius=20,
    onClick=lambda: NewQuestion(1)
)
buttonAnswer2 = Button(
    screen, SCREEN_WIDTH/2+VSPACING/2, 150-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=INACTIVE_COLOR,
    hoverColour=HOVER_COLOR,
    pressedColour=PRESSED_COLOR, radius=20,
    onClick=lambda: NewQuestion(2)
)

buttonAnswer3 = Button(
    screen, 0+VSPACING/2, 200-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=INACTIVE_COLOR,
    hoverColour=HOVER_COLOR,
    pressedColour=PRESSED_COLOR, radius=20,
    onClick=lambda: NewQuestion(3)
)

buttonAnswer4 = Button(
    screen, SCREEN_WIDTH/2+VSPACING/2, 200-15+HSPACING/2, SCREEN_WIDTH/2-VSPACING, TEXTSIZE+15*2-HSPACING,
    fontSize=50, margin=20,
    inactiveColour=INACTIVE_COLOR,
    hoverColour=HOVER_COLOR,
    pressedColour=PRESSED_COLOR, radius=20,
    onClick=lambda: NewQuestion(4)
)

def updateButtons ():
    global buttonAnswer1
    global buttonAnswer2
    global buttonAnswer3
    global buttonAnswer4
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    SCREEN_WIDTH = screen.get_rect()[2]
    SCREEN_HEIGHT = screen.get_rect()[3]
    buttons = [buttonAnswer1, buttonAnswer2, buttonAnswer3, buttonAnswer4]
    for button in buttons:
        button.setWidth(SCREEN_WIDTH/2-VSPACING)
    buttons = [buttonAnswer2, buttonAnswer4]
    for button in buttons:
        button.setX(SCREEN_WIDTH/2+VSPACING/2)
    

global QuestionCount
QuestionCount = 0

def wrongAnswers (itemNR, questionNR, questionDifficulty):
    global Answer1Text_text
    global Answer2Text_text
    global Answer3Text_text
    global Answer4Text_text
    if questionDifficulty == 1:
        Answer1Text_text = ("Antwort 1: " + questions_1[itemNR][questionNR][2])
        Answer2Text_text = ("Antwort 2: " + questions_1[itemNR][questionNR][3])
        Answer3Text_text = ("Antwort 3: " + questions_1[itemNR][questionNR][4])
        Answer4Text_text = ("Antwort 4: " + questions_1[itemNR][questionNR][5])
    if questionDifficulty == 2:
        Answer1Text_text = ("Antwort 1: " + questions_2[itemNR][questionNR][2])
        Answer2Text_text = ("Antwort 2: " + questions_2[itemNR][questionNR][3])
        Answer3Text_text = ("Antwort 3: " + questions_2[itemNR][questionNR][4])
        Answer4Text_text = ("Antwort 4: " + questions_2[itemNR][questionNR][5])
    if questionDifficulty == 3:
        Answer1Text_text = ("Antwort 1: " + questions_3[itemNR][questionNR][2])
        Answer2Text_text = ("Antwort 2: " + questions_3[itemNR][questionNR][3])
        Answer3Text_text = ("Antwort 3: " + questions_3[itemNR][questionNR][4])
        Answer4Text_text = ("Antwort 4: " + questions_3[itemNR][questionNR][5])

def Answer1_right (itemNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 1
    global Answer1Text_text
    if questionDifficulty == 1:
        Answer1Text_text = ("Antwort 1: " + questions_1[itemNR][questionNR][1])
    if questionDifficulty == 2:
        Answer1Text_text = ("Antwort 1: " + questions_2[itemNR][questionNR][1])
    if questionDifficulty == 3:
        Answer1Text_text = ("Antwort 1: " + questions_3[itemNR][questionNR][1])

def Answer2_right (itemNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 2
    global Answer2Text_text
    if questionDifficulty == 1:
        Answer2Text_text = ("Antwort 2: " + questions_1[itemNR][questionNR][1])
    if questionDifficulty == 2:
        Answer2Text_text = ("Antwort 2: " + questions_2[itemNR][questionNR][1])
    if questionDifficulty == 3:
        Answer2Text_text = ("Antwort 2: " + questions_3[itemNR][questionNR][1])

def Answer3_right (itemNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 3
    global Answer3Text_text
    if questionDifficulty == 1:
        Answer3Text_text = ("Antwort 3: " + questions_1[itemNR][questionNR][1])
    if questionDifficulty == 2:
        Answer3Text_text = ("Antwort 3: " + questions_2[itemNR][questionNR][1])
    if questionDifficulty == 3:
        Answer3Text_text = ("Antwort 3: " + questions_3[itemNR][questionNR][1])

def Answer4_right (itemNR, questionNR, questionDifficulty):
    global correctAnswer
    correctAnswer = 4
    global Answer4Text_text
    if questionDifficulty == 1:
        Answer4Text_text = ("Antwort 4: " + questions_1[itemNR][questionNR][1])
    if questionDifficulty == 2:
        Answer4Text_text = ("Antwort 4: " + questions_2[itemNR][questionNR][1])
    if questionDifficulty == 3:
        Answer4Text_text = ("Antwort 4: " + questions_3[itemNR][questionNR][1])

def NewQuestion (answerNR):
    global points
    global PointsText
    if correctAnswer == answerNR and answerNR!=0:
        points += 1
        PointsText_text = str(points) + " Punkte"
        PointsText=Font.render(PointsText_text, False, BLACK, WHITE)
    try:
        itemNR = randrange(0, int(len(questions_1))) - 1
        questionDifficulty = randrange(0, 3)
        if questionDifficulty == 1:
            questionNR = randrange(1, (int(len(questions_1[itemNR])) - 1))
        if questionDifficulty == 2:
            questionNR = randrange(1, (int(len(questions_2[itemNR])) - 1)) 
        if questionDifficulty == 3:
            questionNR = randrange(1, (int(len(questions_3[itemNR])) - 1))

        global QuestionCount
        QuestionCount += 1

        wrongAnswers(itemNR, questionNR, questionDifficulty)

        random.choice([Answer1_right, Answer2_right, Answer3_right, Answer4_right])(itemNR, questionNR, questionDifficulty)

        global TitleText
        global QuestionNRText
        global CountryText
        global QuestionText
        global Answer1Text
        global Answer2Text
        global Answer3Text
        global Answer4Text
        TitleText=Font.render(QuizName + " Quiz!!!!!!!", False, BLACK, WHITE)
        QuestionNRText_text = str(QuestionCount) + ". Frage!!!!!!!!!!"
        QuestionNRText=Font.render(QuestionNRText_text, False, BLACK, WHITE)
        if questionDifficulty == 1:
            QuestionText_text = questions_1[itemNR][questionNR][0]
        if questionDifficulty == 2:
            QuestionText_text = questions_2[itemNR][questionNR][0]
        if questionDifficulty == 3:
            QuestionText_text = questions_3[itemNR][questionNR][0]
        QuestionText=Font.render(QuestionText_text, False, BLACK, WHITE)
        Answer1Text=Font.render(Answer1Text_text, False, BLACK, WHITE)
        Answer2Text=Font.render(Answer2Text_text, False, BLACK, WHITE)
        Answer3Text=Font.render(Answer3Text_text, False, BLACK, WHITE)
        Answer4Text=Font.render(Answer4Text_text, False, BLACK, WHITE)
    except:
        QuestionCount -=1
        NewQuestion(0)

running = True

i = 0

points = 0
PointsText_text = str(points) + " Punkte"
PointsText=Font.render(PointsText_text, False, BLACK, WHITE)

correctAnswer = 0
NewQuestion(0)

while running:

    i += 1

    events = pygame.event.get()
    for event in events: # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close the window
            running = False

    screen.fill(MAGENTA) # fill the screen with a color to wipe away anything from last frame

    #### start of renderer
    updateButtons()
    pygame_widgets.update(events)

    screen.blit(TitleText, (0, 0))
    screen.blit(QuestionNRText, (0, 50))
    screen.blit(QuestionText, (0, 100))
    screen.blit(Answer1Text, (0+15, 150))
    screen.blit(Answer2Text, (SCREEN_WIDTH/2+VSPACING/2+15, 150))
    screen.blit(Answer3Text, (00+15, 200))
    screen.blit(Answer4Text, (SCREEN_WIDTH/2+VSPACING/2+15, 200))
    screen.blit(PointsText, (SCREEN_WIDTH - 100, 0))

    pygame.display.update()

    #### end of renderer

    pygame.time.wait(10)

pygame.quit()
