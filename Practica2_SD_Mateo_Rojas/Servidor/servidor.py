import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO_ENTRADA = os.path.join(BASE_DIR, "comunicacion", "entrada_servidor.txt")
ARCHIVO_SALIDA = os.path.join(BASE_DIR, "comunicacion", "salida_servidor.txt")


mensajes_procesados = 0

print("====================================")
print("       SERVIDOR INICIADO")
print("====================================")
print("Esperando mensajes del cliente...")
print()

while True:
    try:
        
        with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

      
        if len(lineas) > mensajes_procesados:

            nuevos_mensajes = lineas[mensajes_procesados:]

            for mensaje in nuevos_mensajes:

                mensaje = mensaje.strip()

               
                if mensaje == "":
                    mensajes_procesados += 1
                    continue

                print("Mensaje recibido:", mensaje)

               
                respuesta = mensaje.upper()

                print("Mensaje procesado:", respuesta)

             
                with open(ARCHIVO_SALIDA, "a", encoding="utf-8") as archivo:
                    archivo.write(respuesta + "\n")

                mensajes_procesados += 1

                print("Respuesta enviada al cliente.")
                print("------------------------------------")

    except FileNotFoundError:
        print("Esperando archivos de comunicación...")

    except Exception as error:
        print("Error:", error)

    time.sleep(1)