import csv

d = {}

try:
    with open('./data/test_csv.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         # print('spamreader - > ', spamreader)
         for row in spamreader:
             print('length - > ',len(row))
             for i in row:
                 print('rooww  - > ',i)
                 d[i] = i
             print(', '.join(row))
             print('---------------------')
             print(d)
except Exception as e:
    print('Error in reading the file - > ', e)
