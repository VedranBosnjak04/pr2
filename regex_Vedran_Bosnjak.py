"""Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak."""

import re

regex = "^[vV].*[0-5]+.*[kK]$"
while True:
    unos = input("Unesi string: ")
    provjera = re.search(regex, unos)
    if provjera:
        print("Valjan unos")
        break
    else:
        print("Nevaljan unos!")
