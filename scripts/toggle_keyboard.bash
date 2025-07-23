#!/bin/bash

get_current_layout() {
    # Obtener la disposición actual del teclado
    local layout=$(setxkbmap -query | grep layout | cut -d: -f2 | tr -d ' ')
    echo "$layout"
}

toggle_keyboard_layout() {
    # Enviar notificación inicial
    local current_layout=$(get_current_layout)

    # Cambiar disposición
    if [ "$current_layout" == "us" ]; then
        # Cambiar a latam
        setxkbmap latam
    else
        # Cambiar a us
        setxkbmap us
    fi

    # Verificar y notificar el nuevo layout
    local new_layout=$(get_current_layout)
}

# Ejecutar la función
toggle_keyboard_layout