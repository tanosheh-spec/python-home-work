

import random

afrad = ["ali", "amir", "raha", "sara"]
jaize = ["kart pool", "seke", "mobil", "laptap"]

random.shuffle(jaize)

j = 0
while j < len(afrad):
    print(afrad[j] + " barande : " + jaize[j])
    j += 1
