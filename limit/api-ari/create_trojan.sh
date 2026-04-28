#!/bin/bash
Login=$1
masaaktif=$2
iplimit=$3
Quota=$4
user="${Login}TR$(tr -dc 0-9 </dev/urandom | head -c3)"
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
    exit 1
  fi
}
checking_sc
ISP=$(cat /etc/xray/isp)
CITY=$(cat /etc/xray/city)
domain=$(cat /etc/xray/domain)
nama=$(cat /usr/bin/user)
uuid=$(cat /proc/sys/kernel/random/uuid)
clear
tgl=$(date -d "$masaaktif days" +"%d")
bln=$(date -d "$masaaktif days" +"%b")
thn=$(date -d "$masaaktif days" +"%Y")
expe="$tgl $bln, $thn"
tgl2=$(date +"%d")
bln2=$(date +"%b")
thn2=$(date +"%Y")
tnggl="$tgl2 $bln2, $thn2"
exp=`date -d "$masaaktif days" +"%Y-%m-%d"`
sed -i '/#trojanws$/a\#! '"$user $exp"'\
},{"password": "'""$uuid""'","email": "'""$user""'"' /etc/xray/config.json
sed -i '/#trojangrpc$/a\#! '"$user $exp"'\
},{"password": "'""$uuid""'","email": "'""$user""'"' /etc/xray/config.json

# Link Trojan Akun
systemctl restart xray
trojanlink1="trojan://${uuid}@bugkamu.com:443?mode=gun&security=tls&type=grpc&serviceName=trojan-grpc&sni=${domain}#${user}"
trojanlink="trojan://${uuid}@bugkamu.com:443?path=%2Ftrojan-ws&security=tls&host=${domain}&type=ws&sni=${domain}#${user}"
trojanlink2="trojan://${uuid}@bugkamu.com:80?path=%2Ftrojan-ws&security=none&host=${domain}&type=ws#${user}"

mkdir -p /detail/trojan/
#Simpan Detail Akun User
cat > /detail/trojan/$user.txt <<-END
-----------------------------------------
Xray/Trojan Account
-----------------------------------------
Remarks          : ${user}
Host/IP          : ${domain}
User Quota       : ${Quota} GB
User Ip          : ${iplimit} IP
Port             : 443,8443
Key              : ${uuid}
Path             : /trojan-ws/multi-path
ServiceName      : trojan-grpc
-----------------------------------------
Link TLS         : ${trojanlink}
-----------------------------------------
Link GRPC        : ${trojanlink1}
-----------------------------------------
Format OpenClash : https://${domain}:81/trojan-$user.txt
-----------------------------------------
Aktif Selama     : $masaaktif Hari
Dibuat Pada      : $tnggl
Berakhir Pada    : $expe
-----------------------------------------

END

cat >/var/www/html/trojan-$user.txt <<-END
-----------------------------------------
Format Open Clash
-----------------------------------------
- name: Trojan-$user-GO/WS
  server: ${domain}
  port: 443
  type: trojan
  password: ${uuid}
  network: ws
  sni: ${domain}
  skip-cert-verify: true
  udp: true
  ws-opts:
    path: /trojan-ws
    headers:
        Host: ${domain}

- name: Trojan-$user-gRPC
  type: trojan
  server: ${domain}
  port: 443
  password: ${uuid}
  udp: true
  sni: ${domain}
  skip-cert-verify: true
  network: grpc
  grpc-opts:
    grpc-service-name: trojan-grpc

-----------------------------------------
Link Akun Trojan 
-----------------------------------------
Link WS          : 
${trojanlink}
-----------------------------------------
Link GRPC        : 
${trojanlink1}
-----------------------------------------
Expired          : $expe
-----------------------------------------
END

CHATID="-1001911868043"
KEY="7876561487:AAHCpsZnu1LGx6w95fhqFMNSCT7fEGdv2vo"
export TIME="10"
export URL="https://api.telegram.org/bot$KEY/sendMessage"
sensor=$(echo "$user" | sed 's/\(.\{3\}\).*/\1xxx/')
ISP=$(curl -s ipinfo.io/org | cut -d " " -f 2-10 )
TEXT="
<b>-----------------------------------------</b>
<b>TRANSACTION SUCCESSFUL</b>
<b>-----------------------------------------</b>
<b>» Produk : Trojan</b>
<b>» ISP :</b> <code>${ISP}</code>
<b>» Limit Quota :</b> <code>${Quota} GB</code>
<b>» Limit Login :</b> <code>${iplimit} Hp</code>
<b>» Username :</b> <code>$sensor</code>
<b>» Duration :</b> <code>${masaaktif} Days</code>
<b>-----------------------------------------</b>
<i>Automatic Notification From Server</i>
<b>-----------------------------------------</b>"

curl -s --max-time $TIME -d "chat_id=$CHATID&disable_web_page_preview=1&text=$TEXT&parse_mode=html" $URL >/dev/null
clear


if [ ! -e /etc/trojan ]; then
  mkdir -p /etc/trojan
fi

if [[ $iplimit -gt 0 ]]; then
mkdir -p /etc/kyt/limit/trojan/ip
echo -e "$iplimit" > /etc/kyt/limit/trojan/ip/$user
else
echo > /dev/null
fi

if [ -z ${Quota} ]; then
  Quota="0"
fi

c=$(echo "${Quota}" | sed 's/[^0-9]*//g')
d=$((${c} * 1024 * 1024 * 1024))

if [[ ${c} != "0" ]]; then
  echo "${d}" >/etc/trojan/${user}
fi
DATADB=$(cat /etc/trojan/.trojan.db | grep "^#!" | grep -w "${user}" | awk '{print $2}')
if [[ "${DATADB}" != '' ]]; then
  sed -i "/\b${user}\b/d" /etc/trojan/.trojan.db
  echo "#! ${user} ${exp} ${uuid} ${Quota} ${iplimit}" >>/etc/trojan/.trojan.db
else
echo "#! ${user} ${exp} ${uuid} ${Quota} ${iplimit}" >>/etc/trojan/.trojan.db
fi
    systemctl restart xray > /dev/null 2>&1
clear
echo -e " TROJAN XRAY "
echo -e " Remark       : ${user}"
echo -e " Domain        : ${domain}"
echo -e " Limit Quota    : ${Quota} GB"
echo -e " Limit Ip       : ${iplimit}"
echo -e " Port TLS      : 400,8443"
echo -e " port WS       : 80,8880,8080,2082"
echo -e " Key           : ${uuid}"
echo -e " Localtions    : $CITY"
echo -e " ISP           : $ISP"
echo -e " AlterId       : 0"
echo -e " Security      : auto"
echo -e " Network       : ws"
echo -e " Path          : /trojan-ws"
echo -e " Dynamic Path  : yourbug/trojan-ws"
echo -e " ServiceName   : trojan-grpc"

echo -e " Link TLS      : ${trojanlink}"
echo -e " Link WS       : ${trojanlink2}"
echo -e " Link GRPC     : ${trojanlink1}"
echo -e " OpenClash     : https://${domain}:81/trojan-$user.txt"

echo -e " Days in    : $masaaktif Day "
echo -e " Expiry in  : $expe "