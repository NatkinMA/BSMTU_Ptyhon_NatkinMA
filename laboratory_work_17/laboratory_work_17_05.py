import psutil
import time

def monitor_resources():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print(f"CPU загружен на: {cpu_percent}%")
        print(f"Памяти использовано: {mem.percent}%")
        print(f"Диск заполнен на: {disk.percent}%")
        print("-----------------------------")

        time.sleep(5)  # Пауза 5 секунд перед следующим замером
if __name__ == "__main__":
    monitor_resources()