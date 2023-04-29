"""
pip install countryinfo
pip install pycountry
pip install deep_translator
pip install numpy
pip install pip install emoji-country-flag
pip install pygame
""" ##installation der libraries

from countryinfo import CountryInfo 
from deep_translator import GoogleTranslator
import pycountry
import numpy
import random
import json
import flag
import tkinter ##import der libraries
import pygame

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
        countries_DE = json.load(countries_EN_save_file)
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

        label_1.configure(text=("Erfindet Länder... " + str(i) + "/" + str(countryCount)))
        print("Erfindet Länder... " + str(i) + "/" + str(countryCount))
        win.update() ##updated das fenster
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
            captial = countryID.capital()
            try:
                captial = GoogleTranslator(source = "en", target = "de").translate(captial)
            except:
                pass
            question_capital = ("Wie heißt die Hauptstadt von " + countryName_DE + "? [Antwort: " + captial + "]")
            questions_2[countryNR].append(question_capital)
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zur Hauptstadt von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        try:
            area = countryID.area()
            question_area = ("Wie groß ist die Fläche von " + countryName_DE + "? [Antwort: " + str(area) + "km² (" + str(int(area*0.9)) + " - " + str(int(area*1.1)) + ")]")
            questions_3[countryNR].append(question_area)        
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zur Fläche von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        try:
            population = countryID.population()
            question_population = ("Wie hoch ist die Einwohnerzahl von " + countryName_DE + "? [Antwort: " + str(population) + " (" + str(int(population*0.9)) + " - " + str(int(population*1.1)) + ")]")
            questions_3[countryNR].append(question_population)
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
            question_continent = ("Auf welchem Kontinent liegt " + countryName_DE + "? [Antwort: " + region + " (" + subregion + ")]")
            questions_1[countryNR].append(question_continent)
        except:
            e = e + 1
            errors.append("Konnte keine Informationen zum Kontinent von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
        if e == 4:
            errors.remove("Konnte keine Informationen zur Hauptstadt von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.remove("Konnte keine Informationen zur Fläche von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.remove("Konnte keine Informationen zur Einwohnerzahl von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.remove("Konnte keine Informationen zum Kontinent von [" + countryName_DE + "] / [" + countryName_EN + "] finden")
            errors.append("Konnte keine Informationen zu [" + countryName_DE + "] / [" + countryName_EN + "] finden")

        label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
        label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(i) + "/" + str(countryCount)))
        print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
        print("Läd Infos aus dem Darknet runter... " + str(i) + "/" + str(countryCount))
        win.update() ##updated das fenster
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

                label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3)))
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3))
                win.update() ##updated das fenster
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

                label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3)))
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3))
                win.update() ##updated das fenster
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

                label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3)))
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(i) + "/" + str(countryCount*3))
                win.update() ##updated das fenster
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

                label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)"))
                label_4.configure(text=("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3)))
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
                print("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3))
                win.update() ##updated das fenster
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

                label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)"))
                label_4.configure(text=("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3)))
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
                print("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3))
                win.update() ##updated das fenster
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
                
                label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_2.configure(text=("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
                label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)"))
                label_4.configure(text=("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3)))
                print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Lädt Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
                print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
                print("Fügt fehlende Informationen hinzu... " + str(i) + "/" + str(countryCount*3))
                win.update() ##updated das fenster
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

win=tkinter.Tk(className = "MapInfo")
win.geometry("750x200")

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
        question_1 = "[*]   " + questions_1[countryNR][random.randrange(1,len(questions_1[countryNR]))]
    except:
        question_1 = "[*]   Keine Ein-Stern-Frage zu diesem Land gefunden"
    try:
        question_2 = "[**]  " + questions_2[countryNR][random.randrange(1,len(questions_2[countryNR]))]
    except:
        question_2 = "[**]  Keine Zwei-Stern-Frage zu diesem Land gefunden"
    try:
        question_3 = "[***] " + questions_3[countryNR][random.randrange(1,len(questions_3[countryNR]))]
    except:
        question_3 = "[***] Keine Drei-Stern-Frage zu diesem Land gefunden"
    label_names.configure(text=countryNames)
    label_question1.configure(text=question_1)
    label_question2.configure(text=question_2)
    label_question3.configure(text=question_3)

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

label_1 = tkinter.Label(win, text="")
label_1.grid(row=0)
label_2 = tkinter.Label(win, text="")
label_2.grid(row=1)
label_3 = tkinter.Label(win, text="")
label_3.grid(row=2)
label_4 = tkinter.Label(win, text="")
label_4.grid(row=3)
textLabel = tkinter.Label(win, text="Schreibe den Namen des Landes: ")
textLabel.grid(row=4, column=0)
countryInput = tkinter.Entry(win)
countryInput.grid(row=4, column=1)
button = tkinter.Button(win, text="Suche nach Fragen", command=submitCountry)
button.grid(row=4, column=2)
label_names = tkinter.Label(win, text="")
label_names.grid(row=5)
label_question1 = tkinter.Label(win, text="")
label_question1.grid(row=6)
label_question2 = tkinter.Label(win, text="")
label_question2.grid(row=7)
label_question3 = tkinter.Label(win, text="")
label_question3.grid(row=8)
win.update() ##updated das fenster

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

label_1.configure(text=("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
label_2.configure(text=("Läd Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)"))
label_3.configure(text=("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)"))
label_4.configure(text=("Fügt fehlende Informationen hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)"))
print("Erfindet Länder... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
print("Läd Infos aus dem Darknet runter... " + str(countryCount) + "/" + str(countryCount) + " (Done)")
print("Fügt manuelle Informationen unseres Sklaven hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
print("Fügt fehlende Informationen hinzu... " + str(countryCount*3) + "/" + str(countryCount*3) + " (Done)")
printErrors()
win.mainloop()
#while true:
#    countryNR = ChooseCountry(input("Schreibe den Namen des Landes: "))
#    try:
#        print(flag.flagize("DE: " + countries_DE[countryNR] + ", EN: " + countries_EN[countryNR] + ", Native: " + countries_NATIVE[countryNR] + ", Short: " + countries_SHORT[countryNR] + ", Flag: :" + countries_SHORT[countryNR] + ":"))
#    except:
#        pass
#    try:
#        print("[*]   " + questions_1[countryNR][random.randrange(1,len(questions_1[countryNR]))])
#    except:
#        print("[*]   Keine Ein-Stern-Frage zu diesem Land gefunden")
#    try:
#        print("[**]  " + questions_2[countryNR][random.randrange(1,len(questions_2[countryNR]))])
#    except:
#        print("[**]  Keine Zwei-Stern-Frage zu diesem Land gefunden")
#    try:
#        print("[***] " + questions_3[countryNR][random.randrange(1,len(questions_3[countryNR]))])
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

screen = pygame.display.set_mode((500, 500))

Font = pygame.font.SysFont('timesnewroman',  30)

pygame.display.set_caption("MapInfo")

global QuestionCount
QuestionCount = 0

def Answer_1_right (countryNR, QuestionNR):
    global Answer_1
    Answer_1 = (questions_1[countryNR][QuestionNR])

def Answer_2_right (countryNR, QuestionNR):
    global Answer_2
    Answer_2 = (questions_1[countryNR][QuestionNR])

def Answer_3_right (countryNR, QuestionNR):
    global Answer_3
    Answer_3 = (questions_1[countryNR][QuestionNR])

def Answer_4_right (countryNR, QuestionNR):
    global Answer_4
    Answer_4 = (questions_1[countryNR][QuestionNR])

def NewQuestion (countryNR, QuestionNR):
    global QuestionCount
    QuestionCount += 1

    switch={
        1 : Answer_1_right(countryNR, QuestionNR),
        2 : Answer_2_right(countryNR, QuestionNR),
        3 : Answer_3_right(countryNR, QuestionNR),
        4 : Answer_4_right(countryNR, QuestionNR)
    }
    
    switch.get(random.randrange(1,4))

    global TitleText
    global QuestionText
    global Answer1Text
    global Answer2Text
    global Answer3Text
    global Answer4Text
    TitleText=Font.render("Länder Quiz!!!!!!!", False, BLACK, WHITE)
    QuestionText_text = str(QuestionCount) + ". Frage!!!!!!!!!!"
    QuestionText=Font.render(QuestionText_text, False, BLACK, WHITE)
    Answer1Text=Font.render(Answer_1, False, BLACK, WHITE)
    Answer2Text=Font.render(Answer_2, False, BLACK, WHITE)
    Answer3Text=Font.render(Answer_3, False, BLACK, WHITE)
    Answer4Text=Font.render(Answer_4, False, BLACK, WHITE)

countryNR = random.randrange(249)
NewQuestion(countryNR, random.randrange(1,len(questions_1[countryNR])))

running = True

while running:
    for event in pygame.event.get(): # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

    #### start of renderer
    CountryNR = random.randrange(1, len(countries_DE)) - 1
    QuestionNR = random.randrange(1, len(questions_1[countryNR]))

    screen.fill("Lime") # fill the screen with a color to wipe away anything from last frame

    screen.blit(TitleText, (10, 10))

    pygame.display.update()

    #### end of renderer

    pygame.time.wait(500)

pygame.quit()
