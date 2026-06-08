import random

from Number import Number

class Game():
    def __init__(self):
        self.num = Number()
        self.run_game
        self.ls = []
        self.ll = []

#Угадывание
    def gue(self, n):
        """Угадывание числа"""
        
        try:
            an = int(input("Угадай число!:\t"))
        except ValueError:
            print("Не верное введение числа")
            self.gue(n)
            return
        
        n = int(n)
        if n < an:
            print("Меньше")
            self.ls.append(an)
            self.gue(n=n)
        elif an == n:
            print("Ты выйграл")
        elif n > an:
            print("Больше")
            self.ll.append(an)
            self.gue(n=n)
    
       
#Игра
    def run_game(self):
        """Запуск игры"""
        game = True
        while game:
            d = self.num.ch()
            if d == False:
                game = False
            else:
                n = self.num.ran_x (dif= d)
                self.gue(n=n)

start = Game()
start.run_game()