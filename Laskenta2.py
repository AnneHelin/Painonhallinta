# Moduulin funktioilla voidaan laske PAINOINDEKSI (BMI) ja kehon rasvaprosentti

# Funktion määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """Laske painoindeksin kaavalla paino jaettuna pituuden neliöllä

    Args:
        paino (float): paino kiloina (kg)
        pituus (float): pituus metreinä (m)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / pituus ** 2

# Aikuisen rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
        """[summary]

        Args:
            bmi (float): painoindeksi
            ika (float): ika vuosina
            sukupuoli (float): 1 Miehet , 0 naiset
        
        Returns:
            float: kehon rasvaprosentti
        """
        rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
        return rprosentti

 # Testit
 if __name__=='_main_':

        # 1. testi oma painoindeksi
        pituus = 1,50
        paino =   50
        omabmi = bmi(paino, pituus)
        print('Pituus', pituus, 'Paino', paino, 'Painoindeksi', omabmi) 

        # 2. testi oma rasvaprosentti
        ika = 43
        sukupuoli = 0
        print('Rasvaprosentti:', rasvaprosentti(omabmi, ika, sukupuoli))      