import psutil

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Имя: {proc.info['name']}")

list_processes()