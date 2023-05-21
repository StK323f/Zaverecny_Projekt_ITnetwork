class Pojistenec:
    """
    Třída pro vytvoření nových pojištěnců.
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Slouží k inicializaci instance pojištěného.
        :param jmeno: Křestní jméno (nesmí obsahovat čísla a spec. znaky?)
        :param prijmeni: Příjmení (nesmí obsahovat čísla a spec. znaky?)
        :param vek: Věk pojištěného (0<vek<110; nesmí obsahovat písmena a spec. znaky)
        :param telefon: Tel. číslo pojištěného (předvolba? min a max délka 9 pozic a pouze čísla)
        """
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._telefon = telefon

    def __str__(self):
        """
        Textová reprezentace pojištěného.
        """
        return f"{self._jmeno}\t\t{self._prijmeni}\t\t{self._vek}\t\t{self._telefon}"