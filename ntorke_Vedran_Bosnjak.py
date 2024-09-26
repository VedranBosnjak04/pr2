"""Iz učitanih podataka sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.
Nedovoljan
0-49%
Dovoljan
50-65%
Dobar
65-80%
Vrlodobar
80-90%
Izvrstan
90-100%"""

from csv import reader
import csv

with open('P1REZ.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple, csv_reader))[4:-3]

studenti.sort(key=lambda i: i[1])
print(studenti)

rjecnik = {
    "nedovoljan": 0,
    "dovoljan": 0,
    "dobar": 0,
    "vrlo dobar": 0,
    "izvrstan": 0
    }
for i in studenti:
    if int(i[2]) >= 50 and int(i[2]) <65:
        rjecnik["dovoljan"] += 1
    elif int(i[2]) >= 65 and int(i[2]) < 80:
        rjecnik["dobar"] += 1
    elif int(i[2]) >= 80 and int(i[2]) < 90:
        rjecnik["vrlo dobar"] += 1
    elif int(i[2]) >= 90:
        rjecnik["izvrstan"] += 1

print(rjecnik)

