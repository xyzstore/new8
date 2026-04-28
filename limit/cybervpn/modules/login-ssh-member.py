from cybervpn import *
import subprocess
# CEK VMESS
@bot.on(events.CallbackQuery(data=b'login-ssh-member'))
async def cek_ssh(event):
    user_id = str(event.sender_id)
    
    async def cek_ssh_(event):
        cmd = 'cek-ssh'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
        
        {z}
        
        **Shows Logged In Users ssh**
        """, buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await cek_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

