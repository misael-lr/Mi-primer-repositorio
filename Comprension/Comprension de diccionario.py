# diccionario = {key: expresion for (key, value) in iterable}
# diccionario = {key: expresion for (key, value) in iterable if condicion}
# diccionario = {key: (if/else) for (key, value) in iterable}
# diccionario = {key: function(value) for (key, value) in iterable}

ciudades_en_F = {"Chicago": 30, "Boston": 40, "Colombia": 24, "Santo Domingo": 31}

ciudades_en_C = {key: round((value-32)*(5/9)) for (key, value) in ciudades_en_F.items()}
print(ciudades_en_C)


clima = {"New York": 'Nieve', "Boston": 'Soleado', "Los Angeles": 'Soleado', "Brooklyn": 'Lluvioso', "Chicago": 'Nublado'}

clima_soleados = {key: value for (key, value) in clima.items() if value == "Soleado"}
print(clima_soleados)

clima_nieve = {key: value for (key, value) in clima.items() if value == "Nieve"}
print(clima_nieve)

clima_nublado = {key: value for (key, value) in clima.items() if value == "Nublado"}
print(clima_nublado)

clima_lluvioso = {key: value for (key, value) in clima.items() if value == "Lluvioso"}
print(clima_lluvioso)


clima = {"Chicago": 30, "Boston": 40, "Colombia": 24, "Santo Domingo": 31}
clima_2 = {key: ("Calor" if value >= 40 else "Frio") for (key, value) in clima.items()}
print(clima_2)


def check_temp(value):
    if value >= 70:
        return "Calor"
    elif 60 >= value >= 40:
        return "Normal"
    else:
        return "Frio"


ciudades = {"Chicago": 30, "Boston": 40, "Colombia": 24, "Santo Domingo": 31}
clima_ciudades = {key: check_temp(value) for (key, value) in ciudades.items()}
print(clima_ciudades)

