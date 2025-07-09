
import hashlib

hash_file = "c0535e4be2b79ffd93291305436bf889314e4a3faec05ecffcbb7df31bf7e2b9"

dic_file = input("Ingresa la direccion del diccionario: ")

with open(dic_file, 'r') as file:

    diccionario = [linea.strip() for line in file]

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:

            print("La contraseña original es: " + password)
            break
        else:
            print("La contraseña no se encuentra en el diccionario")    