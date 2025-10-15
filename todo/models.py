from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
