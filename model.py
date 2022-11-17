names = ['Иванов Иван', 'Петров Петр', 'Сидоров Сидр']
tel = ['+71234567890\n', '+71234567891\n', '+71234567892\n']


def printTelef():
    list = []
    for i in range(len(names)):
        list.append(names[i])
        list.append(tel[i])
    print(' '.join(list))


def addTelef():
    name = input("Введите ФИО: ")
    telephone = input("Введите tel: ") + '\n'

    names.append(name)
    tel.append(telephone)
    print('Данные добавлены!')

def serchTelef():
    name = input("Введите ИМЯ: ")
    for i in range(len(names)):
        if name in names[i] : print(names[i] + ' ' + tel[i])


def saveAsHTML():

    book = open('book.html', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])
        book.write('<br>')

    print('Файл "book.html" сохранен!')


def saveAsXML():

    book = open('book.xml', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])

    print('Файл "book.xml" сохранен!')
