# Moduulin funktioilla voidaan laske PAINOINDEKSI (BMI) ja kehon rasvaprosentti

# Funktion määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """Laske painoindeksin kaavalla paino jaettuna pituuden neliöllä

    Args:
        paino (kg): paino kiloina (kg)
        pituus (cm): pituus senttimetreinä (cm)

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
        pituus = 150
        paino =   50
        omabmi = bmi(paino, pituus)
        print('Pituus', pituus, 'Paino', paino, 'Painoindeksi', omabmi) 

        # 2. testi oma rasvaprosentti
        ika = 43
        sukupuoli = 0
        print('Rasvaprosentti:', rasvaprosentti(omabmi, ika, sukupuoli))      
    
    # Aikuisen rasvaprosenti
    if ika>= 18:
        rprosentti = 1.2 * bmi + 0,23 * ika - 10.8 * sukupuoli - 5.4
    else:

    # Lapsen rasvaprosentti
    def lapsen rasvaprosentti(bmi, ika, sukupuoli)
        """[summary]
        
        Args:
            bmi (float): painoiindeksi
            ika (float):ika vuosina
            sukupuoli (float): 1 Miehet , 0 Naiset

        Returns:
            float: lapsen rasvaprosentti
        """
        rprosentti = 1.5 * bmi - 0,7 * ika - 3.6 * sukupuoli + 1,4
        return rprosentti
        
        
        
        
        
        
        
        pituus = 120
        paino = 18
        print('Rasvaprosentti:', rasvaprosentti() )