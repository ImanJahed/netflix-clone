from core.models import Genre


def genre(request):
    genres = Genre.objects.all()
    return {
        'genres': genres
    }