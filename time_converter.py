import sys

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    data = file.readlines()

with open(filename, 'w', encoding='utf-8') as file:
    for row in data:
        if 'M73' not in row:
            file.write(row)
            continue
        progress, minutes = [int(m[1:]) for m in row.split()[1:]] # percents and remaining time in minutes
        new_row = 'M117 '
        new_row += f'{str(minutes//60).zfill(2)}:{str(minutes%60).zfill(2)} left'
        new_row += f' / {str(progress).rjust(2)}% done\n'
        file.write(new_row)
