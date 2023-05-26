#!/bin/bash
# Script superscan.sh
# Nombre: Victor Manuel Cardenas Cavazos
# Matrícula: 1919410
#
# Ejemplo de Menu en BASH
#
date
    echo "|"
    echo "|---------------------------|"
    echo "|   	  Menu Principal      |"
    echo "|---------------------------|"
    echo "|1. Net Discover"
    echo "|2. Portscanv1"
    echo "|3. Welcome"
    echo "|4. Actual User"
    echo "|5. Hostname"
    echo "|6. Exit"
    echo "|"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $HOME/netdiscover.sh;;
        2) $HOME/portscanv1.sh;;
        3) $HOME/welcome.sh;;
        4) whoami;;
        5) echo "Tu host es:"
                hostname
                echo "saludos";;
        6) echo "Bye!"; exit 0;;
esac
