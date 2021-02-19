'''
    Painonhallintasovelluksen pääohjelma
    Huolehtii syötteen lukemisesta ja tulosten näyttämisestä

'''

# Kirjastojen ja modulien lataukset


# Pääohjelmat omat luokkat, funktiot ja kirjastokomponentien alustukset

# Pääohjelma ikuinen silmukka
jatketaan = 'K'
while True:
    while virhekoodi != 0:
        paino_str = input('Paino kiloina: ')
   
    pituus_str = input('Pituus metreiinä: ')
    ika_str = input('ikä vuosina: ')
    sukupuoli_str = input('Nainen 0, Mies 1 ')
    jatketaan = input('Haluatko jatkaa K/e? ')

    # TODO: tee rutiini oletusarvolle K
    pass
    if jatketaan != 'K':
        break
