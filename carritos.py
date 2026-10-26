import requests


response = requests.get("https://dummyjson.com/carts")

if response.status_code == 200:
  datos = response.json()


  totales_por_carrito = {}

  for carrito in datos["carts"]:
    suma_valida = 0
    for producto in carrito["products"]:
     
      if producto["discountPercentage"] < 12:
        suma_valida += producto["quantity"]

    totales_por_carrito[carrito["id"]] = suma_valida

  
  print(totales_por_carrito)