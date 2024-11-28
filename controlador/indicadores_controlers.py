#Acá las funciones que traer los datos o registran e interactuan con la vista
import requests
def traer_indicadores():
    indicadores=requests.get("https://mindicador.cl/api").json()
    return indicadores