import os

def find_file(file_name, search_path='/home/'):
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return "Файл не найден"

# Замените 'lab_work.txt' на имя файла вашей лабораторной работы
file_to_find = 'matrix_3.txt'

file_path = find_file(file_to_find)

print("Полный путь к файлу:", file_path)