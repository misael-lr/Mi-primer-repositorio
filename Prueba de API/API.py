import requests

# 1. Hacemos la solicitud a la API
url = "https://official-joke-api.appspot.com/random_joke"
respuesta = requests.get(url)

# 2. Convertimos la respuesta a formato JSON
datos = respuesta.json()

# 3. Mostramos el contenido
print("Aquí tienes un chiste 😄")
print(f"{datos['setup']}")
print(f"{datos['punchline']}")



