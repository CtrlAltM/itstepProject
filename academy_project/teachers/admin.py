from django.contrib import admin
from .models import Note, Member, Task

admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Note)