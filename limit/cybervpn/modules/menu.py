from cybervpn import *
from telethon import events, Button
import requests

url = "https://raw.githubusercontent.com/LT-BACKEND/stunnelvpn/momok/statushariini"

response = requests.get(url)


if response.status_code == 200:
    print(response.text)
else:
    print("Gagal mendapatkan konten dari URL")

@bot.on(events.NewMessage(pattern=r"(?:.menu|/start|/menu|.gas|.mulai|.memek|.go|.crot)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def start_menu(event):
    user_id = str(event.sender_id)

    if check_user_registration(user_id):
        try:
            saldo_aji, level = get_saldo_and_level_from_db(user_id)

            if level == "user":
                member_inline = [
                    [Button.inline("Ssh Menu", "ssh")],
                    [Button.inline("Vmess Menu", "vmess-member"),
                     Button.inline("Vless Menu", "vless-member")],
                    [Button.inline("Trojan Menu", "trojan-member"),
                     Button.inline("Socks Menu", "shadowsocks-member")],
                    [Button.inline("Noobzv Vpn", "noobzvpn-member")],
                    [Button.url("✨whatsapp✨", "https://wa.me/6281327393959"),
                     Button.inline("💵Topup Manual💵", f"topup")]
                ]

                member_msg = f"""
**━━━━━━━━━━━━━━━━**
** ARI TUNNELING **
**━━━━━━━━━━━━━━━━**
**Notice:{response.text}**
**━━━━━━━━━━━━━━━━**
**  ➢SERVICE STATUS **
**» ssh status      :** `{get_ssh_status()}`
**» ssh xray        :** `{get_xray_status()}`
**» udp status      :** `{get_udp_status()}`
**» Noobzvpns status:** `{get_noobz_status()}`
**» slowdns status  :** `{get_slowdns_status()}`
**» dropbear status :** `{get_dropbear_status()}`
**» websocket status:** `{get_ws_status()}`
**» Anti DDoS status:** `{get_ddos_status()}`
**━━━━━━━━━━━━━━━━**
**» 🇲🇨Version:** `v4.7.7`
**» 🇲🇨Your ID ** `{user_id}`
**» 🇲🇨SISA SALDO : ** `RP.{saldo_aji}`
**━━━━━━━━━━━━━━━━**
"""
                x = await event.edit(member_msg, buttons=member_inline)
                if not x:
                    await event.reply(member_msg, buttons=member_inline)


            elif level == "admin":
                admin_inline = [
                    [Button.inline("LIBEV SSH", "ssh")],
                    [Button.inline("LIBEV VMESS", "vmess"),
                     Button.inline("LIBEV VLESS", "vless")],
                    [Button.inline("LIBEV TRJAN", "trojan"),
                     Button.inline("LIBEV SS -R", "shadowsocks")],
                    [Button.inline("LIBEV NOOBZ", "noobzvpns"),
                     Button.inline("ADD MEMBER", "registrasi-member"),
                     Button.inline("DEL MEMBER", "delete-member")],
                     [Button.inline("LIST MEMBER", "show-user")],
                    [Button.inline("💰ADD MONEY💰 ", "addsaldo")],
                    [Button.inline("👙CHECKING VPS👙", "info"),
                     Button.inline("👙FEATURES SET👙", "setting")],
                    [Button.url("📩Whatsapp📩", "https://wa.me/6281327393959"),
                     Button.url("📤BuyScript📤", "https://t.me/ARI_VPN_STORE")]
                ]

                admin_msg = f"""
**━━━━━━━━━━━━━━━━**
** ARI TUNNELING **
**━━━━━━━━━━━━━━━━**
**Notice:{response.text}**
**━━━━━━━━━━━━━━━━**
**  ➢SERVICE STATUS **
**» ssh status      :** `{get_ssh_status()}`
**» ssh xray        :** `{get_xray_status()}`
**» udp status      :** `{get_udp_status()}`
**» Noobzvpns status:** `{get_noobz_status()}`
**» slowdns status  :** `{get_slowdns_status()}`
**» dropbear status :** `{get_dropbear_status()}`
**» websocket status:** `{get_ws_status()}`
**» Anti DDoS status:** `{get_ddos_status()}`
**━━━━━━━━━━━━━━━━**
**» 🇲🇨Version:** `v3.1.1`
**» 🇲🇨Your ID ** `{user_id}`
**» 🇲🇨Total databases:** `{get_user_count()}`
**━━━━━━━━━━━━━━━━**
"""
                x = await event.edit(admin_msg, buttons=admin_inline)
                if not x:
                    await event.reply(admin_msg, buttons=admin_inline)

        except Exception as e:
            print(f"Error: {e}")

    else:
        await event.reply(
            f'```Anda belum terdaftar, silahkan registrasi```',
            buttons=[[(Button.inline("Registrasi", "registrasi"))]]
        )

