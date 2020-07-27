import csv

data = []

with open('Flight Distance Test.csv', 'r+') as f:
    csv_data = csv.reader(f)
    headers = next(csv_data)
    print(headers)

    for row in csv_data:
        data.append(row)

print(*data, sep='\n')