from django.db import models
from account.models import User
# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5ODU5ODY4LCJpYXQiOjE2OTk4NTg2NjgsImp0aSI6IjczMzE3MTRiZGYzNjQ2Yzc4MTBkNmE4ZThkMDBkYjdjIiwidXNlcl9pZCI6MX0.FeS3D_W7zaFs6pWrmc7jjovVVVQJ9zR74KmI6-JpBPQ