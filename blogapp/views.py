from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serialazer import BlogSerialazer,UserSerializer

from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User


from rest_framework import mixins
from rest_framework import generics
# Create your views here.

from .permissions import IsAdminOrReadOnly


@api_view(['GET'])
def getDatas(request):
    blogs=Blog.objects.all()
    
    seria=BlogSerialazer(blogs,many=True)
    print(seria)
    return Response(seria.data)

@api_view(['GET'])
def getData(request,pk):
    blogs=Blog.objects.get(id=pk)
    
    seria=BlogSerialazer(blogs,many=False)
    
    return Response(seria.data)

# @api_view(['POST'])
# def postData(request):
#     seria=BlogSerialazer(data=request.data)
#     if seria.is_valid():
#         seria.save()
#         return Response(seria.data)
#     return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def test(request):
#     blogs=Blog.objects.all()
#     print(blogs)
#     return Response('eeeeeee')




class BlogPost(APIView):
    
    
        
    def get(self, request, format=None):
        
        return Response("eeeeeeeeeeeeeeee")
    def post(self, request, format=None):
        data=request.data
        
        data.update({'owner':self.request.user.id})
        serializer = BlogSerialazer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


