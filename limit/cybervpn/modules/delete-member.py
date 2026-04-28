from cybervpn import *
import subprocess
import datetime as DT
import asyncio

@bot.on(events.CallbackQuery(data=b'delete-member'))
async def delete_handler(event):
    chat = event.chat_id
    sender = await event.get_sender()
    user_id = str(event.sender_id)

    async def delete_member(telegram_id):
        hapus_user(telegram_id)
        today = DT.date.today()
        later = today + DT.timedelta(days=int(0))
        msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ 🕊 delete successfully 🕊 ⟩**
**━━━━━━━━━━━━━━━━**
**» Member ID:** `{telegram_id}`
**» status account:** `deleted✅`
**━━━━━━━━━━━━━━━━**
**» Date of deletion:** `{later}`
**» 💌@ARI_VPN_STORE**
**━━━━━━━━━━━━━━━━**
"""
        inline = [
            [Button.url("[ Contact ]", "wa.me/6281327393959"),
             Button.url("[ Channel ]", "t.me/ARI_VPN_STORE")]
        ]
        await event.respond(msg, buttons=inline)

    async with bot.conversation(chat) as conv:
        try:
            # Input Telegram ID
            await conv.send_message('**Input Telegram ID member:**')
            id_msg = await conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            telegram_id = id_msg.raw_text

            await delete_member(telegram_id)

            user_level = get_level_from_db(user_id)
            print(f'Retrieved level from database: {user_level}')

            if user_level == 'admin':
                await delete_handler(event)
            else:
                await event.answer(f'Akses Ditolak..!!', alert=True)

        except asyncio.TimeoutError:
            print("Timeout occurred during conversation.")
            await event.respond("Percakapan timeout. Silakan coba lagi.")
        except Exception as e:
            print(f'Error: {e}')

