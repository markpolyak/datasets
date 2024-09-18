# Выводит все расширения файлов, которые есть, и кол-во файлов каждого расширения

import os
from collections import defaultdict

# Директория для обхода
root_dir = "dumpsters"

# Словарь для хранения статистики по форматам файлов
file_formats = defaultdict(int)

# Функция для обхода директорий
def walk_directories(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            _, extension = os.path.splitext(filename)
            file_formats[extension.lstrip(".")] += 1
        for dirname in dirnames:
            walk_directories(os.path.join(dirpath, dirname))

# Запуск обхода
walk_directories(root_dir)

# Вывод статистики по форматам файлов
print("File format statistics:")
for file_format, count in sorted(file_formats.items(), key=lambda x: x[1], reverse=True):
    print(f"{file_format}: {count}")
