from google import genai
from dotenv import load_dotenv

from pydantic import BaseModel, Field

load_dotenv()


class Order(BaseModel):
    intent: str
    order_id: str
    reason: str


client = genai.Client()

prompt = "I want to return the order 24512 because i received it completely damaged"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Order.model_json_schema()
    }
)

response = Order.model_validate_json(interaction.output_text)


# response = interaction.output_text
print(response)