from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from config.config import admin


async def del_publication_location_command(dp):
    @dp.message(Command(commands="del_publication_location"))
    async def del_publication_location(message: types.Message, state: FSMContext) -> None:
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            pass
