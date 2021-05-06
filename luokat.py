# Tässä modulissa määritellään luokat painonhallintasovellukseen

# Modulien ja kirjastojen lataukset


# Henkilö-luokka

class Henkilo:
    """Yliluokka kaikille henkilötyypeille"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):

        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
        return bmi

    @staticmethod
    def bmi(pituus, paino):
        bmi = paino / (pituus/100)**2
        return bmi

class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii Henkilo-luokan ominaisuudet
    ja metodit
    """
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        self.tavoitepaino = tavoitepaino

    def rasvaprosentti(self):
        rasvaprosentti = 1.2 * self.painoindeksi() + 0.23 * self.ika - 10.8 * self.sukupuoli - 5.4
        return rasvaprosentti
# Tehtävä 1
class Lapsi(Henkilo):
    """Henkilöluokan aliluokka lapsille."""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        
    def rasvaprosentti(self):
        rasvaprosentti = 1.51 * self.painoindeksi() - 0.70 * self.ika - 3.6 * self.sukupuoli + 1.4
        return rasvaprosentti    


if __name__ == "__main__":
    anneh = Henkilo('Anne', 'Helin', 150, 50, 43, 0)
    print('Henkilö painaa', anneh.paino)

    anneh.painoindeksi()

    anneh2 = Aikuinen('Anne', 'Helin', 150, 50, 43, 0, 70)
    print(anneh2.etunimi, 'painoindeksi', anneh2.painoindeksi())
    print(anneh2.etunimi, 'rasvaprosentti', anneh2.rasvaprosentti())

    # Lasketaan painoindeksi staattisella metodilla
    pituus = 150
    paino = 50
    
    print('Painoindeksi on', Henkilo.bmi(pituus, paino))
