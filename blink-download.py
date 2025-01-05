import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from datetime import datetime, timedelta

USER = ""
PASS = ""
OUTDIR = ""
CAMERA_NAME = ""

async def start():
    blink = Blink(session=ClientSession())
    auth = Auth({"username": USER, "password": PASS})
    blink.auth = auth
    await blink.start()
    await blink.download_videos(OUTDIR, camera=CAMERA_NAME, since="2025/01/01 00:00", stop=100, delay=2)
    print("Video downloaded")
    return blink

blink = asyncio.run(start())

#for name, camera in blink.cameras.items():
    #  print(name)
    #  print(camera.attributes) 