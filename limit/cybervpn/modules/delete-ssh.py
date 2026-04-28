from cybervpn import *
import subprocess
@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
    user_id = str(event.sender_id)
    async def delete_ssh_(event):
        async with bot.conversation(chat) as user:
            await event.respond("**Username To Be Deleted:**")
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        try:
            subprocess.check_output(f"userdel -f {user}", shell=True)
        except subprocess.CalledProcessError:
            await event.respond(f"**User** `{user}` **Not Found**")
        else:
            await event.respond(f"**Successfully Deleted** `{user}`")

    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await delete_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak..!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

