from django.urls import path
from todolist_app import views


urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('pending/<int:task_id>/', views.pending_task, name='pending_task'),
   
]