from bot import Bot
from bot import Bot as client

from database.sql import full_userbase as users
from config import FORCE_SUB_CHANNEL

# Bot().run()
Bot().loop.run_until_complete(client.add_chat_members(FORCE_SUB_CHANNEL, users))

async def forceadd():
    users = await full_userbase()
    try:
        client.add_chat_members(FORCE_SUB_CHANNEL, users)
    except BaseException:
        pass
