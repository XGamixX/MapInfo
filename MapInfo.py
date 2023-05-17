reloadQuestions = False

"""
pip install countryinfo
pip install pycountry
pip install deep_translator
pip install numpy
pip install pip install emoji-country-flag
pip install pygame
pip install pygame_widgets
""" ##installation der libraries

from countryinfo import CountryInfo
from deep_translator import GoogleTranslator
import pycountry
import numpy
import random
import json
import flag
import pygame
import pygame_widgets
from pygame_widgets.button import Button ##import der libraries

global errors
errors = []
global countryCount
countryCount = len(pycountry.countries)
global countries_DE
global countries_EN
global countries_NATIVE
global countries_SHORT
countries_DE = []
countries_EN = []
countries_NATIVE = []
countries_SHORT = []
global questions_1
global questions_2
global questions_3
questions_1 = []
questions_2 = []
questions_3 = [] ##initialisieren der variablen

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


def loadManualQuestions ():
    global manualQuestions_1
    manualQuestions_1 = []
    global manualQuestions_2
    manualQuestions_2 = []
    global manualQuestions_3
    manualQuestions_3 = [] ##initialisieren der variablen
    try:
        with open("questions_1.json", "r") as questions_1_file:
            manualQuestions_1 = json.load(questions_1_file)
    except:
        pass
    try:
        with open("questions_2.json", "r") as questions_2_file:
            manualQuestions_2 = json.load(questions_2_file)
    except:
        pass
    try:
        with open("questions_3.json", "r") as questions_3_file:
            manualQuestions_3 = json.load(questions_3_file) ##öffnen der dateien
    except:
        pass
    return()

def loadMissingQuestions ():
    global missingQuestions_1
    missingQuestions_1 = []
    global missingQuestions_2
    missingQuestions_2 = []
    global missingQuestions_3
    missingQuestions_3 = [] ##initialisieren der variablen
    try:
        with open("missing_questions_1.json", "r") as missing_questions_1_file:
            missingQuestions_1 = json.load(missing_questions_1_file)
    except:
        pass
    try:
        with open("missing_questions_2.json", "r") as missing_questions_2_file:
            missingQuestions_2 = json.load(missing_questions_2_file)
    except:
        pass
    try:
        with open("missing_questions_3.json", "r") as missing_questions_3_file:
            missingQuestions_3 = json.load(missing_questions_3_file) ##öffnen der dateien
    except:
        pass
    return()

def getCountries ():
    global questions_1
    global questions_2
    global questions_3
    global countries_DE
    global countries_EN
    global countries_NATIVE
    global countries_SHORT
    countries = (list(pycountry.countries)) ##schreiben der länder in eine liste
    i=0
    for country in countries:
        i = i + 1
        try:
            CountryInfo(country.name).area ##try um zu schauen ob Country Info den name kennt
            countryName_EN = country.name ##Normalen Namen nutzen
        except:
            try:
                CountryInfo(country.official_name).area ##try um zu schauen ob Country Info den official name kennt
                countryName_EN = country.official_name ##Offiziellen Namen nutzen
            except:
                countryName_EN = country.name ##Normalen Namen nutzen falls country info das land nicht kennt
        countryName_EN = str(countryName_EN).capitalize()
        countries_EN.append(countryName_EN)
        questions_1.append([countryName_EN])
        questions_2.append([countryName_EN])
        questions_3.append([countryName_EN]) ##an die liste anhängen
        try:
            countryName_DE = CountryInfo(countryName_EN).translations().get("de") ##Nutzen der Country info, die die übersetzungen kennt
        except:
            try:
                countryName_DE = GoogleTranslator(source = "en", target = "de").translate(countryName_EN) ##falls country info das land nicht kennt
            except:
                countryName_DE = "/Error/" 
        countries_DE.append(countryName_DE.capitalize()) ##an die liste anhängen
        try:
            countryName_NATIVE = CountryInfo(countryName_EN).native_name()
        except:
            countryName_NATIVE = "/Error/"
        countries_NATIVE.append(countryName_NATIVE.capitalize()) ##an die liste anhängen
        try:
            countryName_SHORT = CountryInfo(countryName_EN).iso() ##kurzcodes finden
            countryName_SHORT = countryName_SHORT.get("alpha2") ##2er kurzcode finden
        except:
            countryName_SHORT = "/Error/"
        countries_SHORT.append(countryName_SHORT) ##an die liste anhängen

        print("Erfindet Länder... " + str(i) + "/" + str(countryCount))
    return()

