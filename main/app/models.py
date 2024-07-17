from django.db import models

# Create your models here.
class course(models.Model):
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.course_name