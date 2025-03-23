# Ejecutar el programa y probar las clases
from muebles import Silla, Mesa, Armario, Inventario  # Importamos la clase Inventario
from rich.console import Console
from rich.table import Table  # Para mostrar el inventario en forma de tabla

console = Console()

# Crear inventario
inventario = Inventario()

# Crear muebles
silla = Silla("Madera", 50, True)
mesa = Mesa("Metal", 100, "Grande")
armario = Armario("Plastico", 200, 2)

# Agregar muebles al inventario
inventario.agregar_mueble(silla)
inventario.agregar_mueble(mesa)
inventario.agregar_mueble(armario)

# Mostrar información de los muebles individualmente
console.print(f"[bold blue]Silla:[/bold blue] Material: {silla.material}, Precio Final: ${silla.calcular_precio_final():.2f}")
console.print(f"[bold green]Mesa:[/bold green] Material: {mesa.material}, Precio Final: ${mesa.calcular_precio_final():.2f}")
console.print(f"[bold red]Armario:[/bold red] Material: {armario.material}, Precio Final: ${armario.calcular_precio_final():.2f}")

# Mostrar el inventario en forma de tabla con Rich
table = Table(title="Inventario de la Muebleria")

table.add_column("Tipo de Mueble", style="cyan", justify="center")
table.add_column("Material", style="magenta", justify="center")
table.add_column("Precio Final", style="yellow", justify="center")

for mueble in inventario.muebles:
    table.add_row(mueble.__class__.__name__, mueble.material, f"${mueble.calcular_precio_final():.2f}")

console.print("\n[bold underline]Inventario:[/bold underline]")
console.print(table)

# Aplicar descuentos
silla.aplicar_descuento(10)
mesa.aplicar_descuento(15)
armario.aplicar_descuento(20)

# Mostrar inventario despues de los descuentos
console.print("\n[bold underline]Inventario despues de aplicar descuentos:[/bold underline]")

table_descuento = Table(title="Inventario con Descuentos Aplicados")
table_descuento.add_column("Tipo de Mueble", style="cyan", justify="center")
table_descuento.add_column("Material", style="magenta", justify="center")
table_descuento.add_column("Precio con Descuento", style="yellow", justify="center")

for mueble in inventario.muebles:
    table_descuento.add_row(mueble.__class__.__name__, mueble.material, f"${mueble.precio:.2f}")

console.print(table_descuento)
