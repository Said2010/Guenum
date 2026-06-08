import random

from Number import Number

class Game():
    def __init__(self):
        self.num = Number()
        self.run_game
        self.ls = []
        self.ll = []
        self.k = 0 

#Угадывание
    def gue(self, n, l, k ):
        """Угадывание числа"""
        if k == l:
            print(f"Ты проиграл! Загаданное число было: {n}")
            return self.con()

    #Обработка ошибки
        try:
            an = int(input("Угадай число!:\t"))
        except ValueError:
            print("Не верное введение числа")
            self.gue(n, l, k )
            return
        
        n = int(n)
        if n < an:
            print("Меньше")
            self.ls.append(an)
            return self.gue(n=n,l=l, k=k+1)
        elif n > an:
            print("Больше")
            self.ll.append(an)
            return self.gue(n=n, l=l,k=k+1)
        elif an == n:
            print("Ты выйграл")
            return self.con()

    def con(self):
        """Спрашивает о продолжении"""
        a_1 = input("Хотите продолжить?")
        if a_1.title() == "Да":
            t = True
            return t
        elif a_1.title() == "Нет":
            t = False
            return t
        else:
            print("Ответе Да/Нет")
            self.con()
        
#Игра
    def run_game(self):
        """Запуск игры"""
        game = True
        while game:
            result = self.num.ch()
            if result == False:
                game = False
            else:
                d, l = result
                n = self.num.ran_x (dif= d)

                t = self.gue(n=n, l=l, k=0 )
                if t == False:
                    game = False
                else:
                    game = True

start = Game()
start.run_game()