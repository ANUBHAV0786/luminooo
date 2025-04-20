
STEP 4 

we will a create a databse structure 



    -----======================================--------------
    So now we in this step 4 we will open 

            models.py file inside our main folder 

    inside our models.py we will models for 
        1. Teacher 
            class Teacher(models.Model): 
                full_name = models.CharField(max_length=100)
                email = models.EmailField(unique=True)
                password= models.CharField(max_length=100)
                qualification=models.CharField(max_length=100)
                mobile_number=models.CharField(max_length=15)
                address=models.TextField()
                subject = models.CharField(max_length=100)

        2. 
                # we will  create Course Category Model
                class CourseCategory(models.Model):
                    title = models.CharField(max_length=100)
                    description = models.TextField()
                    created_at = models.DateTimeField(auto_now_add=True)

        3.      # we will create Course Model
                class Course(models.Model):
                    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE) 
                    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
                    title=models.CharField(max_length=100)
                    description=models.TextField()

        4.       # we will create Student Model
                class Student(models.Model):
                    full_name=models.CharField(max_length=100)
                    email=models.EmailField(unique=True)
                    password=models.CharField(max_length=100)
                    mobile_number=models.CharField(max_length=15)
                    address=models.TextField()
                    date_of_birth=models.DateField()
                    interested_categories=models.TextField()


===================================================================================================
===================================================================================================
===================================================================================================

After creating the models we will assign it to admin .

for this we need to migrate and assign it  to  admin panel 

        so first we will use 
                # py manage.py makemigrations
                 then we will use 
                 # py manage.py migrate

        Now open PGADMIN4 we can se our tables have successfully migrated to our postgres DB 

        AFter this wwe will add the models to our admin panel
            for this first open admin.py inside main and we will register our models here 


                    from django.contrib import admin

                    from . import models
                    
                    admin.site.register(models.Teacher)
                    admin.site.register(models.CourseCategory)
                    admin.site.register(models.Course)
                    admin.site.register(models.Student)


After doing the aboe said we will open our server 
        use # py manage.py 
        
        and go to http://127.0.0.1:8000/admin nd login in it
        we will find our tables created at models like teacher, students, categories etc
        