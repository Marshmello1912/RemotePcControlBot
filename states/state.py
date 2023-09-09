from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    menu = State()
    System = State()
    Steam = State()
    Browser = State()
