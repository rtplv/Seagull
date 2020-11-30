from django.contrib import admin

# Register your models here.
from gui.models import ProgramGroup, Program


@admin.register(ProgramGroup)
class ProgramGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = 'name',
    search_fields = 'name',

    pass
