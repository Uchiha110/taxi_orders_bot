from aiogram import types
from aiogram.filters.command import Command

from config.config import admin


async def default_commands(dp):
    @dp.message(Command(commands="start"))
    async def command_start(message: types.Message):
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = ("This bot was custom-made, "
                   "but the customer and I did not agree on the price, "
                   "so it is now on my GitHub.\n"
                   "If you want to learn more about the capabilities of the bot, "
                   "write the command /help")

            await message.answer(msg)

    @dp.message(Command(commands="help"))
    async def command_help(message: types.Message):
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = ("/start - this is the most useless team of all, just the beginning.\n"
                   "/help - this is a list with all the commands that the bot can execute.\n"
                   "/add_order - sending a message to linked chats, as well as writing to the database.\n"
                   "/del_order - deleting a message from linked chats, as well as deleting it from the database.\n"
                   "/add_publication_location - this is to link the chat to the bot.\n"
                   "/del_publication_location - this is to unlink the chat from the bot\n")

            await message.answer(msg)
