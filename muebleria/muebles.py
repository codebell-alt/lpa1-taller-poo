# Clases relacionadas con los muebles
from abc import ABC, abstractmethod

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

# Definimos la clase `Silla`, que hereda de `Mueble`
class Silla(Mueble):
    def __init__(self, material, precio, respaldo):
        super().__init__(material, precio)
        self.respaldo = respaldo

    def calcular_precio_final(self):
        return self.precio * 1.10  # 10% extra por respaldo

# Definimos la clase `Mesa`, que hereda de `Mueble`
class Mesa(Mueble):
    def __init__(self, material, precio, tamaño):
        super().__init__(material, precio)
        self.tamaño = tamaño

    def calcular_precio_final(self):
        return self.precio * 1.20  # 20% extra por tamaño

# Definimos la clase `Armario`, que hereda de `Mueble`
class Armario(Mueble):
    def __init__(self, material, precio, puertas):
        super().__init__(material, precio)
        self.puertas = puertas

    def calcular_precio_final(self):
        return self.precio * 1.15  # 15% extra por puertas
    
    # NUEVA CLASE INVENTARIO
class Inventario:
    """
    Clase para gestionar el inventario de la mueblería.
    Permite agregar, eliminar y mostrar muebles en el inventario.
    """
    def __init__(self):
        self.muebles = []  # Lista para almacenar los muebles

    def agregar_mueble(self, mueble):
        """
        Agrega un mueble al inventario
        """
        self.muebles.append(mueble)

    def eliminar_mueble(self, mueble):
        #Elimina un mueble del inventario si existe.
    
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
