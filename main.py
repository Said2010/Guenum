import random

from Number import Number

class Game():
    def __init__(self):
        self.num = Number()
        self.run_game
        self.ls = []
        self.ll = []
        self.k = 0 
        self.rec_list = []
        self.max_rec = 0

#Угадывание
    def gue(self, n, l, k, rec ):
        """Угадывание числа"""
        if k == l:
            print(f"Ты проиграл! Загаданное число было: {n}\n Кол-во попыток было {l}")
            rec = 0
            return self.con()

    #Обработка ошибки
        try:
            an = int(input("Угадай число!:\t"))
        except ValueError:
            print("Не верное введение числа")
            self.gue(n, l, k, rec=rec )
            return
        
        n = int(n)
        if n < an:
            print("Меньше")
            self.ls.append(an)
            rec+=1
            return self.gue(n=n, l=l, k=k+1, rec=rec)
        elif n > an:
            print("Больше")
            self.ll.append(an)
            rec+=1
            return self.gue(n=n, l=l,k=k+1, rec=rec)
        elif an == n:
            self.rec_list.append(rec)
            print(f"Ты выйграл!\nКоличество попыток {rec}\n Лучший результат {min(self.rec_list)}")
            rec = 0
            return self.con()

    def con(self):
        """Спрашивает о продолжении"""
        a_1 = input("\tХотите продолжить?")
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

                t = self.gue(n=n, l=l, k=0, rec=1 )
                if t == False:
                    game = False
                else:
                    game = True

start = Game()
start.run_game()