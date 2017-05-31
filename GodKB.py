import csv

with open('data/South_korea/2015/2015_01.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    your_list = list(reader)

print(your_list[0])