import sys
import json
from muebles import Silla, Mesa, Armario, Inventario

INVENTARIO_FILE = "inventario.json"

def cargar_inventario():
    """Carga el inventario desde el archivo JSON."""
    try:
        with open(INVENTARIO_FILE, "r") as f:
            datos = json.load(f)
            inventario = Inventario()
            for item in datos:
                tipo = item["tipo"]
                material = item["material"]
                precio = item["precio"]

                if tipo == "silla":
                    mueble = Silla(material, precio, respaldo=True)
                elif tipo == "mesa":
                    mueble = Mesa(material, precio, "Mediano")
                elif tipo == "armario":
                    mueble = Armario(material, precio, 2)
                else:
                    continue
                
                inventario.agregar_mueble(mueble)
            return inventario
    except (FileNotFoundError, json.JSONDecodeError):
        return Inventario()

def guardar_inventario(inventario):
    """Guarda el inventario en un archivo JSON."""
    datos = []
    for mueble in inventario.muebles:
        datos.append({
            "tipo": mueble.__class__.__name__.lower(),
            "material": mueble.material,
            "precio": mueble.precio
        })
    
    with open(INVENTARIO_FILE, "w") as f:
        json.dump(datos, f, indent=4)

def main():
    inventario = cargar_inventario()

    if len(sys.argv) < 2:
        print("Uso: python cli.py [agregar|mostrar|guardar|cargar|descuento] <args>")
        return

    comando = sys.argv[1]

    if comando == "agregar" and len(sys.argv) >= 4:
        tipo = sys.argv[2].lower()
        material = sys.argv[3]
        precio = float(sys.argv[4])

        if tipo == "silla":
            mueble = Silla(material, precio, respaldo=True)
        elif tipo == "mesa":
            mueble = Mesa(material, precio, "Mediano")
        elif tipo == "armario":
            mueble = Armario(material, precio, 2)
        else:
            print("Tipo de mueble no válido.")
            return

        inventario.agregar_mueble(mueble)
        guardar_inventario(inventario)
        print(f"{tipo.capitalize()} agregado correctamente.")

    elif comando == "mostrar":
        if not inventario.muebles:
            print("El inventario está vacío.")
        else:
            inventario.mostrar_inventario()

    elif comando == "guardar":
        guardar_inventario(inventario)
        print("Inventario guardado correctamente.")

    elif comando == "cargar":
        inventario = cargar_inventario()
        print("Inventario cargado correctamente.")

    elif comando == "descuento" and len(sys.argv) == 4:
        try:
            index = int(sys.argv[2])
            porcentaje = float(sys.argv[3])
            
            if 0 <= index < len(inventario.muebles):
                inventario.muebles[index].aplicar_descuento(porcentaje)
                guardar_inventario(inventario)
                print(f"Se aplicó un descuento del {porcentaje}% al mueble {index}.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Error: índice y porcentaje deben ser números.")

    else:
        print("Comando no reconocido.")

if __name__ == "__main__":
    main()
