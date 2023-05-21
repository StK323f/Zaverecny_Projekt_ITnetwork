from databaze import Databaze
import os
import time

"""
Spouštění aplikace. pokus
"""

databaze = Databaze

def menu():
    """
    Textová reprezentaci úvodního menu s volbami 1-4.
    """
    #time.sleep(3)  # program se na 3 vteřiny zastaví ("uspí")
    os.system('cls' if os.name == 'nt' else 'clear') #vymaže obrazovku

    print("----------------------------")
    print("Evidence pojištěných")
    print("----------------------------")
    print()
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěnou osobu")
    print("4 - Editovat data pojištěnce")
    print("5 - Smazat pojištěnce")
    print("6 - Konec")
    cislo_akce = kontrola_volby("", "Neplatné zadání! Zvolte 1 - 6!\n")
    zvol_si(cislo_akce)


def kontrola_volby(text_zadani, text_chyba):
    """
    Kontrola správnosti vstupu uživatele. Správné hodnoty pouze 1-6.
    """

    while True:
        try:
            cislo = int(input(text_zadani))
            if cislo < 1 or cislo > 6:
                raise ValueError
            else:
                return cislo
        except ValueError:
            print(text_chyba)



def zvol_si(cislo_akce):
    """
    Volba funkce databáze.
    """
    if cislo_akce == 1:
        databaze.pridej_pojistence(Databaze)
        menu()
    elif cislo_akce == 2:
        databaze.vypis_pojistence(Databaze)
        menu()
    elif cislo_akce == 3:
        databaze.vyhledej_pojistence(Databaze)
        menu()
    elif cislo_akce == 4:
        databaze.edituj_pojistence(Databaze)
        menu()
    elif cislo_akce == 5:
        databaze.smaz_pojistence(Databaze)
        menu()
    else:
        print("Děkujeme za použití aplikace na evidenci pojištěnců.")
        exit()


menu()
