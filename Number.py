import random
#Число
class Number():
    def ch(self):
        """Выбор сложности """
        ch = input("Выберите сложность: \n Легкая-1, попыток 5 " \
        "\n Средняя-2, попыток 7 \n Сложная-3, попыток 9 \n Выход 'q' \n")
        #Проверка выхода
        if ch == "q":
            print("Выход")
            return False
        #Проверка сложности
        if ch.title() == "Легкая" or ch == "1":
            print("Выбрана легкая сложность")
            dif = 1
            li = 5
            return dif, li
        elif ch.title() == "Средняя" or ch == "2":
            print("Выбрана средняя сложность")
            dif = 2
            li = 7 
            return dif, li
        elif ch.title() == "Сложная" or ch == "3":
            print("Выбрана трудная сложность")
            dif = 3
            li = 9
            return dif, li
        else:
            print("Не верный ввод, повторите")
            return self.ch()

    def ran_x(self, dif):
        """Задание числа"""
        if dif == 1:
            return self._nur(10)
        elif dif == 2:
            return self._nur(100)
        else:
            return self._nur(1000)
        
    def _nur (self, x):
        """Задание числа, вспомогательная"""
        n = random.randint(1, x)
        return int(n)
    