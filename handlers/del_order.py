from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from config.config import admin
from states.order_states import Form


async def del_order_command(dp):
    @dp.message(Command(commands="del_order"))
    async def del_order(message: types.Message, state: FSMContext) -> None:
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = ""
            await state.set_state(Form.DEL_ORDER)
