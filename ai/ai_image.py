import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_image(event_description: str):
    # Generate image based on description of the event
    client = openai.OpenAI()
    response = client.images.generate(
        model="dall-e-2",
        prompt=event_description,
        n=1,
        size="512x512"
    )

    return response.data[0].url
