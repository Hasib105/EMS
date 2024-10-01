from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def normalize_username(self, username):
        return username.strip().lower()  # Normalize the username by stripping whitespace and converting to lowercase

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        username = self.normalize_username(username)  # Call the normalization method here
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email




class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    achievements = models.ManyToManyField('Achievement', through='AchievementEmployee')

    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AchievementEmployee(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    achievement_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.achievement.name} on {self.achievement_date}"