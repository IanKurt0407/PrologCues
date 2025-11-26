import os
import sys
import time
from pyswip import Prolog

# --- LIBRERÍAS DE DISEÑO ---
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from rich.prompt import Prompt
from rich.layout import Layout
from rich.align import Align
import pyfiglet

# Inicializamos la consola de diseño
console = Console()

# --- CONFIGURACIÓN PROLOG  ---
ruta_prolog = r"C:\Program Files\swipl\bin"
if os.path.exists(ruta_prolog):
    os.environ['PATH'] += ";" + ruta_prolog

# Configuración de preguntas
CUESTIONARIO = [
    ("¿Te molesta mucho el ruido fuerte o las luces brillantes?", "sensibilidad_sensorial"),
    ("¿Sientes un agotamiento extremo después de socializar?", "agotamiento_social"),
    ("¿Te cuesta mantener contacto visual directo?", "contacto_visual"),
    ("¿Tienes intereses muy específicos (temas profundos)?", "interes_profundo"),
    ("¿Te resulta difícil entender sarcasmos o doble sentido?", "literalidad"),
    ("¿Haces movimientos repetitivos para calmarte (stimming)?", "estimulacion"),
    ("¿Te genera ansiedad si cambian tus rutinas?", "rigidez_rutina"),
    ("¿Sueles interrumpir o hablar mucho de un solo tema?", "impulsividad_verbal"),
    ("¿Te cuesta iniciar tareas aburridas (función ejecutiva)?", "dificultad_inicio"),
    ("¿Te hiperfocalizas olvidando comer o dormir?", "hiperfoco")
]

def mostrar_banner():
    console.clear()
    # Título gigante estilo ASCII
    titulo = pyfiglet.figlet_format("NEURO TEST", font="slant")
    console.print(f"[bold cyan]{titulo}[/bold cyan]", justify="center")
    console.print("[dim]Sistema Experto de Análisis de Patrones Cognitivos[/dim]", justify="center")
    console.print("\n")

def limpiar_pantalla_total():
    # Detecta si es Windows ('nt') o Linux/Mac
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
    # TRUCO: Código ANSI para borrar el buffer (historial) de la terminal
    # \033[2J = Borra pantalla
    # \033[3J = Borra historial (Esto es lo que evita el scroll)
    # \033[H = Mueve el cursor al inicio
    print("\033[2J\033[3J\033[H", end="")

def mostrar_disclaimer():
    texto = Text()
    texto.append("AVISO IMPORTANTE\n\n", style="bold red underline")
    texto.append("Este software es un prototipo académico.\n", style="yellow")
    texto.append("NO sustituye un diagnóstico médico profesional.\nLos resultados son meramente orientativos.", style="white")
    
    panel = Panel(texto, border_style="red", title="⚠️ DISCLAIMER", width=60, padding=(1, 2))
    console.print(Align.center(panel))
    console.input("\n[bold white]Presiona [green]ENTER[/green] para aceptar y continuar...[/bold white]")

def main():
    prolog = Prolog()
    
    # Carga silenciosa
    try:
        prolog.consult("reglas_nd.pl")
    except Exception as e:
        console.print(f"[bold red]Error fatal:[/bold red] No se pudo cargar Prolog.\n{e}")
        return


    limpiar_pantalla_total()
    mostrar_banner()
    mostrar_disclaimer()
    # 2. LIMPIEZA DE PANTALLA
    limpiar_pantalla_total()

    mostrar_banner() # Limpiamos y mostramos título de nuevo

    console.print(Panel("[bold yellow]INSTRUCCIONES:[/bold yellow] Responde [green]S[/green] (Sí) o [red]N[/red] (No) a las siguientes preguntas.", border_style="blue"))
    print("\n")

    # Limpiamos memoria de Prolog
    prolog.retractall("indicador(_)")

    hechos_agregados = []

    # Bucle de preguntas con diseño
    for i, (pregunta, clave) in enumerate(CUESTIONARIO, 1):
        # Usamos Prompt de Rich para inputs bonitos
        console.print(f"[bold cyan]Pregunta {i}/10:[/bold cyan] {pregunta}")
        
        while True:
            respuesta = Prompt.ask("   >> Tu respuesta", choices=["s", "n", "S", "N"], show_choices=False)
            if respuesta.lower() in ['s', 'n']:
                break
        
        if respuesta.lower() == 's':
            prolog.assertz(f"indicador({clave})")
            hechos_agregados.append(clave)
        
        console.print("-" * 40, style="dim") # Separador

    # Efecto dramático de "Procesando"
    console.print("\n")
    for _ in track(range(100), description="[green]Analizando patrones neuronales...[/green]"):
        time.sleep(0.02) # Pequeña pausa falsa para dar emoción

    # Consultar resultado
    soluciones = list(prolog.query("resultado(X)"))
    
    #Limpiamos pantalla y mostramos los resultados.
    limpiar_pantalla_total()
    mostrar_banner()

    if soluciones:
        resultado = soluciones[0]["X"]
        
        if resultado == "posible_neurodivergente":
            estilo = "bold green"
            titulo_res = "POSIBLE PERFIL NEURODIVERGENTE"
            msg = f"Se detectaron  {len(hechos_agregados)} indicadores de procesamiento atípico."
            icono = "🧠✨"
        else:
            estilo = "bold blue"
            titulo_res = "POSIBLE PERFIL NEUROTÍPICO"
            msg = f"Se detectaron {len(hechos_agregados)} indicadores. Sugiere un procesamiento estándar."
            icono = "👤"

        # Panel de Resultado Final
        texto_resultado = Text()
        texto_resultado.append(f"\n{icono} {titulo_res}\n\n", style=estilo + " underline")
        texto_resultado.append(msg + "\n", style="white")
        texto_resultado.append("\nGracias por participar.", style="dim italic")

        panel_resultado = Panel(texto_resultado, border_style="green" if resultado == "posible_neurodivergente" else "blue", padding=(2, 4))
        console.print(Align.center(panel_resultado))
        
    else:
        console.print("[bold red]Error:[/bold red] No se pudo determinar un resultado lógico.")

    console.input("\n[dim]Presiona Enter para salir...[/dim]")

if __name__ == "__main__":
    main()