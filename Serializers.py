from rest_framework import serializers
from .models import UPost , Vacancy ,Follow
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UPost
        fields = ('Post_Name','Status' ,'Filed','Contant','User_ID','Like')
        read_only_fields = ('User_ID',)
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('VacancyName', 'Title' , 'Requirement' , 'Type' , 'CompanyID','Like')
        read_only_fields = ('CompanyID',)
class FollowSerializer(serializers.ModelSerializer):
     class Meta:
        model = Follow
        fields = ('User_ID', 'FollowsID','FollowsID')
        read_only_fields = ('User_ID',)