from django.db import models
from users.models import User

# Create your models here.
class Task(models.Model):
    PRIORORITY_CHOICE = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    STATUS_CHOICE = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    ]

    title = models.CharField(max_length = 50, unique = True)
    description = models.CharField(max_length = 500)
    due_date = models.DateField()
    priority = models.CharField(max_length = 10, choices = PRIORORITY_CHOICE )
    status = models.CharField(max_length = 10, choices = STATUS_CHOICE, default = 'Pending')
    completed_at = models.DateField(null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    ## check the requirments and work acordingly
    