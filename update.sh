#!/bin/bash

red() {
    echo -e "\033[32;1m${*}\033[0m"
}

clear

fun_bar() {
    CMD[0]="$1"
    CMD[1]="$2"

    (
        [[ -e $HOME/fim ]] && rm -f "$HOME/fim"
        ${CMD[0]} >/dev/null 2>&1
        ${CMD[1]} >/dev/null 2>&1
        touch "$HOME/fim"
    ) >/dev/null 2>&1 &

    tput civis
    echo -ne " \033[0;33mPlease Wait Loading \033[1;37m- \033[0;33m["

    while true; do
        for ((i = 0; i < 18; i++)); do
            echo -ne "\033[0;32m#"
            sleep 0.1s
        done

        if [[ -e $HOME/fim ]]; then
            rm -f "$HOME/fim"
            break
        fi

        echo -e "\033[0;33m]"
        sleep 1s
        tput cuu1
        tput dl1
        echo -ne " \033[0;33mPlease Wait Loading \033[1;37m- \033[0;33m["
    done

    echo -e "\033[0;33m]\033[1;37m -\033[1;32m OK !\033[1;37m"
    tput cnorm
}

res1() {
    clear
    echo -e "Updating menu from GitHub folder..."

    rm -rf /tmp/new8-master /tmp/new8.zip

    apt update -y >/dev/null 2>&1
    apt install -y unzip curl dos2unix >/dev/null 2>&1

    curl -L -o /tmp/new8.zip https://github.com/xyzstore/new8/archive/refs/heads/master.zip

    if [ ! -s /tmp/new8.zip ]; then
        echo "Gagal download GitHub archive."
        exit 1
    fi

    unzip -o /tmp/new8.zip -d /tmp >/dev/null 2>&1

    if [ ! -d /tmp/new8-master/limit/menu ]; then
        echo "Folder menu tidak ditemukan di GitHub archive."
        exit 1
    fi

    chmod +x /tmp/new8-master/limit/menu/*
    cp -f /tmp/new8-master/limit/menu/* /usr/local/sbin/
    dos2unix /usr/local/sbin/* 2>/dev/null

    cat >/root/.profile <<'EOF'
# ~/.profile: executed by Bourne-compatible login shells.

export PATH=$PATH:/usr/local/sbin:/usr/sbin:/sbin

if [ "$BASH" ]; then
    if [ -x /usr/local/sbin/welcome ]; then
        /usr/local/sbin/welcome
    elif [ -x /usr/local/sbin/menu ]; then
        /usr/local/sbin/menu
    fi
fi
EOF

    chmod 644 /root/.profile

    rm -rf /tmp/new8-master /tmp/new8.zip update.sh

    echo -e "Update menu selesai."
}

clear
echo -e "\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e "\033[1;96m UPDATE SCRIPT \E[0m"
echo -e "\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e ""
echo -e " \033[1;91m update script service\033[1;37m"

fun_bar 'res1'

echo -e "\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e ""
read -n 1 -s -r -p "Press [ Enter ] to back on menu"

if command -v menu >/dev/null 2>&1; then
    menu
else
    /usr/local/sbin/menu
fi