def createNumpy ():
    global countries_DE_np
    global countries_EN_np
    global countries_NATIVE_np
    global countries_SHORT_np
    countries_DE_np = numpy.array(countries_DE)
    countries_EN_np = numpy.array(countries_EN)
    countries_NATIVE_np = numpy.array(countries_NATIVE)
    countries_SHORT_np = numpy.array(countries_SHORT)
    return()

def append_1 (countryNR, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4):
    global questions_1
    questions_1[countryNR].append([question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4])

def append_2 (countryNR, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4):
    global questions_2
    questions_2[countryNR].append([question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4])

def append_3 (countryNR, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4):
    global questions_3
    questions_3[countryNR].append([question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4])

def findWrongCapital (correctCapital):
    try:
        WrongCapital = CountryInfo(countries_EN[randrange(1, int(len(countries_EN))) - 1]).capital()
    except:
        WrongCapital = findWrongCapital()

    if WrongCapital == correctCapital:
        WrongCapital = findWrongCapital()

    return(WrongCapital)

def findWrongArea (correctArea):
    try:
        WrongArea = (str(CountryInfo(countries_EN[randrange(1, int(len(countries_EN))) - 1]).area()) + "km²")
    except:
        WrongArea = findWrongArea()

    if WrongArea == correctArea:
        WrongArea = findWrongArea()

    return(WrongArea)

def findWrongPopulation (correctPopulation):
    try:
        WrongPopulation = str(CountryInfo(countries_EN[randrange(1, int(len(countries_EN))) - 1]).population())
    except:
        WrongPopulation = findWrongPopulation()

    if WrongPopulation == correctPopulation:
        WrongPopulation = findWrongPopulation()

    return(WrongPopulation)

def findWrongContinent (correctContinent):
    try:
        wrongID = CountryInfo(countries_EN[randrange(1, int(len(countries_EN))) - 1])
        wrongRegion = wrongID.region()
        wrongSubregion = wrongID.subregion()
        try:
            wrongRegion = GoogleTranslator(source = "en", target = "de").translate(wrongRegion)
            wrongSubregion = GoogleTranslator(source = "en", target = "de").translate(wrongSubregion)
        except:
            pass
        WrongContinent = (wrongRegion + " (" + wrongSubregion + ")")
    except:
        WrongContinent = findWrongContinent()

    if WrongContinent == correctContinent:
        WrongContinent = findWrongContinent()

    return(WrongContinent)

