import csv

with open('username.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if len(row['First_name']) > 5:
            print(row)