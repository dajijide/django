from django.contrib import admin
from . import models
# Register your models here.


class NoteManager(admin.ModelAdmin):
    list_display = ['id','title','user']

from . import models
admin.site.register(models.Note,NoteManager)

