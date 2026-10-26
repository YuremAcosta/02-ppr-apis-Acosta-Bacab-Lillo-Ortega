import json
import requests

url = "https://dummyjson.com/carts"
carritos = requests.get(url)


if carritos.status_code == 200:
  datos_json = carritos.json()
  print("=== DATOS DE LOS CARRITOS EXTRAÍDOS EXITOSAMENTE ===\n")
  print(json.dumps(datos_json))
  
else:
  print(f"Error en la petición. Código de estado: {carritos.status_code}")