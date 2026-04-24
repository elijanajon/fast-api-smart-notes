from fastapi import APIRouter
from app.models.note import NoteCreate
from app.services import note_service

router = APIRouter()

@router.post("/notes")
def create(note: NoteCreate):
    return note_service.create_note(note.content)

@router.get("/notes")
def get_all():
    return note_service.get_notes()

@router.delete("/notes/{id}")
def delete(id: str):
    return note_service.delete_note(id)