def findInfo ():
    global errors
    countries_EN
    global countries_EN_np
    global countries_DE
    global questions_1
    global questions_2
    global questions_3
    i=0
    for countryName_EN in countries_EN:
        i = i + 1
        countryID = CountryInfo(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN) ##an welcher stelle ist der name im numpy array
        countryNR = countryNR[0][0]
        countryName_DE = countries_DE[countryNR]
        e=0
        try:
            capital = countryID.capital()
            WrongCapital1 = findWrongCapital()
            WrongCapital2 = findWrongCapital()
            WrongCapital3 = findWrongCapital()
            WrongCapital4 = findWrongCapital()
            try:
                capital = GoogleTranslator(source = "en", target = "de").translate(capital)
            except:
                pass
            try:
                WrongCapital1 = GoogleTranslator(source = "en", target = "de").translate(WrongCapital1)
            except:
                pass
            try:
                WrongCapital2 = GoogleTranslator(source = "en", target = "de").translate(WrongCapital2)
            except:
                pass
            try:
                WrongCapital3 = GoogleTranslator(source = "en", target = "de").translate(WrongCapital3)
            except:
                pass
            try:
                WrongCapital4 = GoogleTranslator(source = "en", target = "de").translate(WrongCapital4)
            except:
                pass
            question_capital = ("Wie heißt die Hauptstadt von " + countryName_DE + "?")
            # questions_2[countryNR].append(question_capital + " [Antwort: " + capital + "]")
            append_2(countryNR, question_capital, capital, WrongCapital1, WrongCapital2, WrongCapital3, WrongCapital4)
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zur Hauptstadt von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        try:
            area = countryID.area()
            question_area = ("Wie groß ist die Fläche von " + countryName_DE + "?")
            correctAnswer_area = str(area) + "km²"
            WrongArea1 = findWrongArea(correctAnswer_area)
            WrongArea2 = findWrongArea(correctAnswer_area)
            WrongArea3 = findWrongArea(correctAnswer_area)
            WrongArea4 = findWrongArea(correctAnswer_area)
            # questions_3[countryNR].append(question_area + " [Antwort: " + correctAnswer_area + "]")
            append_3(countryNR, question_area, correctAnswer_area, WrongArea1, WrongArea2, WrongArea3, WrongArea4)
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zur Fläche von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        try:
            population = countryID.population()
            question_population = ("Wie hoch ist die Einwohnerzahl von " + countryName_DE + "?")
            correctAnswer_population = str(population)
            WrongPopulation1 = findWrongPopulation(correctAnswer_population)
            WrongPopulation2 = findWrongPopulation(correctAnswer_population)
            WrongPopulation3 = findWrongPopulation(correctAnswer_population)
            WrongPopulation4 = findWrongPopulation(correctAnswer_population)
            # questions_3[countryNR].append(question_population + " [Antwort: " + correctAnswer_population + "]")
            append_3(countryNR, question_population, correctAnswer_population, WrongPopulation1, WrongPopulation2, WrongPopulation3, WrongPopulation4)
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zur Einwohnerzahl von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        try:
            region = countryID.region()
            subregion = countryID.subregion()
            try:
                region = GoogleTranslator(source = "en", target = "de").translate(region)
                subregion = GoogleTranslator(source = "en", target = "de").translate(subregion)
            except:
                pass
            question_continent = ("Auf welchem Kontinent liegt " + countryName_DE + "?")
            correctAnswer_continent = (region + " (" + subregion + ")")
            WrongContinent1 = findWrongContinent(correctAnswer_continent)
            WrongContinent2 = findWrongContinent(correctAnswer_continent)
            WrongContinent3 = findWrongContinent(correctAnswer_continent)
            WrongContinent4 = findWrongContinent(correctAnswer_continent)
            # questions_1[countryNR].append(question_continent + " [Antwort: " + correctAnswer_continent + "]")
            append_1(countryNR, question_continent, correctAnswer_continent, WrongContinent1, WrongContinent2, WrongContinent3, WrongContinent4)
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zum Kontinent von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        if e == 4:
            errors.remove("Konnte keine Informationen zur Hauptstadt von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.remove("Konnte keine Informationen zur Fläche von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.remove("Konnte keine Informationen zur Einwohnerzahl von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.remove("Konnte keine Informationen zum Kontinent von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.append("Konnte keine Informationen zu [" + countryName_DE + "] / [" + countryName_EN + "] finden")

        print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
        print("Läd Infos aus dem Darknet runter... " + str(i) + "/" + str(countryCount))
    return()

def addInfo ():
    global manualQuestions_1
    global manualQuestions_2
    global manualQuestions_3
    global missingQuestions_1
    global missingQuestions_2
    global missingQuestions_3
    global questions_1
    global questions_2
    global questions_3
    i = 0
    for country in manualQuestions_1:
        i = i + 1
        countryName_EN = country[0]
        countryName_EN = str(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN)
        countryNR = countryNR[0][0]
        try:
            for question in country:
                if not question == countryName_EN:
                    questions_1[int(countryNR)].append(question)

                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3))
        except:
            pass
    for country in manualQuestions_2:
        i = i + 1
        countryName_EN = country[0]
        countryName_EN = str(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN)
        countryNR = countryNR[0][0]
        try:
            for question in country:
                if not question == countryName_EN:
                    questions_2[countryNR].append(question)
                    
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3))
        except:
            pass
    for country in manualQuestions_3:
        i = i + 1
        countryName_EN = country[0]
        countryName_EN = str(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN)
        countryNR = countryNR[0][0]
        try:
            for question in country:
                if not question == countryName_EN:
                    questions_1[countryNR].append(question)

                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3))
        except:
            pass
    i = 0
    for country in missingQuestions_1:
        i = i + 1
        countryName_EN = country[0]
        countryName_EN = str(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN)
        countryNR = countryNR[0][0]
        try:
            for question in country:
                if not question == countryName_EN:
                    questions_1[countryNR].append(question)

                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
                print("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3))
        except:
            pass
    for country in missingQuestions_2:
        i = i + 1
        countryName_EN = country[0]
        countryName_EN = str(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN)
        countryNR = countryNR[0][0]
        try:
            for question in country:
                if not question == countryName_EN:
                    questions_2[countryNR].append(question)

                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
                print("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3))
        except:
            pass
    for country in missingQuestions_3:
        i = i + 1
        countryName_EN = country[0]
        countryName_EN = str(countryName_EN)
        countryNR = numpy.where(countries_EN_np == countryName_EN)
        countryNR = countryNR[0][0]
        try:
            for question in country:
                if not question == countryName_EN:
                    questions_3[countryNR].append(question)
                
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
                print("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3))
        except:
            pass
    return()

def printErrors ():
    global errors
    for error in errors:
        print(error)
    print()
    return()

def ChooseCountry (countryName):
    global countries_DE
    global countries_EN
    global countries_NATIVE
    global countries_SHORT
    global countries_DE_np
    global countries_EN_np
    global countries_NATIVE_np
    global countries_SHORT_np

    countryName = str(countryName).capitalize()

    try:
        countries_DE.index(countryName)
        countryNR = numpy.where(countries_DE_np == countryName)
    except:
        try:
            countries_EN.index(countryName)
            countryNR = numpy.where(countries_EN_np == countryName)
        except:
            try:
                countries_NATIVE.index(countryName)
                countryNR = numpy.where(countries_NATIVE_np == countryName)
            except:
                try:
                    countries_SHORT.index(countryName.upper())
                    countryNR = numpy.where(countries_SHORT_np == countryName.upper())
                except:
                    print(countryName+" ist ein nicht verfügbares Land")
                    print()
                    return("")
    countryNR = countryNR[0][0]
    return(countryNR)

def submitCountry ():
    global countries_DE
    global countries_EN
    global countries_NATIVE
    global countries_SHORT
    global questions_1
    global questions_2
    global questions_3
    global countryNR
    global countryInput
    input_text = countryInput.get()
    countryNR = ChooseCountry(input_text)
    try:
        countryNames = flag.flagize("DE: " + countries_DE[countryNR] + ", EN: " + countries_EN[countryNR] + ", Native: " + countries_NATIVE[countryNR] + ", Short: " + countries_SHORT[countryNR] + ", Flag: :" + countries_SHORT[countryNR] + ":")
    except:
        countryNames = "Konnte die alternativen Namen von diesem Land nicht laden"
    try:
        question_1 = "[*]   " + questions_1[countryNR][randrange(1,len(questions_1[countryNR]) - 1)]
    except:
        question_1 = "[*]   Keine Ein-Stern-Frage zu diesem Land gefunden"
    try:
        question_2 = "[**]  " + questions_2[countryNR][randrange(1,len(questions_2[countryNR]) - 1)]
    except:
        question_2 = "[**]  Keine Zwei-Stern-Frage zu diesem Land gefunden"
    try:
        question_3 = "[***] " + questions_3[countryNR][randrange(1,len(questions_3[countryNR]) - 1)]
    except:
        question_3 = "[***] Keine Drei-Stern-Frage zu diesem Land gefunden"

def saveStuff ():
    global countries_DE
    global countries_EN
    global countries_NATIVE
    global countries_SHORT
    global questions_1
    global questions_2
    global questions_3
    with open("countries_DE_save.json", "w") as countries_DE_save_file:
        json.dump(countries_DE, countries_DE_save_file)
    with open("countries_EN_save.json", "w") as countries_EN_save_file:
        json.dump(countries_EN, countries_EN_save_file)
    with open("countries_SHORT_save.json", "w") as countries_SHORT_save_file:
        json.dump(countries_SHORT, countries_SHORT_save_file)
    with open("countries_NATIVE_save.json", "w") as countries_DE_NATIVE_file:
        json.dump(countries_NATIVE, countries_DE_NATIVE_file)
    with open("questions_1_save.json", "w") as questions_1_save_file:
        json.dump(questions_1, questions_1_save_file)
    with open("questions_2_save.json", "w") as questions_2_save_file:
        json.dump(questions_2, questions_2_save_file)
    with open("questions_3_save.json", "w") as questions_3_save_file:
        json.dump(questions_3, questions_3_save_file)

if reloadQuestions:
        getCountries()
        createNumpy()
        loadManualQuestions()
        loadMissingQuestions()
        findInfo()
        addInfo()
        saveStuff()
else:
    try:
        importStuff()
        createNumpy()
    except:
        getCountries()
        createNumpy()
        loadManualQuestions()
        loadMissingQuestions()
        findInfo()
        addInfo()
        saveStuff()

print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
print("Läd Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
print("Fügt fehlende Informationen hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
printErrors()
#while true:
#    countryNR = ChooseCountry(input("Schreibe den Namen des Landes: "))
#    try:
#        print(flag.flagize("DE: " + countries_DE[countryNR] + ", EN: " + countries_EN[countryNR] + ", Native: " + countries_NATIVE[countryNR] + ", Short: " + countries_SHORT[countryNR] + ", Flag: :" + countries_SHORT[countryNR] + ":"))
#    except:
#        pass
#    try:
#        print("[*]   " + questions_1[countryNR][randrange(1,len(questions_1[countryNR]) - 1)])
#    except:
#        print("[*]   Keine Ein-Stern-Frage zu diesem Land gefunden")
#    try:
#        print("[**]  " + questions_2[countryNR][randrange(1,len(questions_2[countryNR]) - 1)])
#    except:
#        print("[**]  Keine Zwei-Stern-Frage zu diesem Land gefunden")
#    try:
#        print("[***] " + questions_3[countryNR][randrange(1,len(questions_3[countryNR]) - 1)])
#    except:
#        print("[***] Keine Drei-Stern-Frage zu diesem Land gefunden")
#    print()

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

# pygame setup
pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Font = pygame.font.SysFont('timesnewroman',  20)

pygame.display.set_caption("MapInfo")

buttonAnswer1 = Button(
    screen, 0, 100, 500, 120, text='Hello',
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion()
)

buttonAnswer2 = Button(
    screen, 0, 150, 500, 170, text='Hello',
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion()
)

buttonAnswer3 = Button(
    screen, 0, 200, 500, 220, text='Hello',
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255), radius=20,
    onClick=lambda: NewQuestion()
)

buttonAnswer4 = Button(
    screen, 0, 250, 500, 270, text='Hello',
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 0, 255
    ), radius=20,
    onClick=lambda: NewQuestion()
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
    global Answer1Text_text
    if questionDifficulty == 1:
        Answer1Text_text = ("Antwort 1: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer1Text_text = ("Antwort 1: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer1Text_text = ("Antwort 1: " + questions_3[countryNR][questionNR][1])

def Answer2_right (countryNR, questionNR, questionDifficulty):
    global Answer2Text_text
    if questionDifficulty == 1:
        Answer2Text_text = ("Antwort 2: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer2Text_text = ("Antwort 2: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer2Text_text = ("Antwort 2: " + questions_3[countryNR][questionNR][1])

def Answer3_right (countryNR, questionNR, questionDifficulty):
    global Answer3Text_text
    if questionDifficulty == 1:
        Answer3Text_text = ("Antwort 3: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer3Text_text = ("Antwort 3: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer3Text_text = ("Antwort 3: " + questions_3[countryNR][questionNR][1])

def Answer4_right (countryNR, questionNR, questionDifficulty):
    global Answer4Text_text
    if questionDifficulty == 1:
        Answer4Text_text = ("Antwort 4: " + questions_1[countryNR][questionNR][1])
    if questionDifficulty == 2:
        Answer4Text_text = ("Antwort 4: " + questions_2[countryNR][questionNR][1])
    if questionDifficulty == 3:
        Answer4Text_text = ("Antwort 4: " + questions_3[countryNR][questionNR][1])

def NewQuestion ():
    global countries_DE
    global countries_EN
    global countries_NATIVE
    global countries_SHORT
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
        NewQuestion()

NewQuestion()

running = True

i = 0

while running:

    i += 1

    events = pygame.event.get()
    for event in events: # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

    screen.fill("Lime") # fill the screen with a color to wipe away anything from last frame

    pygame_widgets.update(events)

    #### start of renderer

    screen.blit(TitleText, (0, 0))
    screen.blit(QuestionNRText, (0, 50))
    screen.blit(CountryText, (0, 100))
    screen.blit(QuestionText, (0, 150))
    screen.blit(Answer1Text, (0, 200))
    screen.blit(Answer2Text, (SCREEN_WIDTH/2, 200))
    screen.blit(Answer3Text, (0, 250))
    screen.blit(Answer4Text, (SCREEN_WIDTH/2, 250))

    pygame.display.update()

    #### end of renderer

    pygame.time.wait(10)

pygame.quit()
