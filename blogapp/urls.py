from django.urls import path
from . import views

urlpatterns = [
    path('blog/',views.getDatas),
    # path('blogPost/',views.postData),
    path('blog/<str:pk>/',views.getData),
    path('addBlog/',views.BlogPost.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('test/',views.test)
    
]
