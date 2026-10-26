import requests

respuesta = requests.get("https://dummyjson.com/carts")

if respuesta.status_code == 200:
  datos = respuesta.json()
  carritos = datos["carts"]

  mayor = 0
  ganador = None

  for carrito in carritos:
    suma = 0
    for producto in carrito["products"]:
      if producto["discountPercentage"] < 12:
        suma += producto["quantity"]

    if suma > mayor:
      mayor = suma
      ganador = carrito

  if ganador is not None:
    user_id = ganador["userId"]

    url = f"https://dummyjson.com/users/{user_id}"
    respuesta_usuario = requests.get(url)

    if respuesta_usuario.status_code == 200:
      usuario = respuesta_usuario.json()

      nombre = usuario["firstName"]
      apellido = usuario["lastName"]
      ciudad = usuario["address"]["city"]

      reporte = (
          f"El cliente con más productos regulares es {nombre} {apellido}"
          f" (ID: {user_id}), de la ciudad de {ciudad}. Compró un total de"
          f" {mayor} productos válidos."
      )

      print("=" * 70)
      print("REPORTE DE AUDITORÍA DE DESCUENTOS")
      print("=" * 70)
      print(reporte)
      print("=" * 70)

      with open("reporte_auditoria.txt", "w", encoding="utf-8") as archivo:
        archivo.write(reporte)

      print("\n¡Archivo 'reporte_auditoria.txt' generado con éxito!")

    else:
      print("Error al obtener los datos del usuario")
  else:
    print("No se encontró un carrito ganador")

else:
  print("Error al obtener los carritos")