from cybervpn import *
import subprocess
@bot.on(events.CallbackQuery(data=b'show-ssh-member'))
async def show_ssh(event):
    user_id = str(event.sender_id)
    
    async def show_ssh_(event):
        cmd = "awk -F: '($3>=1000)&&($1!='nobody'){print $1}' /etc/passwd"
        x = subprocess.check_output(cmd, shell=True).decode("ascii").split("\n")
        z = []
        for us in x:
            z.append("`" + us + "`")
        zx = "\n".join(z)
        await event.respond(f"""
        **Showing All SSH User**
        
        {zx}
        `
        **Total SSH Account:** `{str(len(z))}`
        """, buttons=[[Button.inline("‹ Main Menu ›", "menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await show_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

