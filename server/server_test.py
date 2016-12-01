from server import Database
def test_add_notes():
    note_list = Database()
    note_list.add_note("new note")
    assert note_list.get_notes() == [{"note": "new note", "id": 1}]

def test_add_several_notes():
    note_list = Database()
    note_list.add_note("new note")
    note_list.add_note("other note")
    assert note_list.get_notes() == [[{"note": "new note", "id": 1}], [{"note": "other note", "id": 2}]]
  
