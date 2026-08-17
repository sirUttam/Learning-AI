from google import genai
from dotenv import load_dotenv

from schema import Person

load_dotenv()

client = genai.Client()

prompt = "John is 25 years old and lives in Kathmandu."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Person.model_json_schema()
    }
)

response = Person.model_validate_json(interaction.output_text)

# print(type(interaction))
# print("--------------------------------")
# print(interaction)
# print("--------------------------------")
# print(interaction.output_text)
print(response)

# print(type(response))

# print(isinstance(response, Person))

# print(response.name)
# print(response.age)
# print(response.city)
# print(response.email)

print(response.model_dump())

print(response.model_dump_json())