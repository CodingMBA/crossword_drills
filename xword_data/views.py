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

    if request.method == 'GET':
        context = {}
        context['random_clue'] = get_random_clue()
        return render(request, 'xword/drill.html', context)
    elif request.method == 'POST':
        context = {'incorrect': False}
        random_clue_id = request.POST.get('random_clue_id')
        guess = request.POST.get('guess').upper()
        context['guess'] = guess

        random_clue = Clue.objects.get(pk=random_clue_id)
        context['random_clue'] = random_clue

        if guess == random_clue.entry.entry_text:
            return redirect('answer', random_clue_id)
        else:
            context['incorrect'] = True
            return render(request, 'xword/drill.html', context)

def answer(request, random_clue_id):
    random_clue = Clue.objects.get(pk=random_clue_id)
    matches = Entry.objects.filter(clue__clue_text=random_clue.clue_text)
    match_count = matches.count()
    context = {
        'random_clue': random_clue,
        'match_count': match_count        
    }
    return render(request, 'xword/answer.html', context)
