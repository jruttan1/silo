from fastapi import FastAPI, BaseModel

app = FastAPI()

class Capture(BaseModel):
    id: int | None = None
    content: str

captures = []

@app.post('/capture')
def add_capture(capture: Capture) -> Capture:
    new_capture = Capture(id = len(captures) + 1, content = capture.content)
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

@app.post('/capture/{id}')
def update_content(content: str, id: int):
    for capture in captures:
        if capture.id == id:
            capture.content = content
            return {"Success:" "Updated Content for Capture"}, 200
        
    return {"Failed to Update"}, 404
