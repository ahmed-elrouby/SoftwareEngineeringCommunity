from rest_framework import serializers
from .models import Post , Vacancy



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('Post_Name','Status' ,'Filed','Contant','User_ID' )
        read_only_fields = ('User_ID',)
class VacancySerializer(serializers.ModelSerializer):
 class Meta:
    model = Vacancy
    fields = ('VacancyName', 'Title' , 'Requirement' , 'Type' , 'CompanyID')
    read_only_fields = ('CompanyID',)