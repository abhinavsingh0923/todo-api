from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers import *

# Create your views here.

class AllTodoList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user= request.user.id
        todo = TodoList.objects.filter(user=user)
        serializer = TodoSerializer(todo,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            data = request.data.copy() 
            # Assuming request.user.id returns an integer
            user_id = request.user.id
            # Adding user_id to the data dictionary
            data.update({"user":user_id})
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Internal Server Error'})
        
class TodoById(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            todo=TodoList.objects.get(id=id)
            todo.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,data={e})