import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO_ENTRADA = os.path.join(BASE_DIR, "comunicacion", "entrada_servidor.txt")
ARCHIVO_SALIDA = os.path.join(BASE_DIR, "comunicacion", "salida_servidor.txt")

print("====================================")
print("          CLIENTE INICIADO")
print("====================================")

while True:

    mensaje = input("\nIngrese un mensaje (o 'salir' para terminar): ")

    if mensaje.lower() == "salir":
        print("Cliente finalizado.")
        break

    if mensaje.strip() == "":
        print("No puede enviar un mensaje vacío.")
        continue


    try:
        with open(ARCHIVO_SALIDA, "r", encoding="utf-8") as archivo:
            respuestas_anteriores = archivo.readlines()
    except FileNotFoundError:
        respuestas_anteriores = []

    cantidad_anterior = len(respuestas_anteriores)


    with open(ARCHIVO_ENTRADA, "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")

    print("Mensaje enviado al servidor.")
    print("Esperando respuesta...")

    time.sleep(2)

    respuesta_recibida = False

    for intento in range(10):

        try:
            with open(ARCHIVO_SALIDA, "r", encoding="utf-8") as archivo:
                respuestas = archivo.readlines()

            if len(respuestas) > cantidad_anterior:
                respuesta = respuestas[-1].strip()

                print("\nRespuesta del servidor:")
                print(respuesta)

                respuesta_recibida = True
                break

        except FileNotFoundError:
            pass

        time.sleep(1)

    if not respuesta_recibida:
        print("No se recibió respuesta del servidor.")