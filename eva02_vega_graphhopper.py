import requests

# ================================
# Configuración inicial
# ================================
API_KEY = "87427e2b-f8cd-4df1-857b-d6819cfecaf3"
URL = "https://graphhopper.com/api/1/route?point=-33.0424,-71.3726&point=-33.0246,-71.5496&vehicle=car&locale=es&key=87427e2b-f8cd-4df1-857b-d6819cfecaf3"

print("=== Programa de Geolocalización con GraphHopper ===")
print("Este programa calculará la ruta desde tu casa hasta tu sede.\n")

# ================================
# Bucle principal
# ================================
while True:
    origen = input("📍 Ingresa el punto de origen (o escribe 's' o 'salir' para terminar): ")
    if origen.lower() in ["s", "salir"]:
        print("👋 Programa finalizado. ¡Hasta luego!")
        break

    destino = input("📍 Ingresa el punto de destino: ")

    # Parámetros para la API
    params = {
        "key": API_KEY,
        "q": f"{origen} to {destino}",
        "locale": "es",        # para que las instrucciones estén en español
        "profile": "car",      # modo de transporte (auto)
        "instructions": "true" # pedir pasos del viaje
    }

    # Llamar a la API
    response = requests.get(URL, params=params)

    if response.status_code != 200:
        print("❌ Error al obtener la ruta. Verifica tu token o los lugares ingresados.")
        continue

    data = response.json()

    # Obtener distancia y tiempo
    distancia_metros = data["paths"][0]["distance"]
    tiempo_ms = data["paths"][0]["time"]

    # Convertir unidades
    distancia_km = distancia_metros / 1000
    tiempo_min = tiempo_ms / 60000

    print("\n🗺️ Resultados del viaje:")
    print(f"Distancia total: {distancia_km:.2f} km")
    print(f"Duración estimada: {tiempo_min:.2f} minutos\n")

    # Mostrar narrativa paso a paso
    print("➡️ Instrucciones del viaje:")
    for i, paso in enumerate(data["paths"][0]["instructions"], start=1):
        texto = paso["text"]
        distancia_paso = paso["distance"] / 1000
        print(f"{i}. {texto} ({distancia_paso:.2f} km)")

    print("\n✅ Ruta completada con éxito.\n")
