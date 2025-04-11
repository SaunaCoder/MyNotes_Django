from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create note', create_note, name='create note'),
    path('delete/<int:note_id>', delete_note, name='delete note')
]
