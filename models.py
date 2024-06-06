from django.db import models



# Create your models here.
Choices = (
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    
)

class TodoItems(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=100, blank=True, null=True)
    datedue = models.DateField(verbose_name="Due Date", blank=True, null=True)
    priority = models.CharField(verbose_name="Priority", choices=Choices, default="Low", null=True)

    def __str__(self):
        return self.title