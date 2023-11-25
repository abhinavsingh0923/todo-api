from django.urls import path
from . import views

urlpatterns = [
    path('alltodo/',views.AllTodoList.as_view()),
    path('delete/todo/<int:id>/',views.TodoById.as_view())
]
