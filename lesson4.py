#EASY ****************************************************************
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
ls = [1, 2, 3, 4, 5]
ls_g = [el**2 for el in ls]
print("Квадраты: ", ls_g)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ["apple", "orange", "banana", "pear"]
fruits2 = ["apple", "orange", "mango"]
fruitsUnited = [el for el in fruits1 if fruits2.__contains__(el)]
print("Объединенный список фруктов: ", fruitsUnited)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
ls = [1, 2, 3, 4, 5, 21, 30]
lsMultiple = [el for el in ls if el % 3 == 0 and el > 0 and el % 4 != 0]
print(lsMultiple)
#******************************************************************************

#NORMAL
# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры,
# потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
email = input("Введите email: ")
pattern1 = "^[А-Я]{1,1}"
if re.match(pattern1, name) is None:
    print("Имя в неверном формате")
    if re.match(pattern1, surname) is None:
        print("Фамилия в неверном формате")
        if re.match('[a-z0-9_]+@+[a-z0-9]+\.(ru|com|org)', email) is None:
                print("email в неверном формате")
else:
    print("Добро пожаловать: {}, {}, {}".format(name, surname, email))



# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые....,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
pattern = "[/.]{2}"
if re.findall(pattern, some_str) is None:
    print("В тексте нет 2-х и более точек подряд")
else:
    print("В тексте найдено более двух точек подряд")

