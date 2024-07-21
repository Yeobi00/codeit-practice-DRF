"""
from django.urls import path
from .views import movie_list, movie_detail, review_list

urlpatterns = [
    path('movies', movie_list),
    path('movies/<int:pk>', movie_detail),
    path('movies/<int:pk>/reviews', review_list),
]
"""
from django.urls import path
from .views import MovieList, MovieDetail, ReviewList

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('movies/<int:pk>/reviews', ReviewList.as_view()),
]