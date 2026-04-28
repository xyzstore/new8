from cybervpn import *
import requests
import time
import subprocess
@bot.on(events.CallbackQuery(data=b'create-shadowsocks'))
async def create_shadowsocks(event):
    user_id = str(event.sender_id)

    async def create_shadowsocks_(event):
        try:
            async with bot.conversation(chat) as user_conv:
                await event.respond('**Username:**')
                user_msg = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                user = (await user_msg).raw_text

            async with bot.conversation(chat) as exp_conv:
                await event.respond('**expired days?:**')
                exp_msg = exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                exp = (await exp_msg).raw_text

            await event.edit("Processing.")
            await event.edit("Processing..")
            await event.edit("Processing...")
            await event.edit("Processing....")
            time.sleep(1)
            await event.edit("`Processing Create Premium Account`")
            time.sleep(1)
            await event.edit("`Wait.. Setting up an Account`")

            

            cmd = f'printf "%s\n" "{user}" "{exp}" | addss'

            a = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Exit code: {e.returncode}")
            print(f"Output: {e.output.decode('utf-8')}")
            await event.respond(f"Error executing command: {e}")
            return  # Stop execution to prevent further processing on error

        except Exception as ex:
            print(f"Unexpected error: {ex}")
            await event.respond("An unexpected error occurred.")
            return  # Stop execution to prevent further processing on error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        x = [x.group() for x in re.finditer("ss://(.*)", a)]
        uuid = re.search("ss://(.*?)@", x[0]).group(1)

        msg = f"""
        
**◇━━━━━━━━━━━━━━━━━◇**
**⟨  SHDWSCSK Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{user}`
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `Unlimited`
**» Pub Key     :** `{PUB}`
**» Port TLS    :** `443`
**» Port NTLS   :** `80`
**» Port GRPC   :** `443`
**» Port DNS    :** `443, 53`
**» Password    :** `{uuid}`
**» Cipers      :** `aes-128-gcm`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `(/multi path)/ss-ws`
**» ServiceName :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS    :**
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link gRPC   :** 
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link QR  :** `Link Via Qris  :https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=${x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
*» 💌@ARI_VPN_STORE**
*◇━━━━━━━━━━━━━━━━━◇**

        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await create_shadowsocks_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')









@bot.on(events.CallbackQuery(data=b'cek-shadowsocks'))
async def cek_shadowsocks(event):
    user_id = str(event.sender_id)
    async def cek_shadowsocks_(event):
        cmd = 'bash cek-mss'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
        
        {z}

**Shows Users Shadowsocks in database**
        """, buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_shadowsocks_(event)
        else:
            await event.answer('Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')




@bot.on(events.CallbackQuery(data=b'cek-shadowsocks-online'))
async def cek_shadowsocks(event):
    user_id = str(event.sender_id)
    async def cek_shadowsocks_(event):
        cmd = 'bash cek-ss'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
        
        {z}

**Shows online Users Shadowsocks**
        """, buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_shadowsocks_(event)
        else:
            await event.answer('Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')



















@bot.on(events.CallbackQuery(data=b'delete-shadowsocks'))
async def delete_shadowsocks(event):
    async def delete_shadowsocks_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user_event = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user_text = (await user_event).raw_text

        cmd = f'printf "%s\n" "{user_text}" | delss'
        try:
            output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except subprocess.CalledProcessError:
            await event.respond("**User Not Found**")
        else:
            msg = "**Successfully Deleted**"
            await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(sender.id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await delete_shadowsocks_(event)
        else:
            await event.answer('Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')







@bot.on(events.CallbackQuery(data=b'trial-shadowsocks'))
async def trial_shadowsocks(event):
    user_id = str(event.sender_id)
    async def trial_shadowsocks_(event):
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
        # ... (other progress edits)
        time.sleep(1)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        time.sleep(1)
        await event.edit("`Wait.. Setting up an Account`")

        try:
            # Assuming this function checks and processes user balance for SSH
            cmd = f'printf "%s\n" "Trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" | addss'
            a = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Exit code: {e.returncode}")
            print(f"Output: {e.output.decode('utf-8')}")
            await event.respond(f"Error executing command: {e}")
            return  # Stop execution to prevent further processing on error

        except Exception as ex:
            print(f"Unexpected error: {ex}")
            await event.respond("An unexpected error occurred.")
            return  # Stop execution to prevent further processing on error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(1))
        x = [x.group() for x in re.finditer("ss://(.*)", a)]
        uuid = re.search("ss://(.*?)@", x[0]).group(1)

        msg = f"""
        
**◇━━━━━━━━━━━━━━━━━◇**
**⟨  Trial SHDWSCSK Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `Unlimited`
**» Pub Key     :** `{PUB}`
**» Port TLS    :** `443`
**» Port NTLS   :** `80`
**» Port GRPC   :** `443`
**» Port DNS    :** `443, 53`
**» Password    :** `{uuid}`
**» Cipers      :** `aes-128-gcm`
**» NetWork     :** `(WS) or (gRPC)`
**» Path        :** `(/multi path)/ss-ws`
**» ServiceName :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS    :**
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link gRPC   :** 
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link QR  :** `Link Via Qris  :https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=${x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
*» 💌@ARI_VPN_STORE**
*◇━━━━━━━━━━━━━━━━━◇**

        """

        await event.respond(msg)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await trial_shadowsocks_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)

    except Exception as e:
        print(f'Error: {e}')










@bot.on(events.CallbackQuery(data=b'renew-ss'))
async def ren_ss(event):
    async def ren_ss_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**expired days?:**')
            exp = await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp.raw_text
            

        cmd = f'printf "%s\n" "{user}" "{exp}" | renew-ss'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed  {user} {exp} Days**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ren_ss_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')







@bot.on(events.CallbackQuery(data=b'shadowsocks'))
async def shadowsocks(event):
    user_id = str(event.sender_id)

    async def shadowsocks_(event):
        inline = [
            [Button.inline("TRIAL SHDWSOCSK", "trial-shadowsocks"),
             Button.inline("CREATE SHDWSOCSK", "create-shadowsocks")],
            [Button.inline("CHECK SHADOWSOCSK", "cek-shadowsocks")],
            [Button.inline("CHECK ONLINE USER", "cek-shadowsocks-online")],
[Button.inline("RENEW USER", "renew-ss")],
[Button.inline("DELETE SHADOWSOCKS USER", "delete-shadowsocks")],
            [Button.inline("‹ Main Menu ›", "menu")]]
        
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
◇⟨ SHDWSK MANAGER ⟩◇
**◇━━━━━━━━━━━━━━━━━◇**
» Service: `SHADOWSOCKS`
» Hostname/IP: `{DOMAIN}`
» ISP: `{z["isp"]}`
» Country: `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""

        await event.edit(msg, buttons=inline)

    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await shadowsocks_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')


