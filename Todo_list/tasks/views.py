from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskCreateSerializer, TaskDetailSerializer, TaskListSerializer, TaskUpdateSerializer

# Create your views here.

class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user = self.request.user) # only the current users task will be shown
         ## queries to filter the task list
        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        due_date = self.request.query_params.get('due_date')
        title = self.request.query_params.get('title')

        if title:
            queryset = queryset.filter(title__icontains = title)
        if status:
            queryset = queryset.filter(status = status)
        if priority:
            queryset = queryset.filter(priority = priority)
        if due_date:
            queryset = queryset.filter(due_date = due_date)

        sort_by = self.request.query_params.get('sort_by', 'due_date')
        sort_order = self.request.query_params.get('sort_order', 'asc')

        valid_sort_fields = ['due_date', 'priority', 'status']
        if sort_by not in valid_sort_fields: # cheks if the provided sorting field is valid for sortig if not sort by default due_date ascending
            sort_by = 'due_date'  
        
        if sort_order == 'desc':
            queryset = queryset.order_by(f'-{sort_by}')  # descending order
        else:
            queryset = queryset.order_by(sort_by)  # ascending order

        return queryset

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated]

class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'title' # looks up the task with its title

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
class TaskDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'title'

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
    
class TaskDetailView(generics.RetrieveAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'title' 
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user) 

