from django.contrib import admin
from .models import Divination


class DivinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'prediction',)
    list_display_links = ('id', 'prediction',)
    search_fields = ('id','name', 'prediction',)
    # list_editable = ('prediction',)


admin.site.register(Divination, DivinationAdmin)
