"""Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost"""

import re

re_mail = r"^[a-zA-Z]+\.[a-zA-Z]+\@fpmoz\.sum\.ba$"
re_edu = r"^[a-zA-Z][a-zA-Z]+[0-9]?\@sum\.ba$"

while True:
    unos_mail = input("Unesi e-mail: ")
    unos_edu = input("Unesi edu id: ")
    provjera_mail = re.search(re_mail, unos_mail)
    provjera_edu = re.search(re_edu, unos_edu)
    if provjera_mail and provjera_edu:
        print("Valjan unos")
        break
    else:
        print("Nevaljan unos!")
