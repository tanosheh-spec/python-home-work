

"""
import random

harf_khochak = tuple("abcdefghijklmnopqrstuvwxyz")
harf_bozorg = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
adad = tuple("0123456789")
alaem = tuple("!@#$%^&*()-_=+")

alaem = harf_khochak + harf_bozorg + adad + alaem

password = (random.choice(harf_khochak), random.choice(harf_bozorg), random.choice(adad), random.choice(alaem))

for i in range(14):
    password += (random.choice(alaem),)

password_list = list(password)
random.shuffle(password_list)
final_password = "".join(password_list)

print("پسورد:", final_password)
"""

print("#######################")


import random

harf_kochik = tuple("abcdefghijklmnopqrstuvwxyz")
harf_bozorg = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
adad = tuple("0123456789")
alaem = tuple("!@#$%^&*()-_=+")

ozv = harf_kochik + harf_bozorg + adad + alaem

password = [random.choice(harf_kochik), random.choice(harf_bozorg), random.choice(adad), random.choice(alaem)]

for i in range(18):
    password.append(random.choice(ozv))

random.shuffle(password)

ramz_nahayi = ""
for i in password:
    ramz_nahayi = ramz_nahayi + i

print("password:", ramz_nahayi)
