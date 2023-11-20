from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('film-list/', views.film_list, name='film_list'),




    path('login/', views.login_user, name='login_user'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout', views.logout_user, name='logout_user'),

]