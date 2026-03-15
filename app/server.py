from fastapi import FastAPI, BaseModel
from db import Note

app = FastAPI()

notes = Note()

@app.post('/notes')
def add_Note(note: Note) -> Note:
    new_note = Note(id = len(notes) + 1, content = note.content)
    notes.append(new_note)
    return new_note

@app.get('/notes')
def get_all_notes():
    return notes

@app.get('/notes/{id}')
def get_Note_from_id(id: int):
    for Note in notes:
        if Note.id == id:
            return Note
    return {"Error, Not Found"}, 404

@app.post('/note/{id}')
def update_content(content: str, id: int):
    for note in notes:
        if note.id == id:
            note.content = content
            return {"Success:" "Updated Content for Note"}, 200
        
    return {"Failed to Update"}, 404
