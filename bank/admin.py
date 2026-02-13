from django.contrib import admin
from .models import Card
from import_export.admin import ImportExportMixin

# Register your models here.
@admin.register(Card)
class CardAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','card_number')
    search_fields = ['card_number']
