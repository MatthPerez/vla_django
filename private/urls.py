from django.urls import path
from .views import PrivateView

urlpatterns = [
    path("ma_page/", PrivateView.as_view(), name="private"),
    # path("ma_page/note/", NewNote.as_view(), name="note_new"),
    # path("ma_page/note/<int:pk>/modifier", NoteUpdate.as_view(), name="note_update"),
    # path("ma_page/note/<int:pk>/supprimer", NoteDelete.as_view(), name="note_delete"),
]
