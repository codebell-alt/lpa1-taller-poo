# Sistema de Gestión de Mueblería

Este proyecto es un taller práctico para aplicar los conceptos de Programación Orientada a Objetos (POO) en Python.

## Autor
**Isabella Ramirez Franco**  
GitHub: [codebell-alt](https://github.com/codebell-alt)

## Instrucciones
1. Haz un fork de este repositorio a tu cuenta de GitHub.
2. Clona el repositorio a tu computadora local.
3. Sigue las instrucciones de cada punto del taller.
4. Realiza un commit por cada punto completado.
5. Sube tus cambios a tu repositorio remoto.

## Puntos del Taller
1. Editar el `README.md` para incluir el nombre y usuario de GitHub.
2. Definir una clase abstracta `Mueble` con atributos comunes (material, precio) y métodos abstractos (`calcular_precio_final()`). Utilizar el módulo `abc` de Python para definir clases abstractas y métodos abstractos.
3. Crear subclases como `Silla`, `Mesa` y `Armario` que hereden de la clase `Mueble`. Implementar los métodos abstractos y agregar atributos específicos de cada tipo de mueble.
4. En el programa principal (`main.py`) instanciar objetos de las subclases y probar sus métodos. Mostrar información de los muebles (atributos y precios) utilizando `Rich`.
5. Utilizar `pytest` para escribir pruebas unitarias que verifiquen el comportamiento de las clases. Probar con al menos 3 diferentes escenarios y casos de borde.
6. Agregar la capacidad de aplicar descuentos a los muebles.
7. Agregar una clase para gestionar el inventario de la mueblería.
8. Agregar una función para serializar y deserializar los objetos de los muebles en formato JSON.
9. Agregar una interfaz de línea de comandos para interactuar con la mueblería.

## Buenas Prácticas y Workflow Moderno
- **Código Limpio:** Utilizar nombres descriptivos, comentarios claros y una estructura de código coherente.
- **Pruebas Unitarias:** Garantizar la calidad del código mediante `pytest`.
- **Uso de Git:** Gestionar los cambios con `Git` y realizar commits atómicos.
- **Documentación:** Mantener el `README.md` actualizado y documentar el código cuando sea necesario.