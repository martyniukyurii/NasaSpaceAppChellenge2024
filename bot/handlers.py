from aiogram import types
from aiogram.dispatcher import Dispatcher
from game_engine.game_flow import start_game, handle_choice
from ai.ai_image import generate_image

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def handle_start(message: types.Message):
        # Start game for the user
        await message.answer("Welcome to EcoQuest: Рятуй Планету!")
        await start_game(message.from_user.id, message)

    @dp.message_handler()
    async def handle_message(message: types.Message):
        # Process user input
        response = await handle_choice(message.from_user.id, message.text)
        await message.answer(response)

        # Generate AI image (optional, based on game events)
        image_url = await generate_image(response)
        if image_url:
            await message.answer_photo(image_url)
