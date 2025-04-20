from django.db import models

# Create your models here.

# we will create first Teacher Model 

class Teacher(models.Model): 
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=15)
    address=models.TextField()
    subject = models.CharField(max_length=100)

# we will  create Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Course Categories"

# we will create Course Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE) 
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()

# we will create Student Model
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=15)
    address=models.TextField()
    date_of_birth=models.DateField()
    interested_categories=models.TextField()
    # interested_courses=models.ManyToManyField(Course, related_name='students')
    # enrolled_courses=models.ManyToManyField(Course, related_name='enrolled_students')
    





    def __str__(self):
        return self.name 
