from django.shortcuts import render, redirect

from .models import Puzzle, Entry, Clue

def redirect_view(request):
    response = redirect('/xword-drill/')
    return response

def drill(request):
    return render(request, 'xword/drill.html')

def answer(request):
    return render(request, 'xword/answer.html')
