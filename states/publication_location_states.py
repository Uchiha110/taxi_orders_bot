from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    DEFAULT = State()
    PUBLICATION_LOCATION = State()
