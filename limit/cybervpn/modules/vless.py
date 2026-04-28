from cybervpn import *
import requests
import subprocess
import time
@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
    async def create_vless_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond('**exp:**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text

        async with bot.conversation(chat) as ip:
            await event.respond('**ip limit:**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text

        async with bot.conversation(chat) as Quota:
            await event.respond('**Quota usage:**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text

        
        

        await event.edit("`Wait.. Setting up an Account`")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{Quota}" "{ip}" | add-vless'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        x = [x.group() for x in re.finditer("vless://(.*)", a)]
        print(x)
        uuid = re.search("vless://(.*?)@", x[0]).group(1)
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
     `•Vless Account•`
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{user}`
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `{Quota} GB`
**» Port TLS    :** `443-900`
**» Port NTLS   :** `80`
**» Port Grpc   :** `443`
**» Network     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `vless `
**» Path Dynamic:** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC  :**
`{x[2].replace(" ","")}`

**◇━━━━━━━━━━━━━━━━━◇**
**openclass:**
http://{DOMAIN}:81/vless-{user}.yaml
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
*» 💌@ARI_VPN_STORE**
**◇━━━━━━━━━━━━━━━━━◇**
**» Link QR  :**
https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={x[0]}
"""
        await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await create_vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

@bot.on(events.CallbackQuery(data=b'cek-vless'))
async def cek_vless(event):
    async def cek_vless_(event):
        cmd = 'cek-vless'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
╔═╗─╔╗╔╗─╔╗───╔═╦═╗
║╔╬═╣╠╣╚╦╝╠╗╔═╣═╣═╣
║╚╣╩╣═╬╗║╔╣╚╣╩╬═╠═║
╚═╩═╩╩╝╚═╝╚═╩═╩═╩═╝
{z}

**Shows Logged In Users Vless**
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

		
@bot.on(events.CallbackQuery(data=b'renew-vless'))
async def ren_vless(event):
    async def ren_vless_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text

        async with bot.conversation(chat) as exp:
            await event.respond('**expired days?:**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text


        async with bot.conversation(chat) as ip:
            await event.respond('**IP limit?:**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text


        async with bot.conversation(chat) as Quota:
            await event.respond('**Quota usage??:**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text

        
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(1)
        await event.edit("`Processing Create Premium Account`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        
        time.sleep(1)
        await event.edit("`Wait.. Setting up an Account`")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{Quota}" "{ip}" | renewvless'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed {user} {exp} Days, limit ip {ip}, limit Quota {Quota} GB**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ren_vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


# CEK member VLESS
@bot.on(events.CallbackQuery(data=b'cek-membervl'))
async def cek_vless(event):
    async def cek_vless_(event):
        cmd = 'bash cek-mvs'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

{z}

**Shows Users from databases**
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
    async def delete_vless_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(1)
        await event.edit("`Processing Crate Premium Account`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        time.sleep(1)
        await event.edit("`Wait.. Setting up an Account`")
        cmd = f'printf "%s\n" "{user}" | del-vless'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Deleted**"""
            await event.respond(msg)


    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await delete_vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



@bot.on(events.CallbackQuery(data=b'trial-vless'))
async def trial_vless(event):
    async def trial_vless_(event):
        cmd = f'printf "%s\n" "Trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "1" "1" | add-vless'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(1))
            x = [x.group() for x in re.finditer("vless://(.*)", a)]
            print(x)
            remarks = re.search("#(.*)", x[0]).group(1)
            # domain = re.search("@(.*?):", x[0]).group(1)
            uuid = re.search("vless://(.*?)@", x[0]).group(1)
            # path = re.search("path=(.*)&", x[0]).group(1)
            msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
    `•Vless Account•`
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» Port DNS    :** `443, 53`
**» port TLS    :** `443`
**» Port NTLS   :** `80`
**» Port Grpc   :** `443`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `/vless `
**» Path Dynamic:** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**openclass:**
http://{DOMAIN}:81/vless-{remarks}.yaml
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until :** `60 Minutes`
**» 💌@ARI_VPN_STORE**
**◇━━━━━━━━━━━━━━━━━◇**
**» Link QR  :**
https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={x[0]}
"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await trial_vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
    async def vless_(event):
        inline = [
            [Button.inline("TRIAL VLESS", "trial-vless"),
             Button.inline("CREATE VLESS", "create-vless")],
            [Button.inline("CHECK VLESS", "cek-vless"),
             Button.inline("RENEW VLESS", "renew-vless")],
[Button.inline("DELETE VLESS", "delete-vless")],
            [Button.inline("CHEK MEMBER", "cek-membervl")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
    `•vless manager•`
**◇━━━━━━━━━━━━━━━━━◇**
**  Service:** `VLESS`
**  Hostname/IP:** `{DOMAIN}`
**  ISP:** `{z["isp"]}`
**  Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
        await event.edit(msg, buttons=inline)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await vless_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

