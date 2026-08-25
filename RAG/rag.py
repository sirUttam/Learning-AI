with open("knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

# print(text)

words = text.split()

# print(type(words))
# print(words)

print("--------------------------------")

# print(words[0:20])

chunk_size = 20
chunks = []

for start in range(0, len(words), chunk_size):
    chunk = words[start:(start+chunk_size)]
    chunks.append(chunk)

print("--------------------------------")


# print(chunks)

print("--------------------------------")

# print(len(chunks))
print("--------------------------------")


# print(chunks[0])
print("--------------------------------")


# Now joining those chunks into a single text

text_chunks = []

for chunk in chunks:
    text_chunk = " ".join(chunk)
    text_chunks.append(text_chunk)

# print(text_chunks)

print("--------------------------------")

# print(len(text_chunks))


# Now converting those text chunks into vector embeddings

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text_chunks
)

print("--------------------------------")

# print(result)

# print("--------------------------------")
# print("--------------------------------")

# print(result.embeddings)
# print("--------------------------------")
# print("--------------------------------")

# print(result.embeddings[0])
# print("--------------------------------")

# Now we need to arrange these text chunks with their respective embeddings
# For this we will use the zip function to combine the text chunks and their respective embeddings

records = []

for text_chunk, embedding in zip(text_chunks, result.embeddings):
    record = {
        "text": text_chunk,
        "embedding": embedding.values
    }
    records.append(record)

# print(records)
print(type(records))
print(records[1])

print(f"Total number of records {len(records)}")


# Now lets talk about the query embeddings 
#------------------------------------------------------------------------------------------------

query= "How does python handles errors?"

query_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)


print("------------Query embeddings--------------------")

query_embedding = query_result.embeddings[0].values

print(query_embedding)
print("--------------Length of query embedding------------------")
print(len(query_embedding))

print("--------------------------------")
import numpy as np

query_vector = np.array(query_embedding)

# Now trying to find the similarity between the query vector and the chunk embeddings stored ones
# using cosine similarity for this 

search_results = []

for record in records:
    document_vector = np.array(record['embedding'])

    dot = np.dot(query_vector, document_vector)

    magnitude_query = np.linalg.norm(query_vector)
    magnitude_document = np.linalg.norm(document_vector)

    similarity = dot / (magnitude_query * magnitude_document)

    search_results.append({
        "text": record["text"],
        "similarity": similarity
    })

print("-------------------------Similarity-----------------------------")
print(search_results)

# Now we need to sort this search results based on similarity scores
# For this we will use the sorted function 

sorted_results = sorted(
    search_results,
    key=lambda result: result['similarity'],
    reverse=True
)

print("-------------------------Sorted results-----------------------------")

print(sorted_results)