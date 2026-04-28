from cybervpn import *
from telethon import events, Button
import random
import sys
from datetime import datetime, timedelta
import asyncio
import time

async def main(event):
    durasi = 60
    print("Timer dimulai untuk 1 menit.")
    await asyncio.sleep(durasi)
    await event.respond("Waktu transaksi sudah  habis!")

@bot.on(events.CallbackQuery(data=b'topup'))
async def topup_user(event):
    async def topup_user_(event):
        random_numbers = [random.randint(0, 99) for _ in range(3)]
        async with bot.conversation(chat) as nominal_conv:
            await event.edit('**Input nominal topup:**')
            nominal_msg = await nominal_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            nominal = int(nominal_msg.raw_text.strip()) if nominal_msg.raw_text.strip().isdigit() else 0

        if nominal < 10000:
            await event.respond("**Nominal tidak memenuhi syarat. minimal transaksi RP.10.000.**")
            sys.exit()  
        else:
            result = sum(random_numbers) + nominal
            waktu_awal = datetime.now()
            waktu_expired = waktu_awal + timedelta(minutes=1)

        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(1)
        await event.edit("`Processing transaction`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 100%\n█████████████████████████ `")

        try:
            dana_gopay_list = tampilkan_dana_gopay()

            if dana_gopay_list:
                dana_gopay_str = "\n".join(dana_gopay_list)
                msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     🌹 Informasi Pembayaran 🌹**
**◇━━━━━━━━━━━━━━━━━◇**
{dana_gopay_str}
**◇━━━━━━━━━━━━━━━━━◇**
** Nominal yang harus di bayar:**
** TRX:** RP.`{result}`
** Kode transaksi:** `{sum(random_numbers)}`
** Waktu transaksi hanya 1 menit**
** Waktu transaksi: {waktu_awal.strftime("%H:%M:%S")}**
** Expired transaksi: {waktu_expired.strftime("%H:%M:%S")}**
**◇━━━━━━━━━━━━━━━━━◇**
**Notice:** Setelah melakukan topup, harap kirim bukti transfer ke admin @ARI_VPN_STORE untuk mempercepat proses transaksi!
**◇━━━━━━━━━━━━━━━━━◇**
                """
                buttons = [[Button.inline("‹ Main Menu ›", "menu")]]
                await event.respond(msg, buttons=buttons)
                await main(event)
            else:
                await event.respond("Data pengguna tidak tersedia saat ini.")

        except Exception as e:
            print(f'Error: {e}')
            await event.respond(f"Terjadi kesalahan: {e}")

    chat = event.chat_id
    sender = await event.get_sender()
    user_id = str(event.sender_id)

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await topup_user_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

