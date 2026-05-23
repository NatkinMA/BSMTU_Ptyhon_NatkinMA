import subprocess

def remove_user(username):

    subprocess.run(['sudo', 'userdel', username])
    print(f"Пользователь {username} удален.")

remove_user('noviy_user')