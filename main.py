import random

class Activity:
    def __init__(self, name, progress = 0, feeling = 0 ):
        self.name = name
        self.progress = progress
        self.feeling = feeling


class Student:
    def __init__(self, name, progress = 100, feeling = 100 ):
        self.name = name
        self.progress = progress
        self.feeling = feeling
        self.alive = True

    def __str__(self):
        return f'{self.name} (успеваемость: {self.progress}, настроение: {self.feeling})'

    def do (self, activity: Activity):
        print(f'{self.name} взялся за {activity.name}')
        self.progress += activity.progress
        self.feeling += activity.feeling
        self.check_alive()

    def check_alive(self):
        self.alive = self.progress > 0 and self.feeling > 0


stud1 = Student('Mark')
stud2 = Student('Евкакий')

math = Activity('Математику', progress=4, feeling=3)
football = Activity('Игру в футбол с друзьями', progress=-1, feeling=6)
study = Activity('Учёбу', progress=12, feeling=-5)
training = Activity('Тренировки', progress=-2, feeling=-1)
homework = Activity('ДЗ', progress=9, feeling=-4)

wwf = Activity('Прогулку с друзьями', progress=-7, feeling=7)
pmf = Activity('Пуш завика в пабге', progress=-14, feeling=10)
watch_TV = Activity("Просмотр телевизора",progress=-3, feeling=6)

activities = [math, football, study, training, homework, wwf, pmf, watch_TV]
for day in range(30):
    print(f' - День {day+1}')
    stud1.do(random.choice(activities))
    stud2.do(random.choice(activities))
    print(' --- ')
    print(stud1)
    print(stud2)
    if not stud1.alive or not stud2.alive:
        break