#!/bin/bash

red() {
    echo -e "\033[32;1m${*}\033[0m"
}

clear

res1() {
    clear
    echo -e "Updating menu from GitHub folder..."

    rm -rf /tmp/new8-master /tmp/new8.zip

    command -v curl >/dev/null 2>&1 || apt install -y curl >/dev/null 2>&1
    command -v unzip >/dev/null 2>&1 || apt install -y unzip >/dev/null 2>&1
    command -v dos2unix >/dev/null 2>&1 || apt install -y dos2unix >/dev/null 2>&1

    curl -L --connect-timeout 15 --max-time 120 \
        -o /tmp/new8.zip \
        https://github.com/xyzstore/new8/archive/refs/heads/master.zip

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
    chmod +x /usr/local/sbin/* 2>/dev/null

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

echo -e "\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e "\033[1;96m UPDATE SCRIPT \E[0m"
echo -e "\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e ""
echo -e " \033[1;91m update script service\033[1;37m"
echo -e ""

res1

echo -e "\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e ""
read -n 1 -s -r -p "Press [ Enter ] to back on menu"

if command -v menu >/dev/null 2>&1; then
    menu
elif [ -x /usr/local/sbin/menu ]; then
    /usr/local/sbin/menu
fi
