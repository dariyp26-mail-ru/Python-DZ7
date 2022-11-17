import sys
import model

def createMenu():
    print('|#########################|')
    print('|Телефонный справочник    |')
    print('|#########################|')
    print('|1 - Показать справочник  |')
    print('|2 - Добавить запись      |')
    print('|3 - Поиск по имени       |')
    print('|4 - Выгрузить в book.html|')
    print('|5 - Выгрузить в book.xml |')
    print('|0 - Выход                |')
    print('|#########################|')
    number_menu = input()
    if number_menu == '1' : printTel()
    elif number_menu == '2' : addTel()
    elif number_menu == '3' : serchTel()
    elif number_menu == '4' : saveHTML()
    elif number_menu == '5' : saveXML()
    elif number_menu == '0' : end()
    else : 
        print('Некорректный ввод')
        print()
        createMenu()

def printTel():
    model.printTelef()
    createMenu()

def saveHTML():
    model.saveAsHTML()
    createMenu()

def saveXML():
    model.saveAsXML()
    createMenu()

def addTel():
    model.addTelef()
    createMenu()

def serchTel():
    model.serchTelef()
    createMenu()

def end():
    print('Завершение работы...')
    sys.exit()