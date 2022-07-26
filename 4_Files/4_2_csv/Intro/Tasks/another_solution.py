import csv

def key_func(grade):
    number, letter = grade.split('-')
    return int(number), letter

with open('student_counts.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print(list(reader))
    columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
    rows = list(reader)

with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)

