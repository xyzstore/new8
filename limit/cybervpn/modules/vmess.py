from cybervpn import *
import subprocess
import json
import re
import base64
import datetime as DT
import requests
import time

# ... (kode lainnya)

@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
    async def create_vmess_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = (await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**expired days?:**')
            exp = (await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as ip_conv:
            await event.respond('**ip limit:**')
            ip = (await ip_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**Quota limit:**')
            Quota = (await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).raw_text

        cmd = f'printf "%s\n" "{user}" "{exp}" "{Quota}" "{ip}" | addws'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("vmess://(.*)", a)]

        z = base64.b64decode(b[0].replace("vmess://", "")).decode("ascii")
        z = json.loads(z)

        z1 = base64.b64decode(b[1].replace("vmess://", "")).decode("ascii")
        z1 = json.loads(z1)

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**    Vmess Account    **
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{DOMAIN}`
**» User Quota   :** `{Quota} GB`
**» limit IP  :** `{ip} IP`
**» port TLS     :** `443`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» AlterId      :** `0`
**» Security     :** `auto`
**» User ID      :** `{z["id"]}`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `bug.com/vmess`
**» Path NLS     :** `bug.com/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC    :** 
`{b[2].strip("'")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
*» 💌@ARI_VPN_STORE**
**◇━━━━━━━━━━━━━━━━━◇**
**openclass:**
http://{DOMAIN}:81/vmess-{z["ps"]}.yaml
**◇━━━━━━━━━━━━━━━━━◇**
**Link qr:**
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
            await create_vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')





# TRIAL VMESS
@bot.on(events.CallbackQuery(data=b'trial-vmess'))
async def trial_vmess(event):
    async def trial_vmess_(event):
        # loading animasi
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

        # output cmd
        cmd = f'printf "%s\n" "Trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "1" "1" | addws'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            print(f'Error: {e}')
            print(f'Subprocess output: {a}')
            await event.respond(f"An error occurred: {e}\nSubprocess output: {a}")
            return  # Stop execution if there's an error

        today = DT.date.today()
        later = today + DT.timedelta(days=1)  # You may need to adjust this, as "exp" is not defined in the scope
        b = [x.group() for x in re.finditer("vmess://(.*)", a)]

        z = base64.b64decode(b[0].replace("vmess://", "")).decode("ascii")
        z = json.loads(z)

        z1 = base64.b64decode(b[1].replace("vmess://", "")).decode("ascii")
        z1 = json.loads(z1)

        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
    ** Vmess Account **
**◇━━━━━━━━━━━━━━━━━◇**
**» Domain       :** `{DOMAIN}`
**» User Quota   :** `1 GB`
**» limit IP  :** `1 IP`
**» port TLS     :** `443`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `bug.com/vmess`
**» Path NLS     :** `bug.com/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC    :** 
`{b[2].strip("'")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `1 hari`
*» 💌@ARI_VPN_STORE**
**◇━━━━━━━━━━━━━━━━━◇**
**openclass:**
http://{DOMAIN}:81/vmess-{z["ps"]}.yaml
**◇━━━━━━━━━━━━━━━━━◇**
**Link qr:**
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
            await trial_vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

#CEK VMESS
@bot.on(events.CallbackQuery(data=b'cek-vmess'))
async def cek_vmess(event):
    async def cek_vmess_(event):
        cmd = 'cek-ws'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
╔═╗─╔╗──────────╔═╦═╗
║╔╬═╣╠╗╔═╦═╦══╦═╣═╣═╣
║╚╣╩╣═╣╚╗║╔╣║║║╩╬═╠═║
╚═╩═╩╩╝─╚═╝╚╩╩╩═╩═╩═╝
{z}

**Shows Logged In Users Vmess**
""", buttons=[[Button.inline("‹ Main Menu ›", "vmess")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



## CEK member VMESS
@bot.on(events.CallbackQuery(data=b'cek-member'))
async def cek_vmess(event):
    async def cek_vmess_(event):
        cmd = 'bash cek-mws'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""

{z}

**Shows Users from databases**
""", buttons=[[Button.inline("‹ Main Menu ›", "vmess")]])

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await cek_vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')





@bot.on(events.CallbackQuery(data=b'delete-vmess'))
async def delete_vmess(event):
    async def delete_vmess_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'printf "%s\n" "{user}" | delws'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Deleted {user} **"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await delete_vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')
        

@bot.on(events.CallbackQuery(data=b'renew-vmess'))
async def ren_vmess(event):
    async def ren_vmess_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text

        async with bot.conversation(chat) as exp_conv:
            await event.respond('**expired days?:**')
            exp = await exp_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            exp = exp.raw_text
            
        async with bot.conversation(chat) as ip_conv:
            await event.respond('**ip limit:**')
            ip = await ip_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip = ip.raw_text
            
        async with bot.conversation(chat) as Quota_conv:
            await event.respond('**Quota usage?:**')
            Quota = await Quota_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            Quota = Quota.raw_text  

        cmd = f'printf "%s\n" "{user}" "{exp}" "{Quota}" "{ip}" | renewws'

        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Renewed  {user} {exp} Days Limit {ip} IP Quota usage {Quota} GB**"""
            await event.respond(msg)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ren_vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')








		
@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
    async def vmess_(event):
        inline = [
            [Button.inline(" TRIAL VMESS ", "trial-vmess"),
             Button.inline(" CREATE VMESS ", "create-vmess")],
            [Button.inline(" CHECK LOGIN VMESS ", "cek-vmess"),
             Button.inline(" DELETE VMESS ", "delete-vmess")],
            [Button.inline(" RENEW VMESS ", "renew-vmess")],
            [Button.inline(" CHECK MEMBER ", "cek-member"),
             Button.inline("‹ Main Menu ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
     `•vmess manager•`
**◇━━━━━━━━━━━━━━━━━◇**
**» Service:** `VMESS`
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
            await vmess_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')



