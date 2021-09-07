import keyboard
from model.matrice import Matrice

#ADDITION MATRICIELLE
def addition_matricielle(matrice_1, matrice_2) :
    matrice_1_name = matrice_1.get_name()
    matrice_1_array = matrice_1.get_array()
    matrice_1_lc = matrice_1.get_lc()

    matrice_2_name = matrice_2.get_name()
    matrice_2_array = matrice_2.get_array()
    matrice_2_lc = matrice_2.get_lc()

    if (matrice_1_lc == matrice_2_lc) :
        result = list(map(lambda x, y: x + y, matrice_1_array, matrice_2_array))
        print("\x1b[1;33mResultat:", result, "\x1b[0m")
    else :
        print("\x1b[1;31mError :", matrice_1_name, "possède un nombre de colonne(s)/ligne(s) différent de ", matrice_2_name, "\x1b[0m")
        print("\x1b[1;31mError :\x1b[0m\x1b[1;32m", matrice_1_name, ":", matrice_1_lc ,"\x1b[0m-\x1b[1;34m", matrice_2_name, ':', matrice_2_lc ,"\x1b[0m")

# SOUSTRACTION MATRICIELLE
def soustraction_matricielle(matrice_1, matrice_2) :
    matrice_1_name = matrice_1.get_name()
    matrice_1_array = matrice_1.get_array()
    matrice_1_lc = matrice_1.get_lc()

    matrice_2_name = matrice_2.get_name()
    matrice_2_array = matrice_2.get_array()
    matrice_2_lc = matrice_2.get_lc()

    if (matrice_1_lc == matrice_2_lc) :
        result = list(map(lambda x, y: x - y, matrice_1_array, matrice_2_array))
        print("\x1b[1;33mResultat:", result, "\x1b[0m")
    else :
        print("\x1b[1;31mError :", matrice_1_name, "possède un nombre de colonne(s)/ligne(s) différent de ", matrice_2_name, "\x1b[0m")
        print("\x1b[1;31mError :\x1b[0m\x1b[1;32m", matrice_1_name, ":", matrice_1_lc ,"\x1b[0m-\x1b[1;34m", matrice_2_name, ':', matrice_2_lc ,"\x1b[0m")


# PRODUIT MATRICIEL
def produit_matriciel(matrice_1, matrice_2) :
    matrice_1_array = matrice_1.get_array()
    matrice_1_lc = matrice_1.get_lc()

    matrice_2_array = matrice_2.get_array()
    matrice_2_lc = matrice_2.get_lc()

    ligne_m1 = matrice_1_lc[0]
    colonne_m1 = matrice_1_lc[1]

    ligne_m2 = matrice_2_lc[0]
    colonne_m2 =matrice_2_lc[1]

    n = 0
    result = []

    if (matrice_1_lc[0] == matrice_2_lc[1] or matrice_1_lc[1] == matrice_2_lc[0]) :
        for z in range(0 , colonne_m2):
            for i in range(0, ligne_m1) :
                for y in range(0, colonne_m1) :

                    number_1 = matrice_1_array[y + (i * colonne_m1)]
                    number_2 = matrice_2_array[(y * ligne_m1) + z]
                    n += number_1 * number_2

                    print(str(number_1) + " x " + str(number_2))
                print("\x1b[1;33m" + str(n) + "\x1b[0m")
                result.append(n)
                n = 0
                print("\x1b[1;31m---\x1b[0m")
        
        print("\x1b[1;32m" + str(result) + " - [" + str(ligne_m1) + "-" + str(colonne_m2) + "]" + "\x1b[0m")

# DIVISION MATRICIELLE
def division_matricielle(matrice_1, matrice_2) :
    matrice_1_array = matrice_1.get_array()
    matrice_1_lc = matrice_1.get_lc()

    matrice_2_array = matrice_2.get_array()
    matrice_2_lc = matrice_2.get_lc()

    ligne_m1 = matrice_1_lc[0]
    colonne_m1 = matrice_1_lc[1]

    ligne_m2 = matrice_2_lc[0]
    colonne_m2 =matrice_2_lc[1]

    n = 0
    result = []

    if (matrice_1_lc[0] == matrice_2_lc[1] or matrice_1_lc[1] == matrice_2_lc[0]) :
        for z in range(0 , colonne_m2):
            for i in range(0, ligne_m1) :
                for y in range(0, colonne_m1) :

                    number_1 = matrice_1_array[y + (i * colonne_m1)]
                    number_2 = matrice_2_array[(y * ligne_m1) + z]
                    n += number_1 / number_2

                    print(str(number_1) + " / " + str(number_2))
                print("\x1b[1;33m" + str(n) + "\x1b[0m")
                result.append(n)
                n = 0
                print("\x1b[1;31m---\x1b[0m")
        
        print("\x1b[1;32m" + str(result) + " - [" + str(ligne_m1) + "-" + str(colonne_m2) + "]" + "\x1b[0m")


#matrice_1 = Matrice("matrice 1", [ 0, 1, 2, 3, 4, 5, 6, 7, 8], [3, 3])
#matrice_2 = Matrice("matrice 2", [ 0, 0, 1, 1, 0, 1, 0, 1, 1], [3, 3])

matrice_1 = Matrice("matrice 1", [ 2, 4 ], [1, 2])
matrice_2 = Matrice("matrice 2", [ 2, 5 ], [2, 1])
input_value = None

# Choix du calcul
while input_value != "addition" and input_value != "multiplication" and input_value != "soustraction" and input_value != "division" :
    input_value = input("Choisir une fonction : ")
if input_value == "addition" :
    addition_matricielle(matrice_1, matrice_2)
elif input_value == "multiplication":
    produit_matriciel(matrice_1, matrice_2)
elif input_value == "soustraction":
    soustraction_matricielle(matrice_1, matrice_2)
elif input_value == "division":
    division_matricielle(matrice_1, matrice_2)



