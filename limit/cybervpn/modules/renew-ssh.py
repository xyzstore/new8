import subprocess
from cybervpn import *

@bot.on(events.CallbackQuery(data=b'renew-ssh'))
async def ren_ssh(event):
    async def ren_ssh_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user = (await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).message.message.strip()

        async with bot.conversation(chat) as days_conv:
            await event.respond('**Expired days?:**')
            days = (await days_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))).message.message.strip()

        try:
            
            expiration = (datetime.utcnow() + timedelta(days=int(days))).strftime("%Y-%m-%d")

     
            subprocess.check_output(
                f'''
                passwd -u {user}
                usermod -e {expiration} {user}
                ''',
                shell=True
            )
            msg = f'**Successfully Renewed {user} for {days} Days**'
            await event.respond(msg)

        except subprocess.CalledProcessError as e:
            await event.respond(f"Error: {e.stderr}")
        except Exception as e:
            await event.respond(f"Error: {e}")

    user_id = str(event.sender_id)
    chat = event.chat_id
    sender = await event.get_sender()

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await ren_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

