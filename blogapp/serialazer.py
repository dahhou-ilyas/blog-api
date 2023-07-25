from blogapp.models import Blog
from rest_framework import serializers
from django.contrib.auth.models import User


class BlogSerialazer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'
        extra_kwargs = {
            'owner': {'write_only': True}
            }
        
        
class UserSerializer(serializers.ModelSerializer):
    blogs = BlogSerialazer(many=True,read_only=True) 
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name','password','blogs')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

