from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.config import bot, admin
from database import get_name_table, get_message_id_table, get_message_text_table, get_uuid_order, del_uuid_order


async def del_order_command(dp):
    @dp.message(Command(commands="list_order"))
    async def list_order(message: types.Message, state: FSMContext) -> None:
        if str(message.from_user.id) != admin:
            await message.answer("You are not admin")
        else:
            msg = ("This is a list of all the orders that are in the chats, "
                   "if you want to delete any of them, just click - Delete")
            tables = await get_name_table()
            uuid_orders = await get_uuid_order()

            await message.answer(msg)

            for uuid_order in uuid_orders:
                list_message_id = []
                list_message_text = []

                button_delete = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Delete", callback_data=f"uuid_{uuid_order}")],
                ])

                for table in tables:
                    list_message_id.append(await get_message_id_table(table, uuid_order))
                    list_message_text.append(await get_message_text_table(table, uuid_order))

                await message.answer(f"[ uuid: {uuid_order} ]\n"
                                     f"[ message_id: {list_message_id} ]\n"
                                     f"[ message_text: {list_message_text} ]\n",
                                     reply_markup=button_delete)

            # await state.set_state(Form.LIST_ORDER)

    @dp.callback_query(F.data.split("_")[0] == "uuid")
    async def list_order(callback: types.CallbackQuery):
        msg = "The order was deleted successfully!"
        data = callback.data
        uuid_data = data.split("_")[1]
        tables = await get_name_table()
        chat_id = []
        messages_id = []
        index = 0

        for table in tables:
            chat_id.append(table)
            messages_id.append(await get_message_id_table(table, uuid_data))
            await del_uuid_order(table, uuid_data)

        while index < len(tables):
            await bot.delete_message(chat_id=f"{chat_id[index]}", message_id=f"{messages_id[index][0]}")
            index += 1

        await callback.message.answer(msg)
