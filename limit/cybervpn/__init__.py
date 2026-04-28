from telethon import *
import datetime as DT
import sqlite3
import math
import logging
import re
import sys
import subprocess
import asyncio
import aiohttp
from telethon.tl.functions.users import GetUsersRequest
from telethon.sync import events, TelegramClient
from telethon.tl import types, functions
from telethon import utils
import requests
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
uptime = DT.datetime.now()

exec(open("cybervpn/var.txt", "r").read())
bot = TelegramClient("cybervpn", "21368165", "1dc8aa0310e819cf8bcebfc7e2810101").start(bot_token=BOT_TOKEN)











try:
    # Mencoba membuka database
    x = sqlite3.connect("cybervpn/database.db")
    c = x.cursor()

    # Membuat tabel server jika belum ada
    c.execute('''
        CREATE TABLE IF NOT EXISTS server (
            button_name TEXT PRIMARY KEY,
            host TEXT,
            password TEXT
        )
    ''')

    # Memeriksa apakah kolom 'button_name' sudah memiliki data, jika belum, masukkan data contoh
    c.execute("SELECT COUNT(*) FROM server")
    count = c.fetchone()[0]
    if count == 0:
        c.execute("INSERT INTO server (button_name, host, password) VALUES (?, ?, ?)",
                  ('sg🇵🇸', 'cybervpn.my.id', 'GoldenFR2.e'))

    x.commit()
    print("Tabel server berhasil dibuat atau sudah ada.")

    # Membuat tabel user dan ewallet jika belum ada
    c.execute('''CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY,
                    saldo REAL,
                    level TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS ewallet (
                    email TEXT PRIMARY KEY,
                    dana TEXT,
                    gopay TEXT
                )''')

    c.execute("INSERT INTO user (user_id, saldo, level) VALUES (?, ?, ?)", (ADMIN, SALDO, "admin"))

    x.commit()
    print("Database dan tabel user, ewallet berhasil dibuat atau sudah ada.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    if 'x' in locals():
        x.close()


def get_db():
    x = sqlite3.connect("cybervpn/database.db")
    x.row_factory = sqlite3.Row
    return x


def register_user(user_id, saldo, level="user"):
    db = get_db()
    db.execute("INSERT INTO user (user_id, saldo, level) VALUES (?, ?, ?)", (user_id, saldo, level))
    db.commit()





def tambah_saldo(user_id, jumlah_tambahan):
    db = get_db()
    current_saldo_str = db.execute("SELECT saldo FROM user WHERE user_id=?", (user_id,)).fetchone()[0]
    current_saldo = float(current_saldo_str)  # Mengonversi ke float
    new_saldo = current_saldo + float(jumlah_tambahan)  # Mengonversi ke float sebelum menjumlahkan
    db.execute("UPDATE user SET saldo=? WHERE user_id=?", (new_saldo, user_id))
    db.commit()








async def tambah_data_ewallet(email, dana, gopay, event):
    conn = sqlite3.connect('cybervpn/database.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO ewallet (email, dana, gopay) VALUES (?, ?, ?)", (email, dana, gopay))
        conn.commit()
        print("Data berhasil ditambahkan ke dalam tabel ewallet.")
        conn.close()
        return True
    except sqlite3.IntegrityError:
        print("**Email sudah ada dalam database. harap masukan data baru**")
        await event.respond("Email sudah ada dalam tabel ewallet. Tidak dapat menambahkan data.")
        sys.exit()
        conn.close()
        return False




def get_server_info(button_name):
    conn = sqlite3.connect('cybervpn/database.db')
    db = conn.cursor()
    return db.execute("SELECT host, password FROM server WHERE button_name = ?", (button_name,)).fetchone()





async def edit_email_ewallet(old, new, event):
    conn = sqlite3.connect('cybervpn/database.db')
    c = conn.cursor()

    try:
        c.execute("UPDATE ewallet SET email = ? WHERE email = ?", (new, old))  # Menukar posisi old dan new
        if c.rowcount == 0:  # Mengecek apakah tidak ada baris yang terpengaruh oleh UPDATE
            await event.respond("**Email lama tidak ada atau belum di tambahkan, harap menambahkan nya dengan cara mengklik tombol TAMBAH E-WALLET**")
            sys.exit() 
        else:
            conn.commit()
            print("Email berhasil diubah.")
    except sqlite3.Error as e:
        await event.respond("**gagal merubah email **", e)
    finally:
        conn.close()




















# Koneksi ke database
conn = sqlite3.connect('cybervpn/database.db')
c = conn.cursor()

# Fungsi untuk menampilkan tombol inline berdasarkan jumlah primary key di database
async def display_buttons(event):
    buttons = []
    c.execute('SELECT button_name FROM server')
    rows = c.fetchall()
    for row in rows:
        button = row[0]
        buttons.append(button)
    reply_markup = InlineKeyboardMarkup([InlineKeyboardButton(text=button, callback_data=button) for button in buttons])
    await event.reply("Pilih server:", reply_markup=reply_markup)

# Fungsi untuk menangani pemilihan tombol inline
async def button_callback(event):
    button_name = event.raw_text
    c.execute('SELECT host, password FROM server WHERE button_name = ?', (button_name,))
    row = c.fetchone()
    if row:
        server, pw = row
        await event.reply(f'Server: {server}\nPassword: {pw}')
    else:
        await event.reply('Server tidak ditemukan.')




















async def edit_nomor_dana_ewallet(event, email, nomor_dana_baru):
    conn = sqlite3.connect('cybervpn/database.db')
    c = conn.cursor()

    try:
        c.execute("SELECT dana FROM ewallet WHERE email = ?", (email,))
        result = c.fetchone()

        if result:
            c.execute("UPDATE ewallet SET dana = ? WHERE email = ?", (nomor_dana_baru, email))
            conn.commit()
            await event.respond("**dana number successfully changed!**")
        else:
            await event.respond("**email not found error code 404**")
            sys.exit()  
    except sqlite3.Error as e:
        print("Gagal mengubah nomor dana:", e)
    finally:
        conn.close()





async def edit_nomor_gopay_ewallet(event, email, nomor_gopay_baru):
    conn = sqlite3.connect('cybervpn/database.db')
    c = conn.cursor()

    try:
        c.execute("SELECT gopay FROM ewallet WHERE email = ?", (email,))
        result = c.fetchone()

        if result:
            c.execute("UPDATE ewallet SET gopay = ? WHERE email = ?", (nomor_dana_baru, email))
            conn.commit()
            await event.respond("**gopay number successfully changed!**")
        else:
            await event.respond("**email not found error code 404**")
            sys.exit()  
    except sqlite3.Error as e:
        print("Gagal mengubah nomor dana:", e)
    finally:
        conn.close()








def tampilkan_dana_gopay():
    conn = sqlite3.connect('cybervpn/database.db')
    c = conn.cursor()

    c.execute("SELECT COALESCE(dana, 'NULL'), COALESCE(gopay, 'NULL') FROM ewallet")
    data = c.fetchall()

    dana_gopay_list = []  

    for dana, gopay in data:
        dana_gopay_list.append(f"**Dana:** `{dana if dana != 'NULL' else 'NULL'}`\n**GoPay:** `{gopay if gopay != 'NULL' else 'NULL'}`")

    conn.close()

    return dana_gopay_list  
tampilkan_dana_gopay()













def hapus_user(user_id):
    db = get_db()
    db.execute("DELETE FROM user WHERE user_id=?", (user_id,))
    db.commit()



def tampilkan_semua_user():
    db = get_db()
    users = db.execute("SELECT * FROM user").fetchall()

    user_info = []
    for user in users:
        user_info.append(f"**ID:** `{user['user_id']}` \n**Saldo:** `RP.{user['saldo']}` \n**Level: {user['level']}**")

    return user_info








def get_saldo_and_level_from_db(user_id):
    db = get_db()
    result = db.execute("SELECT saldo, level FROM user WHERE user_id = ?", (user_id,)).fetchone()

    if result:
        saldo_aji, level = result
        return saldo_aji, level
    else:
        raise ValueError("User not found in the database.")


def get_saldo_from_db(user_id):
    conn = sqlite3.connect('cybervpn/database.db')
    cursor = conn.cursor()

    # Ubah query untuk mengambil saldo berdasarkan user_id
    cursor.execute(f"SELECT saldo FROM user WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    conn.close()

    # Periksa apakah ada hasil dari query
    if result:
        saldo = result[0]
        return saldo
    else:
        # Jika tidak ada hasil, kembalikan None atau nilai default yang sesuai
        return None






# ...

# Fungsi terkait database
def connect_to_database():
    connection = sqlite3.connect('cybervpn/database.db')
    cursor = connection.cursor()
    return connection, cursor



#saldo ssh


import sys

async def process_user_balance_ssh(event, user_id):
    connection, cursor = connect_to_database()

    try:
        cursor.execute("SELECT saldo FROM user WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            saldo_str = user_data[0]

            try:
                saldo = int(saldo_str)
            except ValueError:
                print("Error: Unable to convert saldo to an integer.")
                return

            if saldo >= 10000:  # Hanya lanjutkan jika saldo mencukupi
                saldo -= 10000
                cursor.execute("UPDATE user SET saldo = ? WHERE user_id = ?", (saldo, user_id))
                connection.commit()

                
                 
            else:
                await event.respond("**Saldo tidak mencukupi untuk operasi ini.**")
                sys.exit()  
    finally:
        connection.close()


##



#saldo vmess


async def process_user_balance_vmess(event, user_id):
    connection, cursor = connect_to_database()

    try:
        cursor.execute("SELECT saldo FROM user WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            saldo_str = user_data[0]

            try:
                saldo = int(saldo_str)
            except ValueError:
                print("Error: Unable to convert saldo to an integer.")
                return

            if saldo >= 10000:  # Hanya lanjutkan jika saldo mencukupi
                saldo -= 10000
                cursor.execute("UPDATE user SET saldo = ? WHERE user_id = ?", (saldo, user_id))
                connection.commit()

                
                 
            else:
                await event.respond("**Saldo tidak mencukupi untuk operasi ini.**")
                sys.exit()  
    finally:
        connection.close()


##





#saldo trojan


async def process_user_balance_trojan(event, user_id):
    connection, cursor = connect_to_database()

    try:
        cursor.execute("SELECT saldo FROM user WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            saldo_str = user_data[0]

            try:
                saldo = int(saldo_str)
            except ValueError:
                print("Error: Unable to convert saldo to an integer.")
                return

            if saldo >= 10000:  # Hanya lanjutkan jika saldo mencukupi
                saldo -= 10000
                cursor.execute("UPDATE user SET saldo = ? WHERE user_id = ?", (saldo, user_id))
                connection.commit()

                
                 
            else:
                await event.respond("**Saldo tidak mencukupi untuk operasi ini.**")
                sys.exit()  
    finally:
        connection.close()




#saldo vless


async def process_user_balance_vless(event, user_id):
    connection, cursor = connect_to_database()

    try:
        cursor.execute("SELECT saldo FROM user WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            saldo_str = user_data[0]

            try:
                saldo = int(saldo_str)
            except ValueError:
                print("Error: Unable to convert saldo to an integer.")
                return

            if saldo >= 10000:  # Hanya lanjutkan jika saldo mencukupi
                saldo -= 10000
                cursor.execute("UPDATE user SET saldo = ? WHERE user_id = ?", (saldo, user_id))
                connection.commit()

                
                 
            else:
                await event.respond("**Saldo tidak mencukupi untuk operasi ini.**")
                sys.exit()  
    finally:
        connection.close()




        





def check_user_registration(user_id):
    try:
        x = sqlite3.connect("cybervpn/database.db")
        c = x.cursor()
        c.execute("SELECT * FROM user WHERE user_id=?", (user_id,))
        user_data = c.fetchone()

        if user_data is None:
            return False  
        else:
            return True  

    except sqlite3.Error as se:
        print(f"SQLite Error: {se}")
        return False  






def get_user_count():
    db_connection = sqlite3.connect('cybervpn/database.db')
    cursor = db_connection.cursor()
    query = "SELECT COUNT(*) FROM user"
    
    try:
        cursor.execute(query)
        user_count = cursor.fetchone()[0]
        return user_count
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db_connection.close()
total_users = get_user_count()
print(f"Total Users in the Database: {total_users}")




def get_level_from_db(user_id):
    db = get_db()
    result = db.execute("SELECT level FROM user WHERE user_id = ?", (user_id,)).fetchone()

    print(f"Query result for user_id {user_id}: {result}")

    if result:
        level = result[0]
        return level
    else:
        raise ValueError("User not found in the database.")


##status service

def get_ssh_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'ssh'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴 [died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'





def get_xray_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'xray'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'






def get_udp_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'udp-custom'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'





def get_noobz_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'noobzvpns'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'




def get_ddos_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'ddos'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'




def get_ws_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'ws-dropbear'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'






def get_dropbear_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'dropbear'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'




def get_slowdns_status():
    try:
 
        result = subprocess.run(['systemctl', 'status', 'client-sldns'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        for line in output_lines:
            if 'Active:' in line:
                if 'inactive' in line or 'dead' in line:
                    return '🔴[died]'
                elif 'running' in line:
                    return '🟢[ok]'
        return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'







xray_status = get_xray_status()
print(f"Status xray: {xray_status}")

ssh_status = get_ssh_status()
print(f"Status SSh: {ssh_status}")

udp_status = get_udp_status()
print(f"Status UDP: {udp_status}")

noobz_status = get_noobz_status()
print(f"Status NOOBZ: {noobz_status}")


ddos_status = get_ddos_status()
print(f"Status DDOS: {ddos_status}")


ws_status = get_ws_status()
print(f"Status websocket: {ws_status}")


dropbear_status = get_dropbear_status()
print(f"Status dropbear: {dropbear_status}")


slowdns_status = get_slowdns_status()
print(f"Status slowdns: {slowdns_status}")




def valid(user_id, level="user"):
    db = get_db()
    x = db.execute(f"SELECT user_id FROM {level}").fetchall()
    a = [v[0] for v in x]
    return str(user_id in a)

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

