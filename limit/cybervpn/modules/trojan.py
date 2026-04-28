from cybervpn import *
import requests
import subprocess
@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def create_trojan(event):
    async def create_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond('**Choose Exp:**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text

        async with bot.conversation(chat) as ip:
            await event.respond('**Choose ip limit:**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text
        
        async with bot.conversation(chat) as Quota:
            await event.respond('**Choose limit Quota:**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text


        await event.edit("`Wait.. Setting up an Account`")
        cmd = f'printf "%s\n" "{user}" "{exp}" "{Quota}" "{ip}" | addtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"Terjadi kesalahan: {e}\nSubproses output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("trojan://(.*)", a)]
        print(b)
        domain = re.search("@(.*?):", b[0]).group(1)
        uuid = re.search("trojan://(.*?)@", b[0]).group(1)
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
`•websocket•`
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{user}`
**» User Quota  :** `{Quota} GB`
**» limit ip.   :** `{ip} IP`
**» port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port GRPC    :** `443`
**» User ID     :** `{uuid}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `bug.com/trojan`
**» Path NLS     :** `bug.com/trojan`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `trojan-grpc`
**━━━━━━━━━━━━━━━━**
**» Link TLS   : **
`{b[0]}`
**━━━━━━━━━━━━━━━━**
**» Link WS    :** 
`{b[0].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» Link GRPC  :** 
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**openclass:**
http://{DOMAIN}:81/trojan-{user}.yaml
**◇━━━━━━━━━━━━━━━━━◇**
**Expired Until:** `{later}`
*» 💌@ARI_VPN_STORE**
**◇━━━━━━━━━━━━━━━━━◇**
https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={b[0]}
"""
        await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await create_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

@bot.on(events.CallbackQuery(data=b'cek-tr'))
async def cek_trojan(event):
    async def cek_trojan_(event):
        cmd = 'cek-tr'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

╔═╗─╔╗╔╗
║╔╬═╣╠╣╚╦╦╦═╦╦═╗╔═╦╗
║╚╣╩╣═╣╔╣╔╣╬╠╣╬╚╣║║║
╚═╩═╩╩╩═╩╝╚╦╝╠══╩╩═╝
───────────╚═╝
{z}

**Shows Logged In Users Trojan**
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')


@bot.on(events.CallbackQuery(data=b'trial-trojan'))
async def trial_trojan(event):
    async def trial_trojan_(event):
        cmd = f'printf "%s\n" "trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "2" "1" | addtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(1))
            b = [x.group() for x in re.finditer("trojan://(.*)", a)]
            print(b)
            remarks = re.search("#(.*)", b[0]).group(1)
            domain = re.search("@(.*?):", b[0]).group(1)
            uuid = re.search("trojan://(.*?)@", b[0]).group(1)
            msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
    `•websocket•`
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{remarks}`
**» User Quota  :** `1 GB`
**» Limit ip  :** `1 IP`
**» Port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port GRPC    :** `443`
**» User ID     :** `{uuid}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `bug.com/trojan`
**» Path NLS     :** `bug.com/trojan`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `trojan-grpc`
**━━━━━━━━━━━━━━━━**
**» Link TLS   :**
`{b[0]}`
**━━━━━━━━━━━━━━━━**
**» Link GRPC  :**
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**openclass:**
http://{DOMAIN}:81/trojan-{remarks}.yaml
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `60 Minutes`
*» 💌@ARI_VPN_STORE**
**◇━━━━━━━━━━━━━━━━━◇**
https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={b[0]}
"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await trial_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

@bot.on(events.CallbackQuery(data=b'renew-trojan'))
async def ren_trojan(event):
    async def ren_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        
        async with bot.conversation(chat) as exp:
            await event.respond('**Exp Account?:**')
            exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = (await exp).raw_text

        async with bot.conversation(chat) as ip:
            await event.respond('**Limit IP ?:**')
            ip = ip.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = (await ip).raw_text

        async with bot.conversation(chat) as Quota:
            await event.respond('**Quota usage?:**')
            Quota = Quota.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = (await Quota).raw_text


        
        cmd = f'printf "%s\n" "{user}" "{exp}" "{Quota}" "{ip}" | renewtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed {user} {exp} days limit ip {ip} limit Quota {Quota}GB**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ren_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak...!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')



# CEK member tr
@bot.on(events.CallbackQuery(data=b'cek-membertr'))
async def cek_tr(event):
    async def cek_tr_(event):
        cmd = 'bash cek-mts'.strip()
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
            await cek_tr_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')


		
@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def delete_trojan(event):
    async def delete_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'printf "%s\n" "{user}" | deltr'
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
            await delete_trojan_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
    async def trojan_(event):
        inline = [
            [Button.inline(" TRIAL TROJAN ", "trial-trojan"),
             Button.inline(" CREATE TROJAN ", "create-trojan")],
            [Button.inline(" CHECK TROJAN ", "cek-tr"),
             Button.inline(" RENEW TROJAN ", "renew-trojan")],
[Button.inline(" DELETE TROJAN ", "delete-trojan")],
            [Button.inline(" CHECK MEMBER ", "cek-membertr")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
  `•Trojan manager•`
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `TROJAN`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
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
            await trojan_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

