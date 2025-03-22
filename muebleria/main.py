# ejecutar el programa y probar las clases
from muebles import Silla, Mesa, Armario  
from rich.console import Console  

console = Console()

silla = Silla("Madera", 50, True)
mesa = Mesa("Metal", 100, "Grande")
armario = Armario("Plástico", 200, 2)

console.print(f"[bold blue]Silla:[/bold blue] Material: {silla.material}, Precio Final: ${silla.calcular_precio_final():.2f}")
console.print(f"[bold green]Mesa:[/bold green] Material: {mesa.material}, Precio Final: ${mesa.calcular_precio_final():.2f}")
console.print(f"[bold red]Armario:[/bold red] Material: {armario.material}, Precio Final: ${armario.calcular_precio_final():.2f}")
