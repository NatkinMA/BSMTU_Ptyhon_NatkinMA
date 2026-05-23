import os

def delete_file(filename):
    os.remove(filename)
    print(f"Файл {filename} удален.")

delete_file('destination.txt')  # замените на имя файла.