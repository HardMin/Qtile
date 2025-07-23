from libqtile.config import Key
from libqtile.lazy import lazy

web = "google-chrome-stable"
terminal = "kitty"

mod = "mod4"

screenshot_dir = "~/Images/Screenshots/"


keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        (
            [mod, "shift", "F3"],
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
        (
            [mod],
            "s",
            lazy.spawn(
                "scrot 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mkdir -p ~/images/screenshots/ | mv $f ~/images/screenshots/'"
            ),
        ),
        ([mod, "shift"], "s", lazy.spawn("scrot -s")),
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
        ([mod], "F2", lazy.spawn(f"flameshot full -p {screenshot_dir} -r")),
        # Captura de pantalla completa y copiar al portapapeles
        ([mod, "shift"], "F2", lazy.spawn("flameshot full -c")),
        # Captura de región y guardar en archivo (interactivo)
        ([], "F2", lazy.spawn(f"flameshot gui -p {screenshot_dir}")),
        # Captura de región y copiar al portapapeles (interactivo)
        # (
        #     [mod, "shift", "control"],
        #     "F2",  # Puedes elegir otro atajo si "s" está en uso
        #     lazy.spawn("flameshot gui -c"),
        # ),
        # Captura de ventana y guardar en archivo (interactivo, selecciona ventana)
        (
            [mod, "control"],
            "F2",
            lazy.spawn(f"flameshot gui -p {screenshot_dir} --active"),
        ),  # --active intenta capturar la ventana activa directamente
        # Captura de ventana y copiar al portapapeles (interactivo, selecciona ventana)
        (
            [mod, "shift", "control"],
            "F2",
            lazy.spawn("flameshot gui -c --active"),
        ),  # --active intenta copiar la ventana activa directamente
        # Si quieres una forma más directa de seleccionar una ventana con el mouse (como `flameshot gui`)
        # Pero solo para la ventana
        # (
        #     [mod],
        #     "w",  # Otro atajo si "w" está en uso
        #     lazy.spawn(f"flameshot gui -p {screenshot_dir}"),
        # ),  # flameshot gui te permite seleccionar una ventana o región
    ]
]
