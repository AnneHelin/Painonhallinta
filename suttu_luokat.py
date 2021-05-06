# Luokka ja olioharjoituksia

# Luokka lintujenn tietojen tallennukseen

class Lintu:
    def __init__(self, nimi, tieteellinen_nimi, ravinto):
        self.nimi = nimi
        self.tieteellinen_nimi = tieteellinen_nimi
        self.ravinto = ravinto

    def aani(self, aani):
        print ('Sanoo' , aani)    

lintu = Lintu('korppi', 'corvus corax', 'raadot')

print(lintu.nimi, 'on tieteelliseltä nimeltään' , lintu.tieteellinen_nimi)
lintu.aani('kraak, kraak')

class Kahlaaja(Lintu):
    def __init__(self, nimi, tieteellinen_nimi, ravinto):
        super().__init__(self, nimi, tieteellinen_nimi, ravinto)
        self.laji = 'kahlaaja'

kahlaaja = Kahlaaja('Kurki', 'Grus Grus' , 'sammakoita')

print(kahlaaja.nimi, 'on' , kahlaaja.laji, 'ja se syö' , kahlaaja.ravinto)

# Auto- luokka yliluokka erilaisille autotyypeille

# Ominaisuudet (Field, Property) merkki, malli, vuosimalli, kilometrit, käyttövoima, vaihteistotyyppi, väri ja päästöt

class Auto():
    # Oliomuodstin eli  konsruktio
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot):
        """Auto-luokka mallinen auto-olioille yliluokka eri autotyypeille

        Args:
            rek (string): Auton rekisterinumero  esim. CPM-186
            merkki (string): Auton valmistaja
            malli (string): Tyyppimerkki
            vm (integer): Vuosimalli
            km (integer): Ajetut kilometrit
            kvoima (string): Käyttövoima: diesel, bensiini, hybridi, sähkö, kaasu, vety
            vaihteisto (string): Vaihteiston tyyppi: käsi, automaatti
            vari (string): Auton vari
            paastot (integerr): Hiilidioksidipäästöt g/km
        """
        self.rek = rek
        self.merkki = merkki
        self.malli = malli
        self.vm = vm
        self.kvoima = kvoima
        self.vaihteisto = vaihteisto
        self.vari = vari
        self.paastot = paastot

    
