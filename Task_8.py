# 1. Доработать калькулятор(групповая работа)

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")


#  2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import pickle
class Book():
    def __init__(self):
        self.Dict = {}
    def enter(self):
    
        while True:
            self.name_family = input("Введите имя и фамилию человека: ")
            self.nomer = input("Введите его номер телефона: ")
            self.Dict [self.name_family] = self.nomer
            self.file = open("Text.bin", 'wb')
            pickle.dump(self.Dict, self.file) 
            self.file.close()
 
            exit_menu = input("Добавить ещё данные или выйти в меню?")
            if exit_menu == "Выйти" or exit_menu == "выйти":
                break
    def output(self):
        file = open('Text.bin', 'rb')
        self.Dict = pickle.load(file)
        print(self.Dict)
 
    def Change(self):
        self.output()
        self.name_family_change = input("Введите имя и фамилию человека чей номер хотите изменить или удалить:\n ")
        if self.name_family_change in self.Dict:
            self.del_and_change = input("Удалить или изменить? \n")
        else:
            print("Такого человека нету в списке попробуйте снова")
 
 
 
a = Book()
a.enter()
a.output()
a.Change()


