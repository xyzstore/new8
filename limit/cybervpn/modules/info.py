from cybervpn import *
import subprocess
import time

@bot.on(events.CallbackQuery(data=b'info'))
async def info_vps(event):
    async def info_vps_(event):
        cmd = 'cat log-install.txt'.strip()
        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(3)
        
        progress_steps = [0, 4, 8, 20, 36, 52, 84, 100]
        for step in progress_steps:
            await event.edit(f"`Processing... {step}%\n{'█' * (step // 4)}{'▒' * ((100 - step) // 4)}`")
            time.sleep(1)
        
        await event.edit("`Wait.. Setting up Server Data`")

        try:
            x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            print(x)
            z = subprocess.check_output(cmd, shell=True).decode("utf-8")
            await event.respond(f"```{z}```", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])
            
            chat = event.chat_id
            sender = await event.get_sender()
            level = get_level_from_db(user_id)
            print(f'Retrieved level from database: {level}')

            if level == 'admin':
                await create_ssh_(event)
            else:
                await event.answer(f'Akses Ditolak..!!', alert=True)

        except Exception as e:
            print(f'Error: {e}')

    await info_vps_(event)

