from django.urls import path
from .import views

urlpatterns = [
    path('',views.movieDetails,name='movieDetails'),
    path('movies',views.movie_list),
    path('movies/<int:id>',views.movie_details),
]