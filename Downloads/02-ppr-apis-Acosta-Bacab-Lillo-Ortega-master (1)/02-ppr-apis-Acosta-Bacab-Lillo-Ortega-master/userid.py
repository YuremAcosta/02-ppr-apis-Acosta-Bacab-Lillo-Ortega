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

        print("Carrito ganador:", ganador["id"])
        print("Cantidad de productos válidos:", mayor)
        print("ID del usuario ganador:", user_id)

       
        url = f"https://dummyjson.com/users/{user_id}"
        respuesta_usuario = requests.get(url)

      
        if respuesta_usuario.status_code == 200:
            usuario = respuesta_usuario.json()

            print("Datos del usuario obtenidos correctamente")
            print("Nombre:", usuario["firstName"])
            print("Apellido:", usuario["lastName"])
            print("Ciudad:", usuario["address"]["city"])

        else:
            print("Error al obtener los datos del usuario")

else:
    print("Error al obtener los carritos")
