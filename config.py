
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


import os

mod = "mod4"
terminal = guess_terminal()

 # var for wallpapers 


wallpapers = [
        "wallpaper-archlinuxDark.jpg",
        "wallpaperflare.com_wallpaper.jpg",
        "wallpaperCarretera.jpg",
        "wallpaperMontana.jpg",
        "wallpaperMontana2.jpg",
        ]
wallpaper = "feh --bg-fill /home/diego/.config/qtile/wallpapers/"+wallpapers[3]




#Variables de control del volumen
controlVolumen = '5%'


#listado iconos nerd font

iconSize = 17

iconArchlinux = "  "   #1- nf-linux-archlinux
iconFolder = "  "      #2- nf-custom-folder
iconFirefox = "  "     #3- nf-dev-firefox
iconTerminal = "  "    #4- nf-dev-terminal
iconMusic = "  "       #4- nf-mdi-music_circle
iconMenu = "  "        #5- nf-mdi-menu
iconVolume = " "       #6- nf-fa-volume_up
iconLayout = "離"       #7- nf-mdi-table 
iconCode = "  "        #8- nf-mdi-code_greater_than 
iconNetWork = "  "     #9- nf-mdi-access_point_network
iconOff = ""           #10- nf-fa-power_off

#listado de colores del background
colorGroup = "#00355a"
colorGroupActive = "#ffffff"

#Colores de grupos
colorGrupo1 = "#0065a1"
colorGrupo2 = "#003e8f"
colorGrupo3 = "#1C9100"
colorButtonApagar = "#CF2400"


def fc_rectangulo(vColor, tipo):
    if tipo == 0:
        icon = ""      #nf-ple-left_half_circle_thick
    elif tipo == 1:
        icon = ""      #nf-ple-right_half_circle_thick
    return widget.TextBox(
            text=icon,
            fontsize=23.5,
            foreground=vColor,
            padding=0,
            margin=0,
            )
        
        
countSreenShots = 0
def ScreenShots_root():
    if countSreenShots > 0:
        lazy.spawn('import -windows root /home/diego/Pictures/screenshot'+countSreenShots+'.jpg')
        countSreenShots += 1
        return
    if countSreenShots == 0:
        lazy.spawn('import -window root /home/diego/Pictures/screenshot.jpg')
        countSreenShots += 1

        
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),


    # WorkSpace Coding
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "c", lazy.spawn('code'), desc="Launch terminal"),



    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, 'shift'], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([mod, "mod1"], "h", lazy.layout.flip_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "l", lazy.layout.flip_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "j", lazy.layout.flip_down(), desc="Grow window down"),
    Key([mod, "mod1"], "k", lazy.layout.flip_up(), desc="Grow window up"),


    Key([mod], 'r', lazy.run_extension(extension.DmenuRun( 

    ))),

    # abrir el Menu
    Key([mod], 'm', lazy.spawn("rofi -show drun"), desc="Abrir menu"),

    # abrir el gestor de carpetas
    Key([mod, 'control'], 'z', lazy.spawn("thunar"), desc="abrir el gestor de carpetas"),

    # abrir el navegador
    Key([mod, 'control'], 'w', lazy.spawn("chromium"), desc="Abrir firefox"),


    # Control del volumen
    Key([mod, 'control'], 'Up', lazy.spawn('pactl set-sink-volume 0 +'+controlVolumen), desc="Subir el volumen"),
    Key([mod, 'control'], 'Down', lazy.spawn('pactl set-sink-volume 0 -'+controlVolumen), desc="Subir el volumen"),

    # Capture
    Key([mod], 's', lazy.spawn('scrot /home/diego/Pictures/%Y-%m-%d_$wx$h.png'), 
        desc="ScreenShots"),
    Key([mod, 'shift'], 's', lazy.spawn('scrot -s /home/diego/Pictures/%Y-%m-%d_$wx$h.png'), 
        desc="ScreenShots"),
]




__groups = {
        1:Group(iconTerminal, matches=[Match(wm_class=[""])]),
        2:Group(iconNetWork,  matches=[Match(wm_class=["firefox","chromium"])]),
        3:Group(iconCode,     matches=[Match(wm_class=["code - oss","code-oss"])]),
        4:Group(iconFolder,   matches=[Match(wm_class=["thunar"])], layout="treetab"),
        5:Group(iconMusic,    matches=[Match(wm_class=["spotify","vlc"])]),
        }
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], numeroEscritorio.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(numeroEscritorio.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Columns(border_focus_stack=["#0000"], border_width=0, 
                    margin=3, border_focus="#04be"),
    # layout.Floating(border_focus="04be", border_normal="#04be"),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="sans",
    font="MesloLGS NF Bold",
    fontsize=14,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(iconArchlinux, foreground="#2fa9c1", fontsize="20"),
                widget.GroupBox(highlight_method='block',background='#000000',
                                padding=0,
                                active=colorGroupActive, fontsize=iconSize),

                widget.WindowName( padding=5,),

                fc_rectangulo(colorGrupo1, 0),
                widget.Memory(format='MEM:{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} ',
                              fontsize=10,background=colorGrupo1, ),
                widget.Memory(format='- Swap:{SwapUsed: .0f}{ms}/{SwapTotal: .0f}{ms}',
                              fontsize=10,background=colorGrupo1, ),
                widget.CPU(format='| CPU:{load_percent}%',
                            background=colorGrupo1, fontsize=10),
                fc_rectangulo(colorGrupo1, 1),

                fc_rectangulo(colorGrupo2, 0),
                widget.Clock(format=" %Y/%m/%d %I:%M %p",background=colorGrupo2, fontsize=10),
                widget.TextBox(iconVolume,               background=colorGrupo2, ),
                widget.Volume(fmt=':{} ', fontsize= 10,  background=colorGrupo2, ),
                fc_rectangulo(colorGrupo2, 1),

                fc_rectangulo(colorGrupo3, 0),
                widget.TextBox(iconLayout,background=colorGrupo3),
                widget.CurrentLayout(background=colorGrupo3),
                fc_rectangulo(colorGrupo3, 1),


                fc_rectangulo(colorButtonApagar, 0),
                widget.QuickExit(default_text=iconOff, background=colorButtonApagar, 
                                 countdown_format='{}'),
                fc_rectangulo(colorButtonApagar, 1),
            ],
            28,
            margin=[0, 0, 2, 0],  # Draw top and bottom borders
            background="#000000"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# Mi configuracion 30-03-22 

cmd = [
        wallpaper,
        "picom --no-vsync &",
        "amixer sset Master unmute",
        "xrandr -s 1440x900",
]

for x in cmd:
    os.system(x)
