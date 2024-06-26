import sys
import time
import uvloop
import colorama
from pyrogram import Client
from telegraph.aio import Telegraph
from TGNowPlaying.settings import settings
from asyncio import get_event_loop, new_event_loop, set_event_loop
from TGNowPlaying.logging import LOGGER

uvloop.install()
LOGGER(__name__).info("Starting TGNowPlaying....")
BotStartTime = time.time()


if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    LOGGER(__name__).critical(
        """
=============================================================
You MUST be on python 3.7 or above, shutting down the bot...
=============================================================
"""
    )
    sys.exit(1)

LOGGER(__name__).info("setting up event loop....")
try:
    loop = get_event_loop()
except RuntimeError:
    set_event_loop(new_event_loop())
    loop = get_event_loop()

colorama.init()

LOGGER(__name__).info( colorama.Fore.CYAN +
    r""" 
    ______ _____ _  __              ___   __             _           
/_  __// ___// |/ /___  _    __ / _ \ / /___ _ __ __ (_)___  ___ _
 / /  / (_ //    // _ \| |/|/ // ___// // _ `// // // // _ \/ _ `/
/_/   \___//_/|_/ \___/|__,__//_/   /_/ \_,_/ \_, //_//_//_/\_, / 
                                             /___/         /___/  
""" + colorama.Style.RESET_ALL)


LOGGER(__name__).info( "creating telegraph session....")
telegraph = Telegraph(domain="graph.org")

LOGGER(__name__).info("initiating the client....")
plugins = dict(root="TGNowPlaying/plugins") 

bot = Client(
    "TGNowPlaying",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    plugins=plugins,
)

