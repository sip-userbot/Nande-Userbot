## Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



NANDE="\n°Nande Userbot Install•"
NANDE+="\n "
NANDE+="\nMenjalankan Nande Userbot di Termux"
NANDE+="\n⚡ Sebelumnya Joinn Grup/Channel ⚡"
NANDE+="\n "
NANDE+="\n📣 Channel: @suportNande"
NANDE+="\n📢 GrupSupport: @NandeSupport"
NANDE+="\n "
LUQ="\n "
echo -e $NANDE
echo -e $LUQ
echo "Waiting..."
echo -e $LUQ
pkg update -y && pkg upgrade
clear
echo -e $NANDE
echo -e $LUQ
echo "Menginstal python3"
echo -e $LUQ
pkg install python3
pkg install screen
pip3 install --upgrade pip
apt install postgresql
apt install neofetch
apt install ffmpeg
apt install curl
apt install megatools
apt install unzip
apt install wget
apt install liblapack-dev
apt install aria2
apt install zip
apt install sudo
apt install python3-wand
apt install postgresql-client
cle
echo -e $NANDE
echo -e $LUQ
echo "⚙️ Github Installer"
echo -e $LUQ
pkg install git -y
rm -rf Nande-Userbot
clear
echo -e $NANDE
echo -e $LUQ
echo "Cloning Panda Userbot"
echo -e $LUQ
git clone https://github.com/sip-userbot/Nande-Userbot
clear
echo -e $NANDE
echo -e $LUQ
echo "Menginstall Pakages"
echo -e $LUQ
cd PandaX_Userbot
pip3 install -U -r requirements.txt
python3 installer/termux.py
screen -S Nande-Userbot
bash start.sh
