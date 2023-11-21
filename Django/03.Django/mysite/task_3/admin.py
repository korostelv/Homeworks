from django.contrib import admin
from .models import Poem, Author, Theme


class PoemAdmin(admin.ModelAdmin):
    list_display = ('id','name','author','theme')
    list_display_links = ('id','name', 'author', 'theme')
    search_fields = ('id','name', 'author', 'theme')
    list_filter = ('author', 'theme')

admin.site.register(Poem, PoemAdmin)
admin.site.register(Author)
admin.site.register(Theme)