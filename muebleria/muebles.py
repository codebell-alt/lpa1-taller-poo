import json
from abc import ABC, abstractmethod

# Definimos la clase abstracta Mueble
class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        """Método abstracto para calcular el precio final del mueble."""
        pass

    # FUNCIÓN PARA APLICAR DESCUENTO  
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio del mueble."""
        if 0 <= porcentaje <= 100:
            descuento = (self.precio * porcentaje) / 100
            self.precio -= descuento
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")

    def __str__(self):
        return f"{self.__class__.__name__}: Material={self.material}, Precio=${self.precio:.2f}"

    def to_dict(self):
        """Convierte el objeto Mueble en un diccionario serializable."""
        return {
            "tipo": self.__class__.__name__,
            "material": self.material,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Mueble a partir de un diccionario."""
        tipo = data["tipo"]
        if tipo == "Silla":
            return Silla(data["material"], data["precio"], respaldo=True)
        elif tipo == "Mesa":
            return Mesa(data["material"], data["precio"], tamaño="Mediana")
        elif tipo == "Armario":
            return Armario(data["material"], data["precio"], puertas=2)
        else:
            raise ValueError(f"Tipo de mueble desconocido: {tipo}")

# Clases específicas de muebles
class Silla(Mueble):
    def __init__(self, material, precio, respaldo):
        super().__init__(material, precio)
        self.respaldo = respaldo

    def calcular_precio_final(self):
        return self.precio * 1.10  # 10% extra por respaldo

class Mesa(Mueble):
    def __init__(self, material, precio, tamaño):
        super().__init__(material, precio)
        self.tamaño = tamaño

    def calcular_precio_final(self):
        return self.precio * 1.20  # 20% extra por tamaño

class Armario(Mueble):
    def __init__(self, material, precio, puertas):
        super().__init__(material, precio)
        self.puertas = puertas

    def calcular_precio_final(self):
        return self.precio * 1.15  # 15% extra por puertas

# CLASE INVENTARIO
class Inventario:
    """
    Clase para gestionar el inventario de la mueblería.
    Permite agregar, eliminar y mostrar muebles en el inventario.
    """
    def __init__(self):
        self.muebles = []  # Lista para almacenar los muebles

    def agregar_mueble(self, mueble):
        """Agrega un mueble al inventario."""
        self.muebles.append(mueble)

    def eliminar_mueble(self, mueble):
        """Elimina un mueble del inventario si existe."""
        if mueble in self.muebles:
            self.muebles.remove(mueble)
        else:
            print("El mueble no está en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los muebles en el inventario."""
        if self.muebles:
            print("\nInventario de la Mueblería:")
            for mueble in self.muebles:
                print(mueble)
        else:
            print("El inventario está vacío.")

    # FUNCIÓN PARA SERIALIZAR INVENTARIO A JSON
    def guardar_json(self, archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON."""
        with open(archivo, "w") as f:
            json.dump([mueble.to_dict() for mueble in self.muebles], f, indent=4)
        print(f"Inventario guardado en {archivo}")

    # FUNCIÓN PARA DESERIALIZAR INVENTARIO DESDE JSON
    def cargar_json(self, archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.muebles = [Mueble.from_dict(m) for m in data]
            print(f"Inventario cargado desde {archivo}")
        except FileNotFoundError:
            print("El archivo JSON no existe. No se cargó nada.")
