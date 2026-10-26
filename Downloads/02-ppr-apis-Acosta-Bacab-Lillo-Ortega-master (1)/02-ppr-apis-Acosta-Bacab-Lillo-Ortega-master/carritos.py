import requests
response = requests.get("https://dummyjson.com/carts")

if response.status_code == 200:
  datos = response.json()

  totales_por_carrito = {}
  suma_total_general = 0

  print("=== REPORTE DE PRODUCTOS VÁLIDOS POR CARRITO (Descuento < 12%) ===\n")

  for carrito in datos["carts"]:
    carrito_id = carrito["id"]
    user_id = carrito["userId"]
    suma_valida = 0

    for producto in carrito["products"]:
      # Condición: descuento menor a 12%
      if producto["discountPercentage"] < 12:
        suma_valida += producto["quantity"]

    totales_por_carrito[carrito_id] = suma_valida
    suma_total_general += suma_valida

    # Mostrar por carrito y usuario cuántos productos aplican
    print(
        f"Carrito ID: {carrito_id} | Usuario ID: {user_id} | Productos"
        f" válidos: {suma_valida}"
    )

  print("=" * 65)
  print(
      f"Suma total general de productos con descuento < 12%:"
      f" {suma_total_general}"
  )
  print("=" * 65)

else:
  print("Error al conectar con la API:", response.status_code)