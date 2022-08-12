from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]


total = timedelta()

for working in data:
    started = time(hour=int(working[0].split(':')[0]), minute = int(working[0].split(':')[1]))
    finished = time(hour=int(working[1].split(':')[0]), minute = int(working[1].split(':')[1]))
    total += timedelta(finished) - timedelta(started)
    print(total)

print(total)
