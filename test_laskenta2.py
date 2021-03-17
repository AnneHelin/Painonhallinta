# Sanity2-moduuli testit

# Moduulin lataus
import sanity2

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma Arvo OK
def test_rajatarkastus_oikein():
      assert sanity2.rajatarkastus(100, 20, 300)== [0,'Arvo OK']

 # Arvo alle alarajan, virhekoodi 1, virhesanoma Arvo on alle alarajan (20) 
 def  test_rajatarkastus_alle():
