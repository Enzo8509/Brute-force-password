def test_brute_force():
    code_reference = "Enzo8509$"

    for essai in range(1, 6):
        code = input(f"Essai {essai}, entrez un code : ")
        if code == code_reference:
            print(f"Vous avez entré le bon code : {code}")
            return

    print("veuilez resseyer.")

    
    
    try:
        with open("Users\e624\Desktop\py\enzo.txt", "w") as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print("Le fichier 'enzo.txt' n'a pas été trouvé.")
    
test_brute_force()
