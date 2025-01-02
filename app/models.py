from django.db import models
from accounts.models import Account
from django.utils import timezone
from django.utils.text import slugify
import os

# Create your models here.
class Course(models.Model):
    
    COURSE_CATEGORY = [
        ('Technology', 'Technology'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Engineering', 'Engineering'),
        ('Computer Science', 'Computer Science'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(Account,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnails')
    category = models.CharField(max_length=255,choices=COURSE_CATEGORY, default='Education')
    price = models.IntegerField(default=0)
    isFree = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.price > 0:
            self.isFree = False
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class EnrolledCourse(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='enrolled_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(timezone.now())
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student.name}-{self.course.name}"

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class LessonFile(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='study_material')
    custom_name = models.CharField(blank=True, null=True, max_length=255)
    
    def save(self, *args, **kwargs):
        if self.file:
            ext = os.path.splitext(self.file.name)[-1]
            sanitized_lesson_name = slugify(self.lesson.name)
            if self.custom_name:
                sanitized_name = slugify(self.custom_name)
                self.file.name = f"{sanitized_name}{ext}"
            else:
                self.file.name = f"{sanitized_lesson_name}-{timezone.now().strftime('%Y%m%d%H%M%S')}{ext}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Study Material {self.file.name} of {self.lesson.name}"