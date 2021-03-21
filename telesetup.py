#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

try:
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
except BaseException:
    print("Telethon Not Found. Installing Now.")
    import os

    os.system("pip3 install telethon")
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
ok = """ ____  ____    __   __   _  _
Lets rock😎
DDDDO$$$Z$ZZZ77III??III77777Z?Z+OZ8$IO77
DDD8Z$$77$Z77II?+?II7III7$77ZIO+~$8O7DNN
D888OOZZZ$$I???+++++I7II7$$?Z=Z+O7887DDN
8ZZ$ZOZOZ77IIII++++++II7$I=~.+,+:,.=:8=~
OZ$7777$$777II?+7ZZZ$??I.$NDZ?8ZI=OO$DD$
88Z$$$$ZZZ7$7IIO8DDD8Z...++??+887~IOZ$I8
O8OZ$$$$ZZ=.?.ZDNNNNN8?..77+I?$ZO~Z87N8D
O8OOZZZZ$I+=,ZDDNNNNNND:.=IZ7I$O8=I87DZ8
Z8OZZZ$O?:$7$NMM8+MDN?N8~?8=ZZZ7D+.8~8+?
OOOZZ7$$I~I+O8NMZNDDDONO.7O8$$7OD+O8OD+Z
8$7Z$??$I~??=DNMN~~~NDD8D87777$DD=$IZDD8
8II+,=+I?~ZZZ88O8OD8O$ZZZ$D8=Z7O8+8I+DOI
D$$O7,77?ZZ$$$ZMZ8ZOZZ$ZZZ8DNO8O??888DD7
MMMNN8ZZZOZZ8ZOO7~~.~7OZ88DDDMNNNNNMMMMM
88ZOI7?I8OOO8O$.=$7I$?,$D8ND8O7Z?+O$88OO
88OZ$II88OO8DO=?Z$Z8$ZI,ODN8OOOZZ+$OOD8D
8ZZZ$7O888DD8Z~7O=Z8$$+~ZMNDDDD$O+OD8N8D
DOZ$ZO8ZO88DDO+=Z++7?:I=8N7NNDNNI+~D88$8
8OZ$7Z$O88DDD8O?:7$+I~~O8D$DNDMMD+OD8NDD
8O88ZO8OOOOOO888ZI?+IO88O777NNM8D?8+DNDN
D8Z$ZZO8$OIOOO8888ODODD8OZ$7IZ$DDID8DN8D
8ZZOOZ$$78O88OD8O8O88DD8O8NZ:$78OODDDN8D
8ZO?$7O$ID8D88DOO$ZZOOOONNM+$++$Z8DIDN8D
88$:+$+~ID8DNDNNO8$O88DNNNM7OO?~I8~III8+
Z.~?=Z,,7ND8NNMN8ODODNNNMND7DDIO8DD7I+O=
"""
print(ok)
APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")

client = TelegramClient(StringSession(), APP_ID, API_HASH)
with client:
    session_str = client.session.save()
    client.send_message("me", f"{session_str}")
    client.send_message(
        "Yeh Raha tera telegram ka string, \nJoin @Rishisuperyogamerzin For More Support."
    )
    print("⬆ Ok bhai abh apna saved msg dekh😑.")
    print("Op Bolte✅⚡😎")
#I am pro
#Yoooo
#Opppppppp
