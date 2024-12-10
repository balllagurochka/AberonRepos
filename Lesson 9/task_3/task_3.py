import re

#Поиск слов и их количества
def get_most_count(a):
    words = re.findall(r'\b\w+\b', a[0])
    #key= слово value= количество
    word_counts = {} # 
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1 #
        most_word = max(word_counts, key=word_counts.get())
        count = word_counts.get(most_word)
    return most_word, count

#-------
def file_open(a):
    with open(f"{a}", "r", encoding="utf-8") as file:
        list_of_str = file.readlines()
    results = []
    for str_file in list_of_str:
        most_word, count = most_count([str_file])
        results.append((most_word, count))
    return results

#---------
def new(file_path):
    result = file_open(file_path)
    with open("New_file.txt", "w", encoding="utf-8") as new_file:
        for word, count in result:
            new_file.write(f"Слово '{word}' встречается {count} раз(а)\n")

a = input("Введите абсолютный путь до вашего файла: ") #C:\\Users\\Strug\\Desktop\\AberonRepos\\Lesson 9\\task_3\\Some_text.txt
new(a)
