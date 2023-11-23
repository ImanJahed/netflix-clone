import re

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages

from .forms import LoginForm, SignUpForm
from .models import Movie, ListMovie


# Create your views here.

@login_required(login_url='login_user')
def home(request):
    movies = Movie.objects.all()
    cover = [obj for obj in movies][-1]

    context = {
        'movies': movies,
        'cover': cover
    }

    return render(request, 'core/home.html', context)


@login_required(login_url='login_user')
def movie(request, pk):
    movie_details = get_object_or_404(Movie, movie_id=pk)
    context = {
        'movie_details': movie_details
    }
    return render(request, 'core/movie.html', context)


@login_required(login_url='login_user')
def my_list(request):
    movies = ListMovie.objects.filter(user=request.user)
    print(movies)
    context = {
        'movies': movies
    }
    return render(request, 'core/movie_list.html', context)


@login_required(login_url='login_user')
def add_to_list(request):
    if request.method == 'POST':
        movie_url_id = request.POST.get('movie_id')
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None
        get_movie = get_object_or_404(Movie, movie_id=movie_id)
        movie_list, created = ListMovie.objects.get_or_create(movie=get_movie, user=request.user)
        if created:
            response_data = {'status': 'success', 'message': 'Added ✓'}

        else:
            response_data = {'status': 'info', 'message': 'Movie already in list'}

        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'messages': 'Invalid request'}, status=400)


@login_required(login_url='login_user')
def film_list(request):
    films = Movie.objects.filter(type_movie='Film')
    cover = [obj for obj in films][-1]

    context = {
        'films': films,
        'cover': cover
    }
    return render(request, 'core/film_list.html', context)


@login_required(login_url='login_user')
def series_list(request):
    series = Movie.objects.filter(type_movie='Series')
    cover = [obj for obj in series][-1]

    context = {
        'series': series,
        'cover': cover
    }
    return render(request, 'core/series.html', context)


@login_required(login_url='login_user')
def search(request):
    q = request.GET.get('q', None)
    movie_search = Movie.objects.filter(title__icontains=q)
    context = {
        'movies': movie_search,
        'search_term': q
    }
    return render(request, 'core/search.html', context)


@login_required(login_url='login_user')
def genre(request, genre):
    movies = Movie.objects.filter(genre__name=genre)
    context = {
        'movies': movies,
        'movie_genre': genre
    }
    return render(request, 'core/genre.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'User does not exists')

        return render(request, 'core/login.html', {'form': form})

    form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            return redirect('login_user')
        return render(request, 'core/signup.html', {'form': form})

    form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')
