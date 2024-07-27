import asyncio

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.config import bot, admin
from states.order_states import Form

chats_id = [-4238739734, -4245221962, -4142811799, -4274863240, -4235633691]


async def add_order_command(dp):
    @dp.message(Command(commands="add_order"))
    async def add_order(message: types.Message, state: FSMContext) -> None:
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = "Enter message for all chat.\nIf you want cancel this process - press Cancel"

            button_cancel = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Cancel", callback_data="cancel_add_order")],
            ])

            await message.answer(msg, reply_markup=button_cancel)
            await state.set_state(Form.ADD_ORDER)

    @dp.message(Form.ADD_ORDER)
    async def add_order(message: types.Message, state: FSMContext) -> None:
        user_msg = message.text
        msg = "Message successfully send!"

        await message.answer(msg)

        for chat_id in chats_id:
            await bot.send_message(chat_id=chat_id, text=f"{user_msg}")
        await state.set_state(Form.DEFAULT)

    @dp.callback_query(Form.ADD_ORDER, F.data == "cancel_add_order")
    async def add_order(callback: types.CallbackQuery, state: FSMContext) -> None:
        msg = "Send message to cancel"

        await callback.message.answer(msg)

        await state.set_state(Form.DEFAULT)

