import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f"Файл {src} скопирован в {dst}")

copy_file('Лабораторная работа № 17.odt', 'destination.odt')  # замените на свои файлы