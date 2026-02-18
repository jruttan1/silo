from fastapi import FastAPI, BaseModel

app = FastAPI()

class Capture(BaseModel):
    id: int | None = None
    content: str

captures = []

@app.post('/capture')
def add_capture(content) -> dict:
    new_capture = {
        id: len(captures) + 1,
        content: content
        }
    captures.append(new_capture)
    return new_capture

@app.get('/captures')
def get_all_captures():
    return captures

@app.get('/captures/{id}')
def get_capture_from_id(id: int):
    for capture in captures:
        if capture.id == id:
            return capture
    return {"Error, Not Found"}, 404

