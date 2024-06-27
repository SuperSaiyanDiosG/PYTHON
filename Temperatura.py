import requests
def obtener_temperatura(ciudad):
    url = "http://wttr.in/" + ciudad + "?format=3"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print (respuesta.text)
    else:
        print("verifica el nombre de la ciudad")
ciudad = input("ciudad?: ")
obtener_temperatura(ciudad)