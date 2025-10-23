from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
# Create your models here.

class Contributor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=254,
        unique=True,
        validators=[MinLengthValidator(10)]
    )

    class Meta:
        db_table = 'contributor'
    
class Task(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, unique=True)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'tasks'

class Attendance(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present')

    class Meta:
        db_table = 'attendance'
        unique_together = ['contributor', 'date']  # Prevent duplicate attendance records
        db_table = 'attendance'