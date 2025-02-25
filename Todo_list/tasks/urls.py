from django.urls import path
from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView


urlpatterns = [
    path('list/', TaskListView.as_view(), name = 'task_list'),
    path('detail/<str:title>', TaskDetailView.as_view(), name = 'task_detail'),
    path('create/', TaskCreateView.as_view(), name = 'new_task'),
    path('edit/<str:title>', TaskUpdateView.as_view(), name = 'edit_task'),
    path('delete/<str:title>', TaskDeleteView.as_view(), name = 'delete_task'),
]