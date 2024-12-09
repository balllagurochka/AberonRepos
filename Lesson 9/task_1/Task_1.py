import os

#Использовать ОДИН раз, лучше сделать копию
#Не знаю как ее сделать кроссплатформенной если у всех разная директория файлов и ее нужно указывать отдельно
new_direct = os.chdir("Work")
main_pos = os.getcwd()

"""Вывести имя вашей ОС"""
print(f"Имя вашей Операционной Системы: {os.name}")

"""Вывести путь до папки, в которой вы находитесь"""
print(f"Путь до папки: {main_pos}")

""" Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений """
folder_name = ""
list_files = os.listdir()
for file in list_files:
    current_pos = f"{main_pos}\\{file}"
    # Присваиевам название нашего расширения
    file_ext = file[file.rfind(".")+1:]
    #Создаем папку
    if not folder_name == f"{file_ext}_folder":
        folder_name = f"{file_ext}_folder"
        os.mkdir(f"{main_pos}\\{folder_name}")
    # #Перемещаем файл в папку
    os.replace(f"{file}", f"{folder_name}/{file}")

""" После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт """
folders = os.listdir()
for folder in folders:
    count = 0
    size_all = 0
    os.chdir(f"{folder}")
    files = os.listdir()
    for file in files:
        count += 1
        size = os.stat(file).st_size
        size_all += size
    print(f"В папку {folder} перемещено {count} файлов, их суммарный размер - {size_all} байт» ")
    os.chdir("..")

"""Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt"""

main_name = file
new_name = f"another_file.{file[file.rfind(".")+1:]}"
os.rename(f"{folder}\\{main_name}", f"{folder}\\{new_name}")
print(f"Файл {main_name} был переименован в {new_name}")







