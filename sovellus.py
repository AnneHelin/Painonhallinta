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

# Varsinaisen pääohjelman alku

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
while True:

    # Kysytään käyttäjältä paino
    tapahtui_virhe = True
    while tapahtui_virhe = True:
        paino_str = input('Paino (kg)? ')
        tulokset = sanity2.liukuluvuksi(paino_str)
        if tulokset [0] == 0:
            paino = tulokset [2]
            tapahtui_virhe = False
        else:
            print(tulokset[1])
    # Testi
    print('Ja paino oli', paino, 'kg')

    """
    pituus_str = input ('Pituus (m)?')
    pituus =

    print('Painoindeksi on')
    """