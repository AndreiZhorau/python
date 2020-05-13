user_time_seconds = int(input('Введите время в секундах: '))

time_hours = user_time_seconds // 3600
time_minutes = (user_time_seconds % 3600) // 60
time_seconds = user_time_seconds % 60

print(f'{time_hours:02d}:{time_minutes:02d}:{time_seconds:02d}')
