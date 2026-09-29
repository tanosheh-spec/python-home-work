list_nomre = []

while True:
	student = input(" 1. miyangin 2. khoroj ")
	match student:
		case "1":
			esm = input(" esm: ").capitalize()
			famil = input(" famil: ").capitalize()
			n_java = float(input(" n_java: "))
			n_html = float(input(" n_html: "))
			n_python = float(input(" n_python: "))
			miyangin = (n_java + n_html + n_python) / 3
			
			etelaat = [esm, famil, n_java, n_html, n_python, miyangin]
			list_nomre.append(etelaat)
			print(" etelaat sabt shod: ", etelaat)
			
		case "2":
			print(" khorooj ")
			print(list_nomre)
			break
