# Rutiineja tietojen kysymiseen käyttäjältä

# Kirjastojen ja modulien lataukset
import sanity2

# Funktioiden määrittelyt

def kysy_liukuluku(kysymys, alaraja, ylaraja):
    """Kysyy käyttäjältä liukuluvun tai kokonaisluvun ja tarkistaa syötteen oikean tietotyypin ja suuruuden

    Args:
        kysymys (str): Käyttäjälle esitettävä kysymys
        alaraja (float]: pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns:
        float: käyttäjän syöttämä arvo liukulukuna
    """
    # Kysytään käyttäjältä tietoa, kunnes saadaan järkevä arvo
    luku = 0
    tapahtui_virhe = True

    while tapahtui_virhe == True:
        
        # Esitetään parametrina annettu kysymys ja tallennetta vastaus
        vastaus_str =input(kysymys + '')

        # Tarkistetaan 