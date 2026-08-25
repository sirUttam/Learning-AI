from google import genai

from pydantic import BaseModel
from dotenv import load_dotenv
import numpy as np 

load_dotenv()

client = genai.Client()

texts = [
    "My house needs repair.",
    "I love motorbike sound",
    "The sound of bike makes me smile",
    
]


result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
)

embeddings = [e.values for e in result.embeddings]

a = np.array(embeddings[0])
b = np.array(embeddings[1])
c = np.array(embeddings[2])

dot_ab = np.dot(a,b)
dot_ac = np.dot(a,c)
dot_bc = np.dot(b,c)



magnitude_a = np.linalg.norm(a)
magnitude_b = np.linalg.norm(b)
magnitude_c = np.linalg.norm(c)


similarity_ab = dot_ab/(magnitude_a * magnitude_b)

similarity_ac = dot_ac/(magnitude_a * magnitude_c)

similarity_bc = dot_bc/(magnitude_b * magnitude_c)

# cosO = (a.b)/|a||b|

print("similarity_ab",similarity_ab)
print("similarity_ac",similarity_ac)
print("similarity_bc",similarity_bc)



# print((result.embeddings[:5]))

# print(result.embeddings)
# print("---------------------------------")
# print(result)
# print("---------------------------------")
# print(type(result))
# print(result.embeddings[:10])
# print("---------------------------------")
# print(len(result.embeddings))
# print(result.embeddings[1].values)
