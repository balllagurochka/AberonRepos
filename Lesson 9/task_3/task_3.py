import re

#Поиск слов и их количества
def most_count(a):
    #Ищем слова и помещаем их в список
    words = re.findall(r'\b\w+\b', a[0])
    #Словарь где key= слово value= количество
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1 #
        most_word = max(word_counts, key=word_counts.get)
        count = word_counts[most_word]
    return most_word, count

#Открываем файл
def file_open(a):
    with open(f"{a}", "r", encoding="utf-8") as file:
        #Добавляем строки в список
        list_of_str = file.readlines()
    print(list_of_str)
    result = []
    #Каждая строка в виде списка
    for str_file in list_of_str:
        most_word, count = most_count([str_file])
        result.append((most_word, count))
    return result

def new(file_path):
    result = file_open(file_path)
    with open("New_file.txt", "w", encoding="utf-8") as new_file:
        for word, count in result:
            new_file.write(f"Слово '{word}' встречается {count} раз(а)\n")

a = input("Введите абсолютный путь до вашего файла: ") #C:\\Users\\Strug\\Desktop\\AberonRepos\\Lesson 9\\task_3\\Some_text.txt
new(a)
