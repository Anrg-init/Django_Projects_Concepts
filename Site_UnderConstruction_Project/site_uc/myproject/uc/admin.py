from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UnderContstruction)
class underconstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'uc_note', 'uc_duration', 'is_uc')
    fields = ('uc_note', 'uc_duration', 'is_uc') 