import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from config.config import bot
from handlers.add_order import add_order_command
from handlers.del_order import del_order_command
from handlers.add_publication_location import add_publication_location_command
from handlers.del_publication_location import del_publication_location_command

load_dotenv()

# Тут код


storage = MemoryStorage()


async def main() -> None:
    dp = Dispatcher(storage=storage)

    await add_order_command(dp)
    await del_order_command(dp)
    await add_publication_location_command(dp)
    await del_publication_location_command(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
