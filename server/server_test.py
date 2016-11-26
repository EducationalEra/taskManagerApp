import requests
from server import NoteList 
def test_add_notes():
    note_list = NoteList()
    note_list.add_note("new note")
    assert note_list.get_notes() == ["new note"]

def test_add_several_notes():
    note_list = NoteList()
    note_list.add_note("new note")
    note_list.add_note("other note")
    assert note_list.get_notes() == ["new note", "other note"]
  
