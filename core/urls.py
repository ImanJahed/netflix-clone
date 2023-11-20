from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<str:pk>', views.movie, name='movie'),
    path('film-list/', views.film_list, name='film_list'),
    path('series-list/', views.series_list, name='series_list'),
    path('my_list/', views.my_list, name='my_list'),
    path('add-to-list', views.add_to_list, name='add-to-list'),
    path('search/', views.search, name='search'),
    path('genre/<str:genre>', views.genre, name='genre'),




    path('login/', views.login_user, name='login_user'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout', views.logout_user, name='logout_user'),

]