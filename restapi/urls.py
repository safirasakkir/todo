from django.urls import path
from restapi import views

urlpatterns=[
    path("todos",views.TodosView.as_view()),
    path("todos/<int:todo_id>",views.TodoDetails.as_view())
]