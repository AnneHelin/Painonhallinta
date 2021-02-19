'''
Moduuli, jonka funktioilla tarkistetaan syötteen järkevyys
Sisältää joukon funktioita, jota käyttämällä saadaan:
1. virhekoodi (int),2. virhesanoma (string) ja 3. arvo (float)
Funktiot palauttavat nämä tiedot listana
'''

# Kirjastojen lataukset 


# Luokkien ja funktioiden määritykset
def liukuluku_syote(syote):
    """Tutkii onko syöte sopiva liukiluvuksi

    Args:
        syote (string): näppäimistöltä syötetty arvo 

    Returns:
        list: virhekoodi (int),sanoma (string), arvo (float)
    """
    syote = syote.strip() # Poistetaan tulostumattomat merkit molemmista päistä
    if syote.find(',') !=-1: # Katsotaan sisältääkö pilkkuja
        syote = syote.replace(',', '.') # Korvataan pilkut pisteellä
    if syote.find(',') ! = -1:  # Katsottan löytyykö pistettä
        osat = syote.split('.') # Luodaan lista jossa pisteellä erotetut osat syötteellä
        if len(osat) > 2:
            arvo = 0
            virhekoodi = 1
            virhesanoma = 'Syötteessä useita desimaalierottimia' 

    else :
        if syote.isnumeric()
            arvo = float(syote)
            virhekoodi = 0
            virhesanoma = 'Syöte OK'


    return tulokset
 pass   


# Koodi, joka suoritetaan vain jos tämä tiedosto käynnistetään konsolista, esim "testit"