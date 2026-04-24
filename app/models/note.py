from pydantic import BaseModel

class NoteCreate(BaseModel):
    content: str

class Note(NoteCreate):
    id:str
    