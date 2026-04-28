from cybervpn import *
import datetime as DT
import requests


@bot.on(events.CallbackQuery(data=b'gantimail'))
async def saldo_handler(event):
    user_id = event.sender_id  
    chat_id = event.chat_id  

    async def get_input(conv, prompt):
        await event.respond(prompt)
        input_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=user_id))
        return input_msg.raw_text

    async with bot.conversation(chat_id) as old_conv:  
        old = await get_input(old_conv, '**masukan email lama mu:**')

    async with bot.conversation(chat_id) as new_conv:  
        new = await get_input(new_conv, '**Masukkan email baru mu:**')

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await edit_email_ewallet(old, new, event)
            today = DT.date.today()
            later = today + DT.timedelta(days=int(0))
            msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ Successful email change ⟩**
**━━━━━━━━━━━━━━━━━**
**» Your ID:** `{user_id}`
**» old email:** `{old}`
**» New email:** `{new}`
**» status:** `success✅`
**━━━━━━━━━━━━━━━━**
**» Change date:** `{later}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
            inline = [
                [Button.url("[ Contact ]", "wa.me/6281327393959"),
                 Button.url("[ wahtsap ]", "t.me/ARI_VPN_STORE")]
            ]
            await event.respond(msg, buttons=inline)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')





@bot.on(events.CallbackQuery(data=b'dana'))
async def dana_handler(event):
    user_id = event.sender_id  
    chat_id = event.chat_id  

    async def get_input(conv, prompt):
        await event.respond(prompt)
        input_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=user_id))
        return input_msg.raw_text

    async with bot.conversation(chat_id) as email_conv: 
        email = await get_input(email_conv, '**input your email:**')

    async with bot.conversation(chat_id) as dana_conv:  
        dana = await get_input(dana_conv, '**Input your new dana number:**')

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await edit_nomor_dana_ewallet(event, email, dana)
            today = DT.date.today()
            later = today + DT.timedelta(days=int(0))
            msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ Successful dana change ⟩**
**━━━━━━━━━━━━━━━━━**
**» Your ID:** `{user_id}`
**» your email:** `{email}`
**» New dana id number:** `{dana}`
**» status:** `success✅`
**━━━━━━━━━━━━━━━━**
**» Change date:** `{later}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
            inline = [
                [Button.url("[ Contact ]", "wa.me/6281327393959"),
                 Button.url("[ Channel ]", "t.me/ARI_VPN_STORE")]
            ]
            await event.respond(msg, buttons=inline)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')




@bot.on(events.CallbackQuery(data=b'gopay'))
async def dana_handler(event):
    user_id = event.sender_id  
    chat_id = event.chat_id  

    async def get_input(conv, prompt):
        await event.respond(prompt)
        input_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=user_id))
        return input_msg.raw_text

    async with bot.conversation(chat_id) as email_conv: 
        email = await get_input(email_conv, '**Input your email:**')

    async with bot.conversation(chat_id) as gopay_conv:  
        gopay = await get_input(gopay_conv, '**Input your new gopay number:**')

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await edit_nomor_gopay_ewallet(event, email, gopay)
            today = DT.date.today()
            later = today + DT.timedelta(days=int(0))
            msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ Successful gopay change ⟩**
**━━━━━━━━━━━━━━━━━**
**» Your ID:** `{user_id}`
**» your email:** `{email}`
**» New gopay id number:** `{gopay}`
**» status:** `success✅`
**━━━━━━━━━━━━━━━━**
**» Change date:** `{later}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
            inline = [
                [Button.url("[ Contact ]", "wa.me/6281327393959"),
                 Button.url("[ Channel ]", "t.me/ARI_VPN_STORE")]
            ]
            await event.respond(msg, buttons=inline)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')













@bot.on(events.CallbackQuery(data=b'wallet'))
async def wallet_handler(event):
    user_id = event.sender_id  
    chat_id = event.chat_id  

    async def get_input(conv, prompt):
        await event.respond(prompt)
        input_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=user_id))
        return input_msg.raw_text

    async with bot.conversation(chat_id) as email_conv:  
        email = await get_input(email_conv, '**masukan email mu:**')

    async with bot.conversation(chat_id) as dana_conv:  
        dana = await get_input(dana_conv, '**Masukkan no dana mu :**')

    async with bot.conversation(chat_id) as gopay_conv:  
        gopay = await get_input(gopay_conv, '**Masukkan no gopay mu:**')

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level is not None and level == 'admin':
            await tambah_data_ewallet(email, dana, gopay, event)
            today = DT.date.today()
            later = today + DT.timedelta(days=int(0))
            msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ Successful add e-wallet ⟩**
**━━━━━━━━━━━━━━━━━**
**» Your email:** `{email}`
**» id dana:** `{dana}`
**» id gopay:** `{gopay}`
**» status:** `success✅`
**━━━━━━━━━━━━━━━━**
**» Change date:** `{later}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
            inline = [
                [Button.url("[ Contact ]", "wa.me/6281327393959"),
                 Button.url("[ Channel ]", "t.me/ARI_VPN_STORE")]
            ]
            await event.respond(msg, buttons=inline)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')


















@bot.on(events.CallbackQuery(data=b'ewallet'))
async def wallet(event):
    user_id = str(event.sender_id)
    
    async def wallet_(event):
        inline = [
            [Button.inline(" GANTI EMAIL", "gantimail")],
            [Button.inline(" TAMBAH E WALLET", "wallet")],
            [Button.inline(" GANTI NO DANA", "dana")],
              [Button.inline(" GANTI NO GOPAY", "gopay")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ 🕊E-WALLET SETTINGS🕊 ⟩**
**━━━━━━━━━━━━━━━━**
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await wallet_(event)
        else:
            await event.answer('Akses Ditolak..!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')






