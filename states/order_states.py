from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    DEFAULT = State()
    ADD_ORDER = State()
