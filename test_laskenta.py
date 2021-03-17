# Modulin laskenta.py testit

# Modulien ja kirjastojen lataukset
import laskenta

# Ensimmäinen testi lasketaan painoindeksi ja verrataan tulosta ennalta laskettuun arvoon
def test_painoindeksi():
    assert laskenta.bmi(50, 1.50) == 20
 