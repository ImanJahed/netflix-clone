from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, SignUpForm
from .models import Movie


# Create your views here.

@login_required(login_url='login_user')
def home(request):
    movies = Movie.objects.all()
    cover = [img.movie_poster for img in movies][-1]

    context = {
        'movies': movies,
        'cover': cover
    }
    return render(request, 'core/home.html', context)


def film_list(request):
    films = Movie.objects.filter(type_movie='Film')
    context = {
        'films': films
    }
    return render(request, 'core/film_list.html', context)


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
