import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.0.5"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
SESSION = os.getenv("SESSION", None)
GROUP_MODE = os.getenv("GROUP_MODE", "True")
START_VID = os.getenv("START_VID", None)


def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list


sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [5576613955, 5348628701]
for x in DEVS:
    SUDO_USERS.append(x)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "5576613955, 5348628701").split())))
#----------------------------------------------

vcbot = Client(
    'Tech-Quard',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'Tech-Quard.Plugin'},
)

HELP_DICT = dict()
hl = HNDLR[0]
start_time = time.time()


if GROUP_MODE == ("True" or "true" or "TRUE"):
    grp = True
else:
    grp = False


#-------------------------CLIENTS-----------------------------
if SESSION:
    sumit = Client(SESSION, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'Tech-Quard.vc'})
    call_py = PyTgCalls(TechQuard)
else:
    sumit = None
    call_py = None
