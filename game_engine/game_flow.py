from data.database import get_user_state, update_user_state
from ai.ai_response import generate_response

async def start_game(user_id: int, message):
    # Initialize game state for the user
    initial_state = {"step": 1, "progress": {}}
    await update_user_state(user_id, initial_state)
    await message.answer("Your journey as an environmental scientist begins now!"
                         "Напиши про себе, свою місію")

async def handle_choice(user_id: int, user_input: str):
    # Retrieve current game state
    user_state = await get_user_state(user_id)

    # Generate next step based on user choice
    response = await generate_response(user_input, user_state)
    await update_user_state(user_id, response["new_state"])

    return response["text"]
