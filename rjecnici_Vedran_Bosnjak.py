"""Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)"""

import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjene = {}
for student in imena:
    ocjene[student] = random.randint(1,5)

rjecnik_ocjena = {}
for ocjena in ocjene.values():
    if ocjena not in rjecnik_ocjena:
        rjecnik_ocjena[ocjena] = 1
    else:
        rjecnik_ocjena[ocjena] += 1

br = 0
for i in ocjene.values():
    if i > 1:
        br += 1
prosjek = round((br/len(ocjene))*100, 2)

print("Prolaznost: ", prosjek, "%")
print(ocjene)
print(rjecnik_ocjena)
