from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = (
        ('F', "Female"),
        ('M', "Male"),
        ('T', "Transgender")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    date_birth = models.DateField(null=True)
    gender_choices = models.CharField(max_length=1, choices=GENDER_CHOICES, default="F")
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class School(models.Model):
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    school_email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.school_name}'

    class Meta:
        ordering = ['school_name', 'school_email', 'school_location']


class Student(models.Model):
    GENDER_CHOICES = (
        ('F', "Female"),
        ('M', "Male"),
        ('T', "Transgender")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    date_birth = models.DateField(null=True)
    gender_choices = models.CharField(max_length=1, choices=GENDER_CHOICES, default="F")
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Course(models.Model):
    Course_Status = (
        ("A", "Activated"),
        ("D", "Dis-activated")
    )
    course_name = models.CharField(max_length=255)
    course_code = models.IntegerField()
    course_description = models.TextField()
    course_status = models.CharField(max_length=1, choices=Course_Status, default="D")
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Result(models.Model):
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
