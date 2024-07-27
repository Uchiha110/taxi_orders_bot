from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.config import admin
from database import create_table
from states.publication_location_states import Form


async def add_publication_location_command(dp):
    @dp.message(Command(commands="add_publication_location"))
    async def add_publication_location(message: types.Message, state: FSMContext) -> None:
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = "Enter the ID of the chat you want to connect to\nIf you want cancel this process - press Cancel"

            button_cancel = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Cancel", callback_data="cancel_add_order")],
            ])

            await message.answer(msg, reply_markup=button_cancel)
            await state.set_state(Form.PUBLICATION_LOCATION)

    @dp.message(Form.PUBLICATION_LOCATION)
    async def add_publication_location(message: types.Message, state: FSMContext) -> None:
        user_msg = message.text
        msg = "The chat has been successfully added!"

        await message.answer(msg)

        await create_table(int(user_msg))
        await state.set_state(Form.DEFAULT)

    @dp.callback_query(Form.PUBLICATION_LOCATION, F.data == "cancel_add_order")
    async def add_publication_location(callback: types.CallbackQuery, state: FSMContext) -> None:
        msg = "Adding a chat has been canceled"

        await callback.message.answer(msg)

        await state.set_state(Form.DEFAULT)

