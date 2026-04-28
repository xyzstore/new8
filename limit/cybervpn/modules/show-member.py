from cybervpn import *
from telethon import events, Button

@bot.on(events.CallbackQuery(data=b'show-user'))
async def show_user(event):
    async def show_user_(event):
        try:
            users_data = tampilkan_semua_user()

            if users_data:
                user_info_str = "\n**━━━━━━━━━━━━━━━━━━**\n".join(users_data)
                msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     🌹 list your member 🌹**
**◇━━━━━━━━━━━━━━━━━◇**
{user_info_str}
**◇━━━━━━━━━━━━━━━━━◇**
**Total user:** `{get_user_count()}`
**◇━━━━━━━━━━━━━━━━━◇**
                """
                buttons = [[Button.inline("‹ Main Menu ›", "menu")]]
                await event.respond(msg, buttons=buttons)
            else:
                await event.respond("Data pengguna tidak tersedia saat ini.")

        except Exception as e:
            print(f'Error: {e}')
            await event.respond(f"An error occurred: {e}")

    user_id = str(event.sender_id)

    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'admin':
            await show_user_(event)
        else:
            await event.answer(f'Akses Ditolak. Level: {level}', alert=True)
    except Exception as e:
        print(f'Error: {e}')

