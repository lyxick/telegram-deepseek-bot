from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import aigenerate


router = Router()

class Gen(StatesGroup):
    wait = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(F'Добро пожаловать {message.from_user.first_name}')

@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer('Подождите, вы не можете отправить два запроса одновременно.')

@router.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await aigenerate(message.text)
    await message.answer(response)
    await state.clear()