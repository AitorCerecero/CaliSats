import time

User = "Via003"
PWD = "Viasat3"

print("Bienvenido al Sistema Satelital Viasat")
# Simula la entrada del usuario
user = User
pwd = PWD

if user == User and pwd == PWD:
    print("Bienvenido al Control de Mision de Viasat")
    # Simula la opción seleccionada por el usuario
    opciones = [1, 2, 3, 4]
    for op in opciones:
        if op == 1:
            print("Obteniendo Datos de los Satelites... Espera un momento")
            time.sleep(5)
            print("Datos Listos")
            print("""
            Nombre: AnikF F2
            Coordenadas: 111.1
            Longitud: Oeste
            Estado: Saludable, Sin Detalles
            """)
            print("""
            Nombre: Wildblue 1
            Coordenadas: 111.1
            Longitud: Oeste
            Estado: Saludable, Sin Detalles
            """)
            print("""
            Nombre: Viasat 1 Mexico
            Coordenadas: 115.1
            Longitud: Oeste
            Estado: Saludable, Sin Detalles
            """)
            print("""
            Nombre: Viasat 2 Russia
            Coordenadas: 69.9
            Longitud: Oeste
            Estado: Saludable, Sin Detalles
            """)
            print("""
            Nombre: Viasat 3
            Coordenadas: 89.9
            Longitud: Oeste
            Estado: Requiere Actualizacion
            """)
        elif op == 2:
            print("Verificando punteo de Antena... Espera un momento")
            time.sleep(3)
            print("Punteo Correcto, Antenas de Central Terrestre apuntadas a los Satelites, Sistemas en Linea")
        elif op == 3:
            print("Iniciando Actualización del OS... Espera un momento")
            time.sleep(10)
            print("Actualización Completada, Sistema Orbital en Linea de nuevo")
        elif op == 4:
            print("Sesion Cerrada")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
else:
    print("Intenta de nuevo")
