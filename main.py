import random

from Number import Number

class Game():
    def __init__(self):
        self.num = Number()
        self.run_game
        self.ls = []
        self.ll = []

#Угадывание
    def gue(self, n, l):
        """Угадывание числа"""
        k = 0 
    #Обработка ошибки
        try:
            an = int(input("Угадай число!:\t"))
        except ValueError:
            print("Не верное введение числа")
            self.gue(n)
            return
        
        n = int(n)
        if k == l:
            print("Ты проиграл")
        elif n < an:
            print("Меньше")
            self.ls.append(an)
            self.gue(n=n)
            k += 1
        elif an == n:
            print("Ты выйграл")
        elif n > an:
            print("Больше")
            self.ll.append(an)
            self.gue(n=n)
            k += 1
    
       
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

                self.gue(n=n, l=l)

start = Game()
start.run_game()