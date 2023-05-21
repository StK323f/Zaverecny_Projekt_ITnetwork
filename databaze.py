from pojistenec import Pojistenec


class Databaze:

    #Třída pro práci s databází pojištěných.

    databaze_pojistencu = [
        Pojistenec("Jan", "Novák", 30, "123456789"),
        Pojistenec("Petr", "Svoboda", 25, "987654321"),
        Pojistenec("Marie", "Nováková", 40, "555666777"),
        Pojistenec("Štěpán", "Kubín", 45, "725648620"),
        Pojistenec("Jan", "Kubín", 12, "706123566")]

    def __init__(self):
        pass

    def pridej_pojistence(self):
        # zadání vstupů
        jmeno = input("Zadejte křestní jméno pojištěnce:\n")
        prijmeni = input("Zadejte příjmení pojištěnce:\n")
        vek = self.nacti_cele_cislo("Zadejte věk pojištěnce:\n", "Zadání není číslo!")
        telefon = self.nacti_cele_cislo("Zadejte telefonní číslo pojištěnce (bez + a bez mezer, pouze čísla):\n", "Zadání není číslo!")
        self.databaze_pojistencu.append(Pojistenec(jmeno, prijmeni, vek, telefon))
        input("Data byla uložena. Pokračujte stiskem libovolné klávesy...")
        # back to menu


    def nacti_cele_cislo(text_zadani, text_chyba):  # uživateli vzdorná funkce na zadávání čísla
        spatne = True
        while spatne:
            try:
                tel_cislo = int(input(text_zadani))
                spatne = False
            except ValueError:
                print(text_chyba)
            else:
                return tel_cislo

    def vypis_pojistence(self):
        if len(self.databaze_pojistencu) == 0:
            print("Seznam pojištěných je prázdný.")
        else:
            print("----------------------------")
            print("Výpis pojištěnců")
            print("----------------------------")
            print()
            for pojisteny in self.databaze_pojistencu:
                print(pojisteny)
            print()
            input("Pokračujte libovolnou klávesou...")
            # back to menu

    def hledani(self):
        hledane_jmeno = input("Zadejte křestní jméno hledaného pojištěnce:\n")
        hledane_prijmeni = input("Zadejte příjmení hledaného pojištěnce:\n")
        hledany_index = None
        for i, pojisteny in enumerate(self.databaze_pojistencu):
            if pojisteny._jmeno == hledane_jmeno and pojisteny._prijmeni == hledane_prijmeni:
                hledany_index = i
        return hledany_index

    def vyhledej_pojistence(self):
        hledany_index = self.hledani(self)
        if hledany_index == None:
            print("Hledaný pojištenec není v databázi.")
        else:
            print("----------------------------")
            print("Data hledaného pojištěnce")
            print("----------------------------")
            print()
            print(self.databaze_pojistencu[hledany_index])
        print()
        input("Pokračujte libovolnou klávesou...")
        #back to menu

    def edituj_pojistence(self):
        hledany_index = self.hledani(self)
        if hledany_index == None:
            print("Udaný pojištěnec není v databázi.")
        else:
            print("----------------------------")
            print(f"Editujete pojištěnce {self.databaze_pojistencu[hledany_index]._jmeno} {self.databaze_pojistencu[hledany_index]._prijmeni}.")
            print("----------------------------")
            print()
            self.databaze_pojistencu[hledany_index]._jmeno = input("Zadejte nové jméno pojištěnce:\n")
            self.databaze_pojistencu[hledany_index]._prijmeni = input("Zadejte nové příjmení pojištěnce:\n")
            self.databaze_pojistencu[hledany_index]._vek = self.nacti_cele_cislo("Zadejte nový věk pojištěnce:\n", "Zadání není číslo!")
            self.databaze_pojistencu[hledany_index]._telefon = self.nacti_cele_cislo("Zadejte nové telefonní číslo pojištěnce (bez + a bez mezer, pouze čísla):\n", "Zadání není číslo!")
            print()
            input("Pokračujte libovolnou klávesou...")
            # back to menu

    def smaz_pojistence(self):
        hledany_index = self.hledani(self)
        if hledany_index == None:
            print("Hledaný pojištenec není v databázi.")
        else:
            print("----------------------------")
            print(f"Chystáte se smazat pojištěnce: {self.databaze_pojistencu[hledany_index]._jmeno} {self.databaze_pojistencu[hledany_index]._prijmeni}!")
            print("----------------------------")
            rozhodnuti = self.dotaz(self)
            if rozhodnuti:
                print(f"Pojištěnec {self.databaze_pojistencu[hledany_index]._jmeno} {self.databaze_pojistencu[hledany_index]._prijmeni} byl úspěšně smazán.")
                del self.databaze_pojistencu[hledany_index]
            else:
                pass

        input("Pokračujte libovolnou klávesou...")
        # back to menu

    def dotaz(self):  # funkce, která umožní zadat pouze znaky y,Y, n a N
        nezadano = True
        while nezadano:
            odpoved = input("\nOpravdu to chcete udělat? a / n: ")
            if (odpoved == "a" or odpoved == "A"):
                return True
            elif (odpoved == "n" or odpoved == "N"):
                return False
            else:
                pass