from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('female', 'Female'),
        ('male', 'Male')
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, db_index=True, unique=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, unique=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False) 
    date_joined = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return f'{self.first_name or ""} {self.last_name or ""}'
    
    @property
    def username(self):
        return self.email

