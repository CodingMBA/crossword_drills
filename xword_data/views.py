from django.shortcuts import render

from .models import Puzzle, Entry, Clue


def drill(request):
    return render(request, 'xword/drill.html')
