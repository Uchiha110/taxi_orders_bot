from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.config import admin
from database import get_name_table, actions_table
from states.publication_location_states import Form


async def del_publication_location_command(dp):
    @dp.message(Command(commands="del_publication_location"))
    async def del_publication_location(message: types.Message, state: FSMContext) -> None:
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = "Enter the ID of the chat you want to connect to\nIf you want cancel this process - press Cancel"

            button_cancel = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Cancel", callback_data="cancel_add_order")],
            ])

            await state.set_state(Form.DEL_PUBLICATION_LOCATION)
            await message.answer(msg, reply_markup=button_cancel)

    @dp.message(Form.DEL_PUBLICATION_LOCATION)
    async def add_publication_location(message: types.Message, state: FSMContext) -> None:
        user_msg = message.text
        msg1 = "The chat has been successfully deleted!"
        msg2 = ('The chat ID must start with the character: "-"\n'
                'Re-enter the command and try again\n'
                'If anything, here it is: /del_publication_location')
        msg3 = ('This chat is not linked\n'
                'Re-enter the command and try again\n'
                'If anything, here it is: /add_publication_location')
        chats_id = await get_name_table()

        if user_msg[0] == "-":
            if user_msg in chats_id:
                await actions_table(actions="delete", name=int(user_msg))
                await state.set_state(Form.DEFAULT)
                await message.answer(msg1)
            else:
                await state.set_state(Form.DEFAULT)
                await message.answer(msg3)
        else:
            await state.set_state(Form.DEFAULT)
            await message.answer(msg2)

    @dp.callback_query(Form.ADD_PUBLICATION_LOCATION, F.data == "cancel_add_order")
    async def add_publication_location(callback: types.CallbackQuery, state: FSMContext) -> None:
        msg = "Deleted a chat has been canceled"

        await state.set_state(Form.DEFAULT)
        await callback.message.answer(msg)
