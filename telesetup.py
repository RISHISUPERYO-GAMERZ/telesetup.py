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

                $ZZZ$
               Z8D8D8Z
              Z××ND××8
             DD××NN××ND
             DMMZ~MDN=DO
            O8NMZNDDD8NO
            8NMN~+=NDD8D8
          ZZZOD8OO88Z$ZZZ$D8
         ZZ$$$ONOO$OZZ$OOZDDN
        OOZZOZOZ7~~,=7O$88DD8
        8OOO8O$.=$7I$I,$D8N88O
       88OO88O=IZ$Z∆$ZI,O8N8OON
      D88DDDDZ~7O=Z∆Z$+~ZMNDDDD
      8OO88D8O+=Z++$?,I~8NMNNDMM
     8$O88DD88Z?:7$?7~:O8DMDND
     NOOOZO8OOO8Z7++IO88O77MNNM8
      8DMO7OOO8O88ODODD8O$$
         8Z88888O8O88DD8O8N
         D8D88DOO$ZZO8OONN
         D8DNDNNOO$O88DNNN
         N88NNMNDZ8ODNNNNND
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
