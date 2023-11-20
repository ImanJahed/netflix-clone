from django.contrib import admin

from core.models import Movie, Genre, ListMovie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'length']


admin.site.register(Genre)
admin.site.register(ListMovie)
