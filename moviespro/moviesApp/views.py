from django.shortcuts import render
from .models import MovieData
from .serializers import MovieSerializer

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def movieDetails(request):
    if request.method == 'POST':
        moviename = request.POST.get('moviename')
        director = request.POST.get('director')
        release_date = request.POST.get('release_date')
        budget = request.POST.get('budget')
        
        movie = MovieData(moviename=moviename,director=director,release_date=release_date,budget=budget)
        movie.save()
    mve = MovieData.objects.all()
    return render(request, 'index.html',{'movie1':mve})
    
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = MovieData.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return render(request, 'index.html')

@api_view(['GET','PUT','DELETE'])
def movie_details(request,id):
    try:
        movies = MovieData.objects.get(pk=id)
    except MovieData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movies)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





