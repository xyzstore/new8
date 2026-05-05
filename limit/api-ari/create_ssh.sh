#!/bin/bash
export TERM=xterm
export PATH="/usr/sbin:/usr/bin:/sbin:/bin"

user=$1
Pass=$2
iplimit=$3
masaaktif=$4
Login="$user"

validate_username() {
  if [[ -z "$1" ]]; then
    echo "Username tidak boleh kosong." >&2
    exit 1
  fi
  if [[ ! "$1" =~ ^[A-Za-z0-9_-]+$ ]]; then
    echo "Username hanya boleh berisi huruf, angka, underscore (_), dan strip (-)." >&2
    exit 1
  fi
}

username_exists_any_protocol() {
  local u="$1"

  getent passwd "$u" >/dev/null 2>&1 && return 0

  local db
  for db in \
    /etc/ssh/.ssh.db \
    /etc/vmess/.vmess.db \
    /etc/vless/.vless.db \
    /etc/trojan/.trojan.db \
    /etc/shadowsocks/.shadowsocks.db
  do
    [[ -f "$db" ]] && awk -v u="$u" '$2 == u { found=1 } END { exit found ? 0 : 1 }' "$db" && return 0
  done

  [[ -e "/etc/kyt/limit/ssh/ip/$u" ]] && return 0
  [[ -e "/etc/kyt/limit/vmess/ip/$u" ]] && return 0
  [[ -e "/etc/kyt/limit/vless/ip/$u" ]] && return 0
  [[ -e "/etc/kyt/limit/trojan/ip/$u" ]] && return 0
  [[ -e "/etc/kyt/limit/shadowsocks/ip/$u" ]] && return 0

  return 1
}

reject_if_username_exists() {
  local u="$1"
  if username_exists_any_protocol "$u"; then
    echo "Username $u sudah ada di salah satu protokol. Pembuatan akun ditolak." >&2
    exit 1
  fi
}

validate_username "${user:-$Login}"
reject_if_username_exists "${user:-$Login}"

IP=$(curl -sS ipv4.icanhazip.com)
data_server=$(curl -v --insecure --silent https://google.com/ 2>&1 | grep Date | sed -e 's/< Date: //')
date_list=$(date +"%Y-%m-%d" -d "$data_server")
data_ip="https://raw.githubusercontent.com/xyzstore/izin/main/ip"
checking_sc() {
  useexp=$(wget -qO- $data_ip | grep $IP | awk '{print $3}')

  if [[ "$useexp" == "Lifetime" ]]; then
    # Jika useexp adalah "Lifetime", anggap tetap aktif

    return
  fi
  date_list_epoch=$(date -d "$date_list" +%s)
  useexp_epoch=$(date -d "$useexp" +%s 2>/dev/null)

  if [[ $? -ne 0 || $date_list_epoch -gt $useexp_epoch ]]; then
    # Tanggal sekarang lebih besar dari tanggal expired, atau format salah
    echo -e "────────────────────────────────────────────"
    echo -e "          404 NOT FOUND AUTOSCRIPT          "
    echo -e "────────────────────────────────────────────"
    echo -e ""
    echo -e "            PERMISSION DENIED !"
    echo -e "   Your VPS $IP Has been Banned"
    echo -e "     Buy access permissions for scripts"
    echo -e "             Contact Admin :"
    echo -e "      WhatsApp wa.me/6281327393959"
    echo -e "────────────────────────────────────────────"
    exit
  fi
}
checking_sc
if getent group "$Login" > /dev/null; then
    GROUP_OPTION="-g $Login"  # Gunakan grup yang ada
else
    /usr/sbin/groupadd "$Login"  # Buat grup baru
    GROUP_OPTION="-g $Login"
fi

egrep "^$Login" /etc/passwd >/dev/null
if [ $? -eq 0 ]; then
    echo "User $Login sudah ada."
    exit 1
fi
ISP=$(cat /etc/xray/isp)
CITY=$(cat /etc/xray/city)
domain=$(cat /etc/xray/domain)
nama=$(cat /usr/bin/user)
NS=$(cat /etc/xray/dns 2>/dev/null)
PUB=$( cat /etc/slowdns/server.pub 2>/dev/null )
tgl=$(date -d "$masaaktif days" +"%d")
bln=$(date -d "$masaaktif days" +"%b")
thn=$(date -d "$masaaktif days" +"%Y")
expe="$tgl $bln, $thn"
tgl2=$(date +"%d")
bln2=$(date +"%b")
thn2=$(date +"%Y")
tnggl="$tgl2 $bln2, $thn2"
/usr/sbin/useradd -e "$(date -d "$masaaktif days" +"%Y-%m-%d")" -s /bin/false -M $GROUP_OPTION "$Login"
expi="$(chage -l $Login | grep "Account expires" | awk -F": " '{print $2}')"
echo -e "$Pass\n$Pass\n"| passwd $Login &> /dev/null
hariini=`date -d "0 days" +"%Y-%m-%d"`
expi=`date -d "$masaaktif days" +"%Y-%m-%d"`
egrep "^$Login" /etc/passwd >/dev/null
if [ $? -ne 0 ]; then
    echo "Gagal membuat user $Login. Periksa log untuk detail."
    exit 1
fi
if [[ $iplimit -gt 0 ]]; then
mkdir -p /etc/kyt/limit/ssh/ip/
echo -e "$iplimit" > /etc/kyt/limit/ssh/ip/$Login
else
echo > /dev/null
fi

if [ ! -e /etc/ssh ]; then
  mkdir -p /etc/ssh
fi

DATADB=$(cat /etc/ssh/.ssh.db | grep "^#ssh#" | grep -w "${Login}" | awk '{print $2}')
if [[ "${DATADB}" != '' ]]; then
  sed -i "/\b${Login}\b/d" /etc/ssh/.ssh.db
  echo "#ssh# ${Login} ${Pass} ${iplimit} ${expe}" >>/etc/ssh/.ssh.db
else
echo "#ssh# ${Login} ${Pass} ${iplimit} ${expe}" >>/etc/ssh/.ssh.db
fi

mkdir -p /detail/ssh/
#Simpan Detail Akun User
cat > /detail/ssh/$Login.txt <<-END
-----------------------------------------
SSH Account
-----------------------------------------
Host             : $domain
IP               : $IP
Username         : $Login
Password         : $Pass
-----------------------------------------
Limit Ip         : ${iplimit} IP
Host Slowdns     : ${NS}
Pub Key          : ${PUB}
Port OpenSSH     : 22
Port DNS         : 53, 2222
Port SSH UDP     : 1-65535
Port Dropbear    : 22, 109
Port SSH WS      : 80,8080,2086,8880
Port SSH WS SSL  : 443,8443
Port SSL/TLS     : 443
BadVPN UDP       : 7100, 7300, 7300
-----------------------------------------
HTTP CUSTOM      : $domain:1-65535@$Login:$Pass"
-----------------------------------------
Payload          : GET /cdn-cgi/trace HTTP/1.1[crlf]Host: Bug_Kalian[crlf][crlf]GET-RAY / HTTP/1.1[crlf]Host: [host][crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]
-----------------------------------------
Save Link Account: https://$domain:81/ssh-$Login.txt
-----------------------------------------
Aktif Selama     : $masaaktif Hari
Dibuat Pada      : $tnggl
Berakhir Pada    : $expe
-----------------------------------------

END

cat > /var/www/html/ssh-$Login.txt <<-END
-----------------------------------------
SSH Account
-----------------------------------------
Host             : $domain
IP               : $IP
Username         : $Login
Password         : $Pass
-----------------------------------------
Limit Ip         : ${iplimit} IP
Host Slowdns     : ${NS}
Pub Key          : ${PUB}
Port OpenSSH     : 22
Port DNS         : 53, 2222
Port SSH UDP     : 1-65535
Port Dropbear    : 22, 109
Port SSH WS      : 80,8080,2086,8880
Port SSH WS SSL  : 443,8443
Port SSL/TLS     : 443
BadVPN UDP       : 7100, 7300, 7300
-----------------------------------------
HTTP CUSTOM      : $domain:1-65535@$Login:$Pass"
-----------------------------------------
Payload          : GET /cdn-cgi/trace HTTP/1.1[crlf]Host: Bug_Kalian[crlf][crlf]GET-RAY / HTTP/1.1[crlf]Host: [host][crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]
-----------------------------------------
Save Link Account: https://$domain:81/ssh-$Login.txt
-----------------------------------------
Aktif Selama     : $masaaktif Hari
Dibuat Pada      : $tnggl
Berakhir Pada    : $expe
-----------------------------------------

END
CHATID="-1001911868043"
KEY="7876561487:AAHCpsZnu1LGx6w95fhqFMNSCT7fEGdv2vo"
export TIME="10"
export URL="https://api.telegram.org/bot$KEY/sendMessage"
sensor=$(echo "$Login" | sed 's/\(.\{3\}\).*/\1xxx/')
ISP=$(curl -s ipinfo.io/org | cut -d " " -f 2-10 )
clear
export TIME="10"
TEXT="
<b>-----------------------------------------</b>
<b>TRANSACTION SUCCESSFUL</b>
<b>-----------------------------------------</b>
<b>» Produk : SSH</b>
<b>» ISP :</b> <code>${ISP}</code>
<b>» Limit Quota :</b> <code>${Quota} GB</code>
<b>» Limit Login :</b> <code>${iplimit} Hp</code>
<b>» Username :</b> <code>${sensor}</code>
<b>» Duration :</b> <code>${masaaktif} Days</code>
<b>-----------------------------------------</b>
<i>Automatic Notification From Server</i>
<b>-----------------------------------------</b>
"
 
curl -s --max-time $TIME -d "chat_id=$CHATID&disable_web_page_preview=1&text=$TEXT&parse_mode=html" $URL >/dev/null
clear
echo -e " SSH ACCOUNT "
echo -e " Remark      : $Login "
echo -e " Password    : $Pass "
echo -e " Limit Ip    : ${iplimit} IP"
echo -e " Domain      : $domain "
echo -e " Ns Domain : $NS  "
echo -e " OpenSSH     : 443, 80, 22 "
echo -e " Port UDP    : 1-65535 "
echo -e " Pub Key    :  $PUB "
echo -e " SSH WS      : 80,8080,8880,2086 "
echo -e " SSL/TLS     : 443 "
echo -e " OVPN UDP    : 2200 "
echo -e " Port 80     : $domain:80@$Login:$Pass "
echo -e " Port 443    : $domain:443@$Login:$Pass "
echo -e " Udp Custom  : $domain:1-65535@$Login:$Pass"
echo -e " OpenVpn     : https://$domain:81/ "
echo -e " Account     : https://$domain:81/ssh-$Login.txt "
echo -e " Payload WS  : GET / HTTP/1.1[crlf]Host: [host][crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]"
echo -e " Payload TLS : GET wss://$domain/ HTTP/1.1[crlf]Host: [host][crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]"
echo -e " Payload ENCD: HEAD / HTTP/1.1[crlf]Host: Masukan_Bug[crlf][crlf]PATCH / HTTP/1.1[crlf]Host: [host][crlf]Upgrade: websocket[crlf][crlf][split]HTTP/ 1[crlf][crlf]"
echo -e " Days in    : $masaaktif Day "
echo -e " Expiry in  : $expe "
