from django.contrib import admin

from .models import Puzzle, Entry, Clue

admin.site.site_header = "Xword Admin"
admin.site.site_title = "Xword Admin Area"
admin.site.index_title = "Welcome to the Xword admin area!"

admin.site.register(Puzzle)
admin.site.register(Entry)
admin.site.register(Clue)
