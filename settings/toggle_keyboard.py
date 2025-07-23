import subprocess, os

from notify import notify


def get_current_layout():
    try:
        # Obtener la disposición actual del teclado
        result = subprocess.check_output(["setxkbmap", "-query"], text=True)
        # Buscar la línea que contiene "layout"
        for line in result.splitlines():
            if "layout" in line:
                # Extraer el valor del layout
                layout = line.split(":")[1].strip()
                return layout
    except Exception as e:
        print(f"Error al obtener la disposición actual: {e}")
        return None


def toggle_keyboard_layout():
    os.system(f"notify-send 'hola'")

    current_layout = get_current_layout()

    if current_layout == "us":
        # Cambiar a latam
        subprocess.run(["setxkbmap", "latam"])
        print("Cambiado a disposición Latinoamericana")
    else:
        # Cambiar a us
        subprocess.run(["setxkbmap", "us"])
        print("Cambiado a disposición Inglés US")

    # Verificar el cambio
    new_layout = get_current_layout()
    os.system(f"notify-send {new_layout}")


# Ejecutar la función
if __name__ == "__main__":
    toggle_keyboard_layout()
