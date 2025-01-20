from django.urls import path
from .views import NewNote, NoteUpdate, NoteDelete

urlpatterns = [
    path("ajouter/", NewNote.as_view(), name="note_new"),
    path("<int:pk>/modifier/", NoteUpdate.as_view(), name="note_update"),
    path("<int:pk>/supprimer/", NoteDelete.as_view(), name="note_delete"),
]
