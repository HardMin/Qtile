from libqtile.config import Key
from libqtile.lazy import lazy
import os  # Necesitas importar os para os.path.expanduser

web = "google-chrome-stable"
terminal = "kitty"

mod = "mod4"
alt = "mod1"

# Es mejor expandir la ruta una sola vez al principio
screenshot_dir = os.path.expanduser("~/Image/Screenshots")


keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        (
            [mod],
            "F2",
            lazy.spawn("toggle-keyboard"),
        ),
        # ------------ Window Configs ------------
        # Layout MonadTall
        ([mod], "i", lazy.layout.grow()),
        ([mod], "b", lazy.layout.shrink()),
        ([mod], "v", lazy.layout.reset()),
        ([mod, "shift"], "n", lazy.layout.normalize()),
        ([mod], "o", lazy.layout.maximize()),
        ([mod, "shift"], "f", lazy.layout.toggle_auto_maximize()),
        ([mod, "shift"], "space", lazy.layout.flip()),
        # Layout Others
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "space", lazy.layout.next()),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        ([mod, "shift"], "h", lazy.layout.shuffle_left()),
        ([mod, "shift"], "l", lazy.layout.shuffle_right()),
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        ([mod, "control"], "h", lazy.layout.grow_left()),
        ([mod, "control"], "l", lazy.layout.grow_right()),
        ([mod, "control"], "j", lazy.layout.grow_down()),
        ([mod, "control"], "k", lazy.layout.grow_up()),
        ([mod], "n", lazy.layout.normalize()),
        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Toggle keyboard lang
        # Move windows up or down in current stack
        # ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        # ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        # Kill window
        ([mod], "w", lazy.window.kill()),
        # Switch focus of monitors
        ([mod], "period", lazy.next_screen()),
        ([mod], "comma", lazy.prev_screen()),
        # Restart Qtile
        ([mod, "control"], "r", lazy.restart()),
        ([mod, "control"], "q", lazy.shutdown()),
        ([mod], "r", lazy.spawncmd()),
        # ------------ App Configs ------------
        # Menu
        ([mod], "m", lazy.spawn("rofi -show drun")),
        # Browser
        ([mod, "shift"], "w", lazy.spawn(web)),
        # File Explorer
        ([mod], "e", lazy.spawn("nemo")),
        # Terminal
        ([mod], "Return", lazy.spawn(terminal)),
        # Redshif
        ([mod], "r", lazy.spawn("redshift -O 2800")),
        ([mod, "shift"], "r", lazy.spawn("redshift -x")),
        # Screenshot
        ([mod], "c", lazy.spawn("code")),
        # ------------ Hardware Configs ------------
        # Volume
        ([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
        ([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
        ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        # Brightness
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
        # ------------ Screenshot Configs ------------
        # Guarda en ~/Images/Screenshots y copia al portapapeles
        (
            [mod],
            "s",
            # Usamos una f-string externa con comillas triples para la cadena del shell.
            # Esto permite usar comillas dobles dentro de la cadena del shell sin problemas.
            lazy.spawn(
                f'bash -c "maim {screenshot_dir}/$(date +%Y-%m-%d-%H%M%S).png && cat {screenshot_dir}/$(date +%Y-%m-%d-%H%M%S).png | xclip -selection clipboard -t image/png"'
            ),
            "Full screenshot, save and copy",
        ),
        # Solo copia al portapapeles
        (
            [mod, "shift"],
            "s",  # Shift + s
            lazy.spawn("maim | xclip -selection clipboard -t image/png"),
            "Full screenshot, copy to clipboard",
        ),
        # --- Captura de Región Seleccionada (Interactiva con slop) ---
        # Guarda en ~/Images/Screenshots y copia al portapapeles
        (
            [mod, "control"],
            "s",  # Control + s
            # Corregido para guardar Y copiar
            lazy.spawn(
                f'bash -c "maim -s {screenshot_dir}/$(date +%Y-%m-%d-%H%M%S).png && cat {screenshot_dir}/$(date +%Y-%m-%d-%H%M%S).png | xclip -selection clipboard -t image/png"'
            ),
            "Region screenshot, save and copy",
        ),
        # Solo copia al portapapeles
        (
            [mod, alt],  # Usando la variable 'alt' que definiste como 'mod1'
            "s",  # Alt + s
            lazy.spawn("maim -s | xclip -selection clipboard -t image/png"),
            "Region screenshot, copy to clipboard only",
        ),
        # --- Captura de Ventana Activa ---
        # Guarda en ~/Images/Screenshots y copia al portapapeles
        (
            [mod, "shift", "control"],
            "s",  # Shift + Control + s
            # Corregido para guardar Y copiar
            lazy.spawn(
                f'bash -c "maim -i $(xdotool getactivewindow) {screenshot_dir}/$(date +%Y-%m-%d-%H%M%S).png && cat {screenshot_dir}/$(date +%Y-%m-%d-%H%M%S).png | xclip -selection clipboard -t image/png"'
            ),
            "Active window screenshot, save and copy",
        ),
        # Solo copia al portapapeles
        (
            [mod, alt, "shift"],  # Usando 'alt' y 'shift'
            "s",  # Alt + Shift + s
            lazy.spawn(
                "maim -i $(xdotool getactivewindow) | xclip -selection clipboard -t image/png"
            ),
            "Active window screenshot, copy to clipboard only",
        ),
    ]
]
