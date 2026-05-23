import subprocess

def add_user(username):
    subprocess.run(['sudo', 'useradd', username])
    print(f"Пользователь {username} добавлен.")

add_user('noviy_user')