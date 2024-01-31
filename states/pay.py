from aiogram.dispatcher.filters.state import State, StatesGroup

class PayState(StatesGroup):
    firstState = State()

class PayCheck(StatesGroup):
    getState = State()
    sendState = State()