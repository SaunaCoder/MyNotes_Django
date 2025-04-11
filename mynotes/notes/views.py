from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .views import *
# Create your views here.

@login_required
def home(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'home.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid:
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('home',)
    else:
        form = NoteForm()
    return render(request, 'createnote.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')
