from django.contrib import admin
from .models import Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_id', 'title', 'content', 'created_at')


admin.site.register(Note, NoteAdmin)
