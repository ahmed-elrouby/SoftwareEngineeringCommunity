#from django.shortcuts import render, get_object_or_404
#from django.http import JsonResponse
from rest_framework import generics
from .models import Post,Vacancy
from .Serializers import PostSerializer,VacancySerializer

class CeatePost(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CeateVacancy(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save()
        
class VacancyView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer