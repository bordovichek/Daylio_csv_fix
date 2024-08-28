import csv

with open('daylio_export_2024_08_29.txt', 'r') as file_read, open('fixed_daylio_export_2024_08_29.csv', 'w', encoding='utf-8-sig', newline='') as file_write:
    cols = [x for x in file_read.readline().strip().split(',')]
    print(cols)
    writer = csv.writer(file_write, delimiter=';')
    writer.writerow(cols[:-1])
    for stroka in file_read.readlines():
        info = list(filter(lambda x: x and x != ',', stroka.strip().split('"')))
        date_and_mood = info[0].strip(",").split(",")
        full_date = date_and_mood[0]
        date = date_and_mood[1]
        weekday = date_and_mood[2]
        time = date_and_mood[3]
        mood = date_and_mood[4]
        try:
            full_data = [full_date, date, weekday, time, mood, info[1], info[2]]
            writer.writerow(full_data)
        except:
            print(f'Information about the day is not recorded: {info}')
