import datetime
import pytz


city_name = 'Иркутск'
time_zone = pytz.timezone('Asia/Irkutsk')
current_time = datetime.datetime.now(time_zone)
print(f"Текущее время в городе {city_name}: {current_time.strftime('%H:%M')}")