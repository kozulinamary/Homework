"""Написать такую программу,  которая будет выводить,  анализировать текстовый файл,
обычный текстовый файл,
но при этом будет принимать некий  символ на вход, ну либо некоторое слово,  ну в общем принимать строку
и выводить то количество раз,  какое эта строка встречается в этом тексте,  в тексте этого файла.
На вход мы принимаем строку, а возвращаем интеджер.

Мне нужно вывести число? Сколько раз встречается слово в этом файле?

"""


"""Вариант 1"""
with open("test.txt", "r") as file:
    tekst = file.read()
    b = [tekst]
word = input("Введи интересуещее тебя букву (слово, строку) без пробела ")
print(tekst.count(str(word)))





"""Вариант 2 """
word = input("Введи интересуещее тебя букву (слово, строку) без пробела ")
with open("test.txt", "r") as file:
    text = file.read()
def letter_counter(letter: str) -> None:
    with open("counter.txt", "w") as file:
        for word in text.split():
            if letter in word:
                file.write(f"{word} ")
    return None
letter_counter("message")
with open("counter.txt", "r") as file:
    a = file.read()
    print(a.count(word))