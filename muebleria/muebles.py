# clases relacionadas con los muebles
### PASO 2: Definir la Clase Abstracta `Mueble`
from abc import ABC, abstractmethod

class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass

### PASO 3: Crear las Subclases `Silla`, `Mesa` y `Armario`
# Se importa la clase base Mueble desde el módulo muebles
from muebleria.muebles import Mueble  

# Definimos la clase `Silla`, que hereda de `Mueble`
class Silla(Mueble):
    def __init__(self, material, precio, respaldo):
        #Constructor de la clase Silla
        super().__init__(material, precio)
        self.respaldo = respaldo

    def calcular_precio_final(self):
       #Calcula el precio final de la silla.
       #Se aplica un incremento del 10% si la silla tiene respaldo.
        
        return self.precio * 1.10  # 10% extra por respaldo

# Definimos la clase `Mesa`, que hereda de `Mueble`
class Mesa(Mueble):
    def __init__(self, material, precio, tamaño):
        
        #Constructor de la clase Mesa.
        super().__init__(material, precio)
        self.tamaño = tamaño

    def calcular_precio_final(self):
        #Calcula el precio final de la mesa. Se aplica un incremento del 20% por el tamaño de la mesa.
        return self.precio * 1.20  # 20% extra por tamaño


# Definimos la clase `Armario`, que hereda de `Mueble`
class Armario(Mueble):
    def __init__(self, material, precio, puertas):
        #Constructor de la clase Armario.
        super().__init__(material, precio)
        self.puertas = puertas

    def calcular_precio_final(self):
        #Calcula el precio final del armario.Se aplica un incremento del 15% basado en el número de puertas.
        return self.precio * 1.15  # 15% extra por puertas
