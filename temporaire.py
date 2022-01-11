import csv

with open('test.csv', 'w', newline='') as fichier:
    writer = csv.writer(fichier)
    writer.writerow(['semaine', 1])
    writer.writerow(['#THEMES'])
    for num in range(6):
        writer.writerows([['#'], [num, 0, 1, 2, 3]])
    writer.writerow(['#MOTS'])
    for num in range(6):
        writer.writerows([['#'], [num, 0, 1, 2, 3]])


