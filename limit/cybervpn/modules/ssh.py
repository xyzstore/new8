import requests
from cybervpn import *

@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
    async def ssh_member_manager(event):
        inline = [
            [Button.inline("[ Trial SSH ]", "trial-ssh-member"),
             Button.inline("[ Create SSH ]", "create-ssh-member")],
            [Button.inline("[ Check Login SSH ]", "login-ssh-member")],
            [Button.inline("[ Show All User SSH ]", "show-ssh-member")],
[Button.inline("[ Renew SSH ]", "renew-ssh-member")],
            [Button.inline("‹ Main Menu ›", "menu")]]
        
        location_info = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**━━━━━━━━━━━━━━━━**
`•ssh member manager•`
**━━━━━━━━━━━━━━━━**
**» Service:** `SSH`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{location_info["isp"]}`
**» Country:** `{location_info["country"]}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
        await event.edit(msg, buttons=inline)

    async def ssh_admin_manager(event):
        inline = [
            [Button.inline("[ Trial SSH ]", "trial-ssh"),
             Button.inline("[ Create SSH ]", "create-ssh"),
             Button.inline("[ Delete SSH ]", "delete-ssh")],
            [Button.inline("[ Check Login SSH ]", "login-ssh")],
            [Button.inline("[ Show All User SSH ]", "show-ssh")],
[Button.inline("[ Renew SSH ]", "renew-ssh")],
            [Button.inline("‹ Main Menu ›", "menu")]]
        
        location_info = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
**━━━━━━━━━━━━━━━━**
`•ssh admin manager•`
**━━━━━━━━━━━━━━━━**
**» Service:** `SSH`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{location_info["isp"]}`
**» Country:** `{location_info["country"]}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
        await event.edit(msg, buttons=inline)

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ssh_admin_manager(event)
        else:
            await ssh_member_manager(event)
    except Exception as e:
        print(f'Error: {e}')

