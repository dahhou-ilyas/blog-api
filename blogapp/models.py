from django.db import models

# Create your models here.

class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)