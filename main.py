from bot import Bot

from database.sql import full_userbase
from config import FORCE_SUB_CHANNEL

# Bot().run()
Bot().run_until_complete(forceadd())

async def forceadd():
	users = await full_userbase()
  try:
      await Bot().add_chat_members(chat_id=FORCE_SUB_CHANNEL, users)
  except BaseException:
     pass
      