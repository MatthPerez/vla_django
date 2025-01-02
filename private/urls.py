from django.urls import path
from .views import PrivateView

urlpatterns = [
    path("", PrivateView.as_view(), name="private"),
    # path("note/", NewNote.as_view(), name="note_new"),
    # path("note/<int:pk>/modifier", NoteUpdate.as_view(), name="note_update"),
    # path("note/<int:pk>/supprimer", NoteDelete.as_view(), name="note_delete"),
]
