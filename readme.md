- CRUD Notes Rest API

see in action : https://drf-notes-api.herokuapp.com/

- Note Object : {
    "note_id" : Primay Key,
    "title" : String,
    "content" : String,
    "created_at" : Date (YYYY-MM-DD)
}

- API Endpoints :
    1) [GET]/note-list/ : Returns all the notes in the database.
    2) [POST]/note-create/ : Creates a note with the json object in body param.
    3) [GET]/note-detail/<str:pk>/ : Return the note with the specified note_id (pk).
    4) [PATCH]/note-update/<str:pk>/ : Update the note with the specified fields in the body param.
    5) [DELETE]/note-delete/<str:pk>/ : Delete the note with the specified note_id (pk).


- NOTE : this api is for test purposes only, it was created to learn frontend developpment and integrate api's into frontend apps !