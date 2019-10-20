from django.shortcuts import render, redirect
from django.db.models import Max

from .models import Puzzle, Entry, Clue

import random

def get_random_clue():
    max_id = Clue.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return Clue.objects.get(pk=pk)

# VIEWS
def redirect_view(request):
    response = redirect('/xword-drill/')
    return response

def drill(request):
    random_clue = get_random_clue()
    context = {'random_clue': random_clue}
    return render(request, 'xword/drill.html', context)

def answer(request):
    return render(request, 'xword/answer.html')
