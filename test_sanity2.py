# Sanity2-modulin testit

# Modulin lataus
import sanity2

# RAJA-ARVOTARKASTUSTEN TESTIT

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma Arvo OK
def test_rajatarkastus_oikein():
    assert sanity2.rajatarkistus(100, 20, 300)== [0, 'Arvo OK']
 
# Arvo alle alarajan, virhekoodi 1, virhesanoma Arvo on alle alarajan (20)
def test_rajatarkastus_alle():
    assert sanity2.rajatarkistus(10, 20, 300)== [1, 'Arvo on alle alarajan']

# Arvo 
def test_rajatarkastus_yli():
    assert sanity2.rajatarkastus(350, 20, 300)== [2, ' Arvo on yli ylärajan(300)']

# LIUKULUKUMUUNNOS TESTIT

# Syötteenä kokonaisluku, virhekoodi 0, virheilmoitus Syöte OK, arvo liukulukuna
def test_liukuluku_kokonaisluku():
    assert sanity2.liukuluvuksi('15') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa desimaalipiste
def  test_liukuluku_liukuluku():
     assert sanity2.liukuluvuksi('15.0') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa desimaalipilkku: automaattinen korjaus
def test_liukuluku_liukuluku():    
    assert sanity2.liukuluvuksi('15.0') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa useampi desimaalipiste: virhe
def test_liukuluku_monta_pistetta():
    assert sanity2.liukuluvuksi('15.0.7') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa useampi desimaalipilkku: virhe
def test_liukuluku_monta_pilkkua():
    assert sanity2 .liukuluvuksi ('15,0,7') == [1, 'Syöte sisältää useita erottimia. Vain yksi arvo sallittu',

# Syötteessä mukana kirjaimia lopussa: virhe
def test_liukuluku_kirjaimia_lopusssa():
    assert sanity2.liukuluvuksi('15.0 kg') == [0, 'Syöte OK', 15.0]

# Syötteessä mukana kirjaimia alussa: virhe    
def test_liukuluku_kirjaimia_alussa():
    assert sanity2.liukuluvuksi('paino 15.0') == [3, 'Ennen desimaalierotinta ylimääräisiä merkkejä. vain numerot ja desimaalipiste on sallittu', 0]
 
# Syöte pelkkää tekstiä, ei numeroita: Virhe
def test_liukuluku_tekstia():
    assert sanity2.liukuluvuksi('sata') == [2,' Syötteessä ylimääräisiä merkkejä: vain numerot ja desimaalipisteet sallittu', 0]
    