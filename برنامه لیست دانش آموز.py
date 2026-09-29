

print(" *** لیست دانش آموز *** ")


parvande = ["anosheh", "takab", "at11", "1375", 12, 13, 14, 15]

while True:
    meno = input("1. Login  2. Sabt-nam  3. Khorooj : ")

    match meno:
        case "1":
            username = input("Username ra vared konid: ")
            password = input("Password ra vared konid: ")

            if username in parvande and password in parvande:
                print("Login shod! Khosh amadid.")
            else:
                print("Etelaat eshtebah ast!")

        case "2":
            esm = input("Nam: ").capitalize()
            famil = input("Famil: ").capitalize()
            user = input("Username: ")
            pas = input("Password: ")
            nomre_python = float(input("Nomre Python: "))
            nomre_java = float(input("Nomre Java: "))
            nomre_html = float(input("Nomre HTML: "))
            nomre_js = float(input("Nomre JS: "))

        
            parvande.append(esm)
            parvande.append(famil)
            parvande.append(user)
            parvande.append(pas)
            parvande.append(nomre_python)
            parvande.append(nomre_java)
            parvande.append(nomre_html)
            parvande.append(nomre_js)

            print("《Sabt-nam ba movafaghiat anjam shod.》")
            print("Parvande:", parvande)

        case "3":
            print("Khodafez!")
            break
              