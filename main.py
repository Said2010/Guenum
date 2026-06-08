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
            self.gue(n=n,l=l, k=k+1)
        elif an == n:
            print("Ты выйграл")
        elif n > an:
            print("Больше")
            self.ll.append(an)
            self.gue(n=n, l=l,k=k+1)
        
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

                self.gue(n=n, l=l, k=0 )

start = Game()
start.run_game()