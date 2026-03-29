from openai import OpenAI
client = OpenAI()
from schemas import NoteCreate

def create_embedding(note: NoteCreate):
    text = {'title': note.title,
            'content': note.content}
    response = client.embeddings.create(
        input = str(text),
        model = "text-embedding-3-small"
    )
    embedding = response.data[0].embedding # unpack response object
    return embedding