from uuid import uuid4
from app.services.db_service import container

def create_note(content: str):
    note = {
        "id": str(uuid4()),
        "content": content
    }
    container.create_item(note)
    return note

def get_notes():
    items = list(container.read_items())
    return items

def delete_note(note_id: str):
    container.delete_item(note_id, partition_key=note_id)