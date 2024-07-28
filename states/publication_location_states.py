from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    DEFAULT = State()
    ADD_PUBLICATION_LOCATION = State()
    DEL_PUBLICATION_LOCATION = State()